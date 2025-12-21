import pytest
from _pytest.fixtures import SubRequest

from tools.webdriver.browser import get_browser_driver

from config import settings


@pytest.fixture(autouse=True, params=settings.browsers)
def driver(request: SubRequest):
    driver = get_browser_driver(request.param)
    yield driver
    driver.quit()
