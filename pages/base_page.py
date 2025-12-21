import allure

from selenium.webdriver.remote.webdriver import WebDriver

from tools.browser_tools.waits import Waits


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.waits = Waits(driver)

    def visit(self, url: str):
        step = f"Opening the url '{url}'"

        with allure.step(step):
            self.driver.get(url)

    def reload(self):
        url = self.driver.current_url
        step = f"Reloading page with url '{url}'"

        with allure.step(step):
            self.driver.refresh()

    def check_current_url(self, expected_url: str):
        step = f'Checking that current url matches "{expected_url}"'

        with allure.step(step):
            self.waits.url_matches(expected_url)

    def check_title_contains(self, title: str):
        step = f'Checking that current title contains "{title}"'

        with allure.step(step):
            self.waits.title_contains(title)
