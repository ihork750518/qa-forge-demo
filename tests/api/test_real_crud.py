import pytest
from qa_forge.api_client import APIClient

@pytest.mark.api
def test_health_over_http(demo_server):
    with APIClient(demo_server) as api:
        r = api.get('/api/health')
        assert r.status_code == 200
        assert r.json() == {'status': 'ok'}

@pytest.mark.api
def test_task_crud_over_http(demo_server):
    with APIClient(demo_server) as api:
        created = api.post('/api/tasks', json={'title': 'Release QA Forge'})
        assert created.status_code == 201
        item = created.json()
        assert item['title'] == 'Release QA Forge'
        listing = api.get('/api/tasks')
        assert listing.status_code == 200
        assert item in listing.json()
        deleted = api.request('DELETE', f"/api/tasks/{item['id']}")
        assert deleted.status_code == 200
        assert api.get('/api/tasks').json() == []

@pytest.mark.api
def test_invalid_task_is_rejected(demo_server):
    with APIClient(demo_server) as api:
        r = api.post('/api/tasks', json={'title': '  '})
        assert r.status_code == 400
        assert r.json()['error'] == 'title_required'
