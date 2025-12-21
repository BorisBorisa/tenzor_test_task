from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent

from elements.text import Text
from elements.link import Link


class RegionSelectDialogComponent(BaseComponent):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.header = Text(
            driver, "Region select dialog header", By.CSS_SELECTOR, ".sbis_ru-Region-Panel__header-text"
        )
        self.region_item_link = Link(
            driver, "Region item", By.XPATH, "//*[@name='dialog']//*[contains(text(), '{region}')]"
        )

    def check_visible(self):
        self.header.check_visible()

    def region_item_link_click(self, region: str):
        self.region_item_link.click(region=region)
