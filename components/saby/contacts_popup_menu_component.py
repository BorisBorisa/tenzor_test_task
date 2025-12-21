from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from elements.link import Link


class ContactsPopupMenuComponent(BaseComponent):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.sbisru_link = Link(driver, "sbis ru", By.XPATH, "//*[@id='popup']//a[contains(@class, 'sbisru-link')]")

    def check_visible(self):
        self.sbisru_link.check_visible()

    def click_sbisru_link(self):
        self.sbisru_link.click()
