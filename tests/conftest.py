import allure
import pytest
from qa_forge.config import get_settings


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default=None, help="dev, stage or prod")


@pytest.fixture(scope="session")
def settings(request):
    return get_settings(request.config.getoption("--env"))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed and "page" in item.funcargs:
        page = item.funcargs["page"]
        try:
            allure.attach(page.screenshot(full_page=True), name="failure-screenshot",
                          attachment_type=allure.attachment_type.PNG)
        except Exception:
            pass  # Do not hide the original assertion failure.


@pytest.fixture
def demo_server():
    """Isolated real HTTP server per test, bound to localhost on a free port."""
    from threading import Thread
    from demo_app.server import DemoServer
    server = DemoServer(("127.0.0.1", 0))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        thread.join(timeout=5)
        server.server_close()
