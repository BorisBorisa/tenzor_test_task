import allure

from abc import ABC, abstractmethod

from selenium.webdriver.common.by import ByType
from selenium.webdriver.remote.webdriver import WebDriver

from tools.browser_tools.waits import Waits
from tools.logger import get_logger

logger = get_logger("BASE_ELEMENT")


class BaseElement(ABC):
    def __init__(self, driver: WebDriver, name: str, locator_type: ByType, locator: str):
        self.driver = driver
        self.waits = Waits(driver)
        self.name = name
        self.locator_type = locator_type
        self.locator = locator

    @property
    @abstractmethod
    def type_of(self) -> str:
        pass

    def get_locator(self, **kwargs) -> tuple[ByType, str]:
        locator = self.locator.format(**kwargs)
        step = f'Getting locator "{locator}"'

        with allure.step(step):
            logger.info(step)
            return self.locator_type, locator

    def click(self, **kwargs):
        locator = self.get_locator(**kwargs)
        step = f'Click {self.type_of} "{self.name}"'

        with (allure.step(step)):
            logger.info(step)
            element = self.waits.clickable(locator)
            element.click()

    def check_visible(self, **kwargs):
        locator = self.get_locator(**kwargs)
        step = f'Checking that {self.type_of} "{self.name}" is visible'

        with allure.step(step):
            logger.info(step)
            self.waits.visible(locator)

    def check_have_text(self, text: str, **kwargs):
        locator = self.get_locator(**kwargs)
        step = f'Checking that {self.type_of} "{self.name}" has text "{text}"'

        with allure.step(step):
            logger.info(step)
            self.waits.have_text(locator, text)
