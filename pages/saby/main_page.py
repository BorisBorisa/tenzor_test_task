import allure

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from components.saby.contacts_popup_menu_component import ContactsPopupMenuComponent
from components.saby.footer_component import FooterComponent

from elements.image import Image
from elements.button import Button


class SabyMainPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.logo = Image(driver, "Main logo", By.ID, "main_page_logo")
        self.contacts_button = Button(driver, "Contacts", By.XPATH, "//*[@class='sbisru-Header']//*[text()='Контакты']")

        self.contacts_popup_menu = ContactsPopupMenuComponent(driver)
        self.footer = FooterComponent(driver)

    @allure.step("Check Main page is opened")
    def is_page_opened(self):
        self.logo.check_visible()

    def contacts_button_click(self):
        self.contacts_button.click()
