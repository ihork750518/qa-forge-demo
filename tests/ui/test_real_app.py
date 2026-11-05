import pytest
from playwright.sync_api import expect

@pytest.mark.ui
def test_create_task_in_real_browser(page, demo_server):
    page.goto(demo_server)
    expect(page.get_by_role('heading', name='QA Forge Tasks')).to_be_visible()
    page.locator('#task').fill('Write Playwright tests')
    page.get_by_role('button', name='Add task').click()
    expect(page.locator('#tasks li')).to_have_text(['Write Playwright tests'])

@pytest.mark.ui
def test_task_list_starts_empty(page, demo_server):
    page.goto(demo_server)
    expect(page.locator('#tasks li')).to_have_count(0)
