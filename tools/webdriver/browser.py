from abc import ABC, abstractmethod

from typing import Type
from pathlib import Path

from selenium.webdriver import (
    Chrome, ChromeOptions,
    Firefox, FirefoxOptions, FirefoxProfile
)

from selenium.webdriver.remote.webdriver import WebDriver

from config import settings, Browser
from tools.logger import get_logger

logger = get_logger("BROWSER")


class BaseBrowser(ABC):
    def __init__(self, driver_class, options_class, browser_config):
        self.driver_class: Type[WebDriver] = driver_class
        self.options_class = options_class
        self.browser_config = browser_config

    def create_driver(self) -> WebDriver:
        options = self.options_class()

        for arg in self.browser_config.options:
            options.add_argument(arg)

        options.page_load_strategy = settings.browsers_config.page_load_strategy

        self.configure_download_folder(options)

        driver = self.driver_class(options=options)
        driver.set_page_load_timeout(settings.browsers_config.page_load_timeout)

        return driver

    @abstractmethod
    def configure_download_folder(self, options):
        pass


class ChromeBrowser(BaseBrowser):
    def __init__(self, download_dir: Path):
        super().__init__(Chrome, ChromeOptions, settings.browsers_config.chromium_config)
        self.download_dir = download_dir

    def configure_download_folder(self, options):
        options.add_experimental_option("prefs", {
            "download.default_directory": str(self.download_dir),
            "safebrowsing.enabled": True
        })


class FirefoxBrowser(BaseBrowser):
    def __init__(self, download_dir: Path):
        super().__init__(Firefox, FirefoxOptions, settings.browsers_config.firefox_config)
        self.download_dir = download_dir

    def configure_download_folder(self, options):
        profile = FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.dir", str(self.download_dir))
        options.profile = profile


def get_browser_driver(browser_name: Browser, tmp_path: Path) -> WebDriver:
    logger.info(f"Initializing WebDriver for browser: {browser_name.value}")
    match browser_name:
        case Browser.CHROME:
            return ChromeBrowser(tmp_path).create_driver()
        case Browser.FIREFOX:
            return FirefoxBrowser(tmp_path).create_driver()
        case _:
            raise ValueError(f"Неизвестный браузер: {browser_name}")
