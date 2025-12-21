from pages.saby.main_page import SabyMainPage
from pages.saby.contacts_page import SabyContactsPage

from pages.tensor.main_page import TensorMainPage
from pages.tensor.about_page import TensorAboutPage

from tools.enums.urls import URLs

class TestTask:
    def test_first_scenario(
            self,
            saby_main_page: SabyMainPage,
            saby_contacts_page: SabyContactsPage,
            tensor_main_page: TensorMainPage,
            tensor_about_page: TensorAboutPage
    ):
        saby_main_page.visit(URLs.SABY_URL)
        saby_main_page.is_page_opened()

        saby_main_page.contacts_button_click()
        saby_main_page.contacts_popup_menu.check_visible()
        saby_main_page.contacts_popup_menu.click_contacts_link()

        saby_contacts_page.is_page_opened()
        saby_contacts_page.contact_clients_tensor_logo_click()

        tensor_main_page.is_page_opened()
        tensor_main_page.check_about_team_block_visible()
        tensor_main_page.about_team_block_more_link_click()

        tensor_about_page.is_page_opened()
        tensor_about_page.check_work_block_visible()
        tensor_about_page.check_work_block_images_have_equal_dimensions()

    def test_second_scenario(self):
        pass

    def test_third_scenario(self):
        pass