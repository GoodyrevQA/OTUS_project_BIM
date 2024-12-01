import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage
from resources.static_data import ACCOUNT_ID


class ProjectsPage(BasePage):
    REL_URL = f'/accounts/{ACCOUNT_ID}/projects'

    def __init__(self, page: Page):
        self.page = page

        self.button_active: Locator = page.get_by_role("button", name="Активные")
        self.button_archived: Locator = page.get_by_role("button", name="Архивные")
        self.button_create_project: Locator = page.get_by_role("button", name="Создать проект")

        # Проекты в хэдере страницы
        self.text_projects: Locator = page.get_by_text("Проекты", exact=True)
