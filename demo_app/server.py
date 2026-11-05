"""Local demo app: HTTP JSON CRUD + a browser UI. Not for public deployment."""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Lock
from urllib.parse import urlsplit

HTML = """<!doctype html><html lang='en'><meta charset='utf-8'><title>QA Forge Tasks</title>
<h1>QA Forge Tasks</h1><label>Task <input id='task' /></label>
<button id='add'>Add task</button><ul id='tasks'></ul>
<script>
async function refresh(){const r=await fetch('/api/tasks');const items=await r.json();
 document.querySelector('#tasks').replaceChildren(...items.map(t=>{let li=document.createElement('li');li.textContent=t.title;return li;}));}
document.querySelector('#add').onclick=async()=>{let input=document.querySelector('#task');
 await fetch('/api/tasks',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({title:input.value})});
 input.value='';await refresh();};refresh();
</script></html>"""

class DemoServer(ThreadingHTTPServer):
    def __init__(self, address):
        super().__init__(address, Handler)
        self.tasks = {}
        self.next_id = 1
        self.lock = Lock()

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def send(self, status, payload):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = urlsplit(self.path).path
        if path == '/':
            body = HTML.encode()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif path == '/api/health':
            self.send(200, {'status': 'ok'})
        elif path == '/api/private/profile':
            if self.headers.get('Authorization') != 'Bearer demo-token':
                return self.send(401, {'error': 'unauthorized'})
            self.send(200, {'username': 'demo-user', 'role': 'tester'})
        elif path == '/api/tasks':
            with self.server.lock:
                self.send(200, list(self.server.tasks.values()))
        else:
            self.send(404, {'error': 'not_found'})

    def do_POST(self):
        if urlsplit(self.path).path != '/api/tasks':
            return self.send(404, {'error': 'not_found'})
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if length < 0: return self.send(400, {'error': 'invalid_length'})
            if length > 10000: return self.send(413, {'error': 'too_large'})
            data = json.loads(self.rfile.read(length))
            title = data.get('title')
            if not isinstance(title, str) or not title.strip():
                return self.send(400, {'error': 'title_required'})
        except (ValueError, TypeError, AttributeError):
            return self.send(400, {'error': 'invalid_json'})
        with self.server.lock:
            item = {'id': self.server.next_id, 'title': title.strip()}
            self.server.tasks[item['id']] = item
            self.server.next_id += 1
        self.send(201, item)

    def do_DELETE(self):
        path = urlsplit(self.path).path
        try:
            item_id = int(path.removeprefix('/api/tasks/')) if path.startswith('/api/tasks/') else -1
        except ValueError:
            item_id = -1
        with self.server.lock:
            found = self.server.tasks.pop(item_id, None)
        self.send(200 if found else 404, {'deleted': True} if found else {'error': 'not_found'})
