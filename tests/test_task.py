from pathlib import Path

from pages.saby.main_page import SabyMainPage
from pages.saby.contacts_page import SabyContactsPage
from pages.saby.download_page import SabyDownloadPage
from pages.tensor.main_page import TensorMainPage
from pages.tensor.about_page import TensorAboutPage

from tools.enums.urls import URLs
from tools.assertions.files import assert_file_size

from config import settings

test_data = settings.test_data


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

    def test_second_scenario(
            self,
            saby_main_page: SabyMainPage,
            saby_contacts_page: SabyContactsPage
    ):
        saby_main_page.visit(URLs.SABY_URL)
        saby_main_page.is_page_opened()

        saby_main_page.contacts_button_click()
        saby_main_page.contacts_popup_menu.check_visible()
        saby_main_page.contacts_popup_menu.click_contacts_link()

        saby_contacts_page.is_page_opened()
        saby_contacts_page.check_region_chooser_link_text(test_data.initial_region)

        partners_for_initial_region = saby_contacts_page.get_partners_by_city()

        saby_contacts_page.region_chooser_link_click()
        saby_contacts_page.region_selection_dialog.check_visible()
        saby_contacts_page.region_selection_dialog.region_item_link_click(test_data.new_region)

        saby_contacts_page.check_region_chooser_link_text(test_data.new_region)
        saby_contacts_page.check_has_partners_changed(partners_for_initial_region)
        saby_contacts_page.check_current_url(test_data.expected_url_part)
        saby_contacts_page.check_title_contains(test_data.expected_region_title_part)

    def test_third_scenario(
            self,
            saby_main_page: SabyMainPage,
            saby_download_page: SabyDownloadPage,
            tmp_path: Path
    ):
        saby_main_page.visit(URLs.SABY_URL)
        saby_main_page.is_page_opened()

        saby_main_page.footer.click_download_local_versions_link()

        saby_download_page.is_page_opened()

        saby_download_page.saby_desktop_tab_button_click()
        saby_download_page.saby_desktop_windows_tab_button_click()
        saby_download_page.download_saby_desktop_for_windows(tmp_path, test_data.saby_desktop_for_windows_app_file_name)

        assert_file_size(
            tmp_path,
            test_data.saby_desktop_for_windows_app_file_name,
            test_data.saby_desktop_for_windows_app_size
        )
