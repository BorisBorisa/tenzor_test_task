import pytest

from selenium.webdriver.remote.webdriver import WebDriver

from pages.saby.main_page import SabyMainPage
from pages.saby.contacts_page import SabyContactsPage
from pages.saby.download_page import SabyDownloadPage

from pages.tensor.main_page import TensorMainPage
from pages.tensor.about_page import TensorAboutPage


@pytest.fixture
def saby_main_page(driver: WebDriver) -> SabyMainPage:
    return SabyMainPage(driver)


@pytest.fixture
def saby_contacts_page(driver: WebDriver) -> SabyContactsPage:
    return SabyContactsPage(driver)


@pytest.fixture
def saby_download_page(driver: WebDriver) -> SabyDownloadPage:
    return SabyDownloadPage(driver)


@pytest.fixture
def tensor_main_page(driver: WebDriver) -> TensorMainPage:
    return TensorMainPage(driver)


@pytest.fixture
def tensor_about_page(driver: WebDriver) -> TensorAboutPage:
    return TensorAboutPage(driver)
