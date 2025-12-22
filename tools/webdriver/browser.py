from abc import ABC, abstractmethod

from typing import Type
from pathlib import Path

from selenium.webdriver import Chrome, ChromeOptions

from selenium.webdriver.remote.webdriver import WebDriver

from config import settings
from tools.logger import get_logger

logger = get_logger("BROWSER")


class BaseBrowser(ABC):
    def __init__(self, driver_class, options_class, browser_config):
        self.driver_class: Type[WebDriver] = driver_class
        self.options_class = options_class
        self.browser_config = browser_config

    def create_driver(self) -> WebDriver:
        options = self.options_class()
        for arg in self.browser_config:
            options.add_argument(arg)

        options.page_load_strategy = settings.browser_config.page_load_strategy
        self.configure_download_folder(options)

        driver = self.driver_class(options=options)
        driver.set_page_load_timeout(settings.browser_config.page_load_timeout)
        return driver

    @abstractmethod
    def configure_download_folder(self, options):
        pass


class ChromeBrowser(BaseBrowser):
    def __init__(self, download_dir: Path):
        super().__init__(Chrome, ChromeOptions, settings.browser_config.chromium_options)
        self.download_dir = download_dir

    def configure_download_folder(self, options):
        options.add_experimental_option("prefs", {
            "download.default_directory": str(self.download_dir),
            "safebrowsing.enabled": True
        })


def get_chrome_browser_driver(tmp_path: Path) -> WebDriver:
    logger.info(f"Initializing WebDriver for chrome browser")
    return ChromeBrowser(tmp_path).create_driver()
