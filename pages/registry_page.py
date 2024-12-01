import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage
from resources.static_data import ACCOUNT_ID, PROJECT_ID


class RegistryPage(BasePage):
    REL_URL = f'accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}/registry'

    def __init__(self, page: Page):
        self.page = page

        self.button_filters: Locator = page.get_by_role("button", name="Фильтры")
        self.field_search: Locator = page.get_by_placeholder("Поиск")
        self.button_upload: Locator = page.get_by_role("button", name="Загрузить")


    @allure.step('Check registry page elements')
    def check_registry_page_elements(self, timeout=60000):
        self.check_element_is_visible(self.button_filters, timeout=timeout)
        self.check_element_is_visible(self.field_search, timeout=timeout)
        self.check_element_is_visible(self.button_upload, timeout=timeout)
