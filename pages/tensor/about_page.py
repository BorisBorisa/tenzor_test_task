import allure

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from elements.text import Text
from elements.image import Image

from tools.enums.routes import Routes


class TensorAboutPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.header_logo = Image(self.driver, "main page logo", By.NAME, 'headerLogo')

        self.work_block_title = Text(
            self.driver, "work block title", By.CSS_SELECTOR,
            ".tensor_ru-About__block3 .tensor_ru-About__block-title"
        )
        self.work_block_images = Image(
            self.driver, "work block images", By.XPATH,
            "//img[contains(@class,'tensor_ru-About__block3-image')]"
        )

    @allure.step("Check Tensor About page is opened")
    def is_page_opened(self):
        self.header_logo.check_visible()
        self.check_current_url(Routes.ABOUT.regex_pattern)

    def check_work_block_images_have_equal_dimensions(self):
        self.work_block_images.have_equal_dimensions()
