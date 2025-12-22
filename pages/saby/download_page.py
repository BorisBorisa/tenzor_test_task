import allure
from pathlib import Path

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from elements.text import Text
from elements.button import Button
from elements.link import Link

from tools.enums.routes import Routes


class SabyDownloadPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.title = Text(
            driver, "download page title", By.XPATH, "//h1[text()='СКАЧАТЬ']"
        )
        self.saby_desktop_tab_button = Button(
            driver, "Saby desktop app tab", By.XPATH, "//*[@data-id='plugin']"
        )
        self.saby_desktop_windows_tab_button = Button(
            driver, "Saby desktop windows app tab", By.XPATH, "//*[@data-for='plugin']//*[@data-id='default']"
        )
        self.saby_desktop_windows_download_link = Link(
            driver, "Saby desktop windows app download", By.XPATH,
            "//*[@data-for='default']//a[contains(@href, '/win32/{file_name}')] "
        )

    @allure.step("Check Saby download page is opened")
    def is_page_opened(self):
        self.check_current_url(Routes.DOWNLOAD.regex_pattern)
        self.title.check_visible()

    def saby_desktop_tab_button_click(self):
        self.saby_desktop_tab_button.click()

    def saby_desktop_windows_tab_button_click(self):
        self.saby_desktop_windows_tab_button.click()

    def download_saby_desktop_for_windows(self, download_dir: Path, file_name: str):
        with self.waits.wait_file_download(download_dir, file_name):
            self.saby_desktop_windows_download_link.click(file_name=file_name)
