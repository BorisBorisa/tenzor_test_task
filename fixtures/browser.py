import pytest
from _pytest.fixtures import SubRequest
from pathlib import Path

from tools.webdriver.browser import get_browser_driver
from selenium.webdriver.remote.webdriver import WebDriver

from config import settings


@pytest.fixture(autouse=True, params=settings.browsers)
def driver(request: SubRequest, tmp_path: Path) -> WebDriver:
    driver = get_browser_driver(request.param, tmp_path)
    yield driver
    driver.quit()
