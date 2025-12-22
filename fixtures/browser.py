import pytest
from pathlib import Path

from tools.webdriver.browser import get_chrome_browser_driver
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def driver(tmp_path: Path) -> WebDriver:
    driver = get_chrome_browser_driver(tmp_path)
    yield driver
    driver.quit()
