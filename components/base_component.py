import allure

from selenium.webdriver.remote.webdriver import WebDriver

from tools.browser_tools.waits import Waits
from tools.logger import get_logger

logger = get_logger("BASE_COMPONENT")


class BaseComponent:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.waits = Waits(driver)

    def check_current_url(self, expected_url: str):
        step = f"Check that current URL matches expected: '{expected_url}'"

        with allure.step(step):
            logger.info(step)
            self.waits.url_matches(expected_url)
