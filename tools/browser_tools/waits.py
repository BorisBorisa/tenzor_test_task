import os
from contextlib import contextmanager

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import settings


class Waits:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver=driver,
            timeout=settings.browsers_config.wait_timeout,
            poll_frequency=settings.browsers_config.wait_poll_frequency
        )

    def visible(self, locator) -> WebElement:
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def visible_all(self, locator) -> list[WebElement]:
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )

    def clickable(self, locator) -> WebElement:
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def have_text(self, locator, text):
        self.wait.until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def url_matches(self, pattern: str):
        self.wait.until(
            EC.url_matches(pattern)
        )

    def title_contains(self, title: str):
        self.wait.until(
            EC.title_contains(title)
        )

    @contextmanager
    def wait_and_switch_to_new_tab(self):
        old_handles = set(self.driver.window_handles)
        yield
        self.wait.until(EC.new_window_is_opened(old_handles))
        new_handle = (set(self.driver.window_handles) - old_handles).pop()
        self.driver.switch_to.window(new_handle)

    @contextmanager
    def wait_file_download(self, download_dir, file_name):
        file_path = os.path.join(download_dir, file_name)
        yield
        self.wait.until(lambda driver: os.path.exists(file_path))
