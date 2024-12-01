import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage
from resources.static_data import ACCOUNT_ID, PROJECT_ID


class DocumentationPage(BasePage):
    REL_URL = f'accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}/documentation'

    def __init__(self, page: Page):
        self.page = page

        self.text_files_of_project: Locator = page.locator("span").filter(has_text="Файлы проекта")
        self.text_favorite_folders: Locator = page.get_by_text("Избранные папки")
        self.text_bin: Locator = page.get_by_text("Корзина")

        self.button_roll_up: Locator = page.get_by_role("button", name="Свернуть")
        self.button_write_to_admin: Locator = page.get_by_role("button", name="Написать администратору")

        self.field_search: Locator = page.locator("input[type=\"text\"]")
        self.icon_search: Locator = page.locator("//*[@data-testid='SearchOutline']")
        self.link_files_of_project: Locator = page.get_by_role("link", name="Файлы проекта")


    @allure.step('Check documentation page elements')
    def check_documentation_page_elements(self, timeout=60000):
        self.check_element_is_visible(self.text_files_of_project, timeout=timeout)
        self.check_element_is_visible(self.text_favorite_folders, timeout=timeout)
        self.check_element_is_visible(self.text_bin, timeout=timeout)
        self.check_element_is_visible(self.button_roll_up, timeout=timeout)
        self.check_element_is_visible(self.field_search, timeout=timeout)
        self.check_element_is_visible(self.icon_search, timeout=timeout)
        self.check_element_is_visible(self.link_files_of_project, timeout=timeout)
