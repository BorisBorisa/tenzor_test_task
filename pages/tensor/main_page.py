import allure

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from elements.text import Text
from elements.link import Link
from elements.image import Image


class TensorMainPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.header_logo = Image(self.driver, "main page logo", By.NAME, 'headerLogo')

        self.about_team_block_title = Text(
            self.driver, "about team block title", By.CSS_SELECTOR,
            ".tensor_ru-Index__block4-bg .tensor_ru-Index__card-title"
        )
        self.about_team_block_more_link = Link(
            self.driver, "about team block more link", By.CSS_SELECTOR,
            ".tensor_ru-Index__block4-bg .tensor_ru-link"
        )

    @allure.step("Check Tensor Main page is opened")
    def is_page_opened(self):
        self.header_logo.check_visible()

    def check_about_team_block_visible(self):
        self.about_team_block_title.check_visible()
        self.about_team_block_more_link.check_visible()

    def about_team_block_more_link_click(self):
        self.about_team_block_more_link.click()
