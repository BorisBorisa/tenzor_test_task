from typing import Type

from selenium.webdriver import (
    Chrome, ChromeOptions,
    Firefox, FirefoxOptions,
    Edge, EdgeOptions
)

from selenium.webdriver.remote.webdriver import WebDriver

from config import settings, Browser
from tools.logger import get_logger

logger = get_logger("BROWSER")


class BaseBrowser:
    def __init__(self, driver_class, options_class, browser_config):
        self.driver_class: Type[WebDriver] = driver_class
        self.options_class = options_class
        self.browser_config = browser_config

    def create_driver(self) -> WebDriver:
        options = self.options_class()

        for arg in self.browser_config.options:
            options.add_argument(arg)

        options.page_load_strategy = settings.browsers_config.page_load_strategy

        driver = self.driver_class(options=options)
        driver.set_page_load_timeout(settings.browsers_config.page_load_timeout)

        return driver


class ChromeBrowser(BaseBrowser):
    def __init__(self):
        super().__init__(Chrome, ChromeOptions, settings.browsers_config.chromium_config)


class FirefoxBrowser(BaseBrowser):
    def __init__(self):
        super().__init__(Firefox, FirefoxOptions, settings.browsers_config.firefox_config)


class EdgeBrowser(BaseBrowser):
    def __init__(self):
        super().__init__(Edge, EdgeOptions, settings.browsers_config.chromium_config)


def get_browser_driver(browser_name: Browser) -> WebDriver:
    logger.info(f"Initializing WebDriver for browser: {browser_name.value}")
    match browser_name:
        case Browser.CHROME:
            return ChromeBrowser().create_driver()
        case Browser.FIREFOX:
            return FirefoxBrowser().create_driver()
        case Browser.EDGE:
            return EdgeBrowser().create_driver()
        case _:
            raise ValueError(f"Неизвестный браузер: {browser_name}")
