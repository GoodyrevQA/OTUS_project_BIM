import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class AccountsPage(BasePage):
    REL_URL = 'accounts'

    def __init__(self, page: Page):
        self.page = page

        self.button_active: Locator = page.get_by_role("button", name="Активные")
        self.button_archived: Locator = page.get_by_role("button", name="Архивные")
        self.button_create_account: Locator = page.get_by_role("button", name="Создать аккаунт")
        self.text_accounts: Locator = page.get_by_text("Аккаунты", exact=True)
