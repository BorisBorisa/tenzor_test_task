from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from elements.link import Link


class FooterComponent(BaseComponent):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.download_local_versions_link = Link(
            driver, "download local versions", By.XPATH,
            "//*[contains(@class, 'sbisru-Footer')]//*[text()='Скачать локальные версии']"
        )

    def check_visible(self):
        self.download_local_versions_link.check_visible()

    def click_download_local_versions_link(self):
        self.download_local_versions_link.click()
