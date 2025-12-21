from collections import defaultdict

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium.common import NoSuchElementException

from pages.base_page import BasePage

from components.saby.region_select_dialog import RegionSelectDialogComponent

from elements.link import Link


class SabyContactsPage(BasePage):
    CONTACT_LIST_ITEM_LOCATOR = By.XPATH, "//*[@data-qa='items-container']/*[@data-qa='item']"
    CITY_LOCATOR = By.CLASS_NAME, "sbisru-Contacts-List__city"
    PARTNER_NAME_LOCATOR = By.CLASS_NAME, "sbisru-Contacts-List__name"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.contact_clients_tensor_logo = Link(
            driver, "Tensor logo", By.CSS_SELECTOR, "#contacts_clients .sbisru-Contacts__logo-tensor"
        )
        self.region_chooser_link = Link(
            driver, "Region chooser", By.CSS_SELECTOR, ".sbisru-Contacts__relative .sbis_ru-Region-Chooser__text"
        )
        self.region_selection_dialog = RegionSelectDialogComponent(driver)

    def is_page_opened(self):
        pass

    def contact_clients_tensor_logo_click(self):
        with self.waits.wait_and_switch_to_new_tab():
            self.contact_clients_tensor_logo.click()

    def region_chooser_link_click(self):
        self.region_chooser_link.click()

    def check_region_chooser_link_text(self, text: str):
        self.region_chooser_link.check_have_text(text)

    def get_partners_by_city(self) -> dict[str, set[str]]:
        items = self.waits.visible_all(self.CONTACT_LIST_ITEM_LOCATOR)

        partners_by_city = defaultdict(set)
        current_city = None

        for item in items:
            try:
                current_city = item.find_element(*self.CITY_LOCATOR).text
            except NoSuchElementException:
                partner_name = item.find_element(*self.PARTNER_NAME_LOCATOR).text
                partners_by_city[current_city].add(partner_name)

        return partners_by_city

    def check_has_partners_changed(self, previous_partners: dict[str, set[str]]):
        current_partners = self.get_partners_by_city()

        assert previous_partners != current_partners, "Partners list did not change"
