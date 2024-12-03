import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage
from resources.static_data import ACCOUNT_ID


class ProjectsPage(BasePage):
    REL_URL = f'accounts/{ACCOUNT_ID}/projects'

    def __init__(self, page: Page):
        self.page = page

        self.button_active: Locator = page.locator("//div[@role='button' and text()='Активные']")
        self.button_archived: Locator = page.locator("//div[@role='button' and text()='Архивные']")
        self.field_search: Locator = page.locator("//input[@data-testid='input-search']")
        self.icon_search: Locator = page.locator("//*[@data-testid='SearchOutline']")
