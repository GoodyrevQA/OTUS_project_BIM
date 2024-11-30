import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage
from resources.static_data import ACCOUNT_ID, PROJECT_ID


class MembersPage(BasePage):
    REL_URL = f'accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}/members'

    def __init__(self, page: Page):
        self.page = page

        self.button_active: Locator = page.get_by_role("button", name="Активные")
        self.button_archived: Locator = page.get_by_role("button", name="Архивные")

        self.field_search: Locator = page.get_by_placeholder("Поиск по Ф.И.О, email, телефон")
        self.icon_search: Locator = page.locator("//*[@data-testid='SearchOutline']")

        self.button_add_a_company: Locator = page.get_by_role("button", name="Добавить компанию")
        self.button_add_members: Locator = page.get_by_role("button", name="Добавить участников")

        self.field_quick_jumper_input: Locator = page.get_by_test_id("quick-jumper-input")


    @allure.step('Check members page elements with add buttons')
    def check_members_page_elements_with_add_buttons(self, timeout=60000):
        self.check_element_is_visible(self.button_active, timeout=timeout)
        self.check_element_is_visible(self.button_archived, timeout=timeout)
        self.check_element_is_visible(self.icon_search, timeout=timeout)
        self.check_element_is_visible(self.field_search, timeout=timeout)
        self.check_element_is_visible(self.button_add_a_company, timeout=timeout)
        self.check_element_is_visible(self.button_add_members, timeout=timeout)
        self.check_element_is_visible(self.field_quick_jumper_input, timeout=timeout)
        

    @allure.step('Check members page elements without add buttons')
    def check_members_page_elements_without_add_buttons(self, timeout=120000):
        self.check_element_is_visible(self.button_active, timeout=timeout)
        self.check_element_is_visible(self.button_archived, timeout=timeout)
        self.check_element_is_visible(self.icon_search, timeout=timeout)
        self.check_element_is_visible(self.field_search, timeout=timeout)
        self.check_element_is_visible(self.field_quick_jumper_input, timeout=timeout)
  