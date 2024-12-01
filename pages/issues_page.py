import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage
from resources.static_data import ACCOUNT_ID, PROJECT_ID


class IssuesPage(BasePage):
    REL_URL = f'accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}/issues'

    def __init__(self, page: Page):
        self.page = page

        # иконка Фильтры и все, что справа от нее
        self.button_filters: Locator = page.locator("//*[@data-testid='icon__setting_slider']")
        self.button_all: Locator = page.locator("//div[@title='Все']")
        self.button_only_mine: Locator = page.locator("//div[@title='Только мои']")
        self.button_assigned_to_me: Locator = page.locator("//div[@title='Назначены мне']")
        self.field_search: Locator = page.get_by_placeholder("Введите название замечания или пользователя")
        self.icon_search: Locator = page.locator("//*[@data-testid='SearchOutline']")
        self.icon_download: Locator = page.locator("//*[@data-testid='ExportOutline']")

        # шапка таблицы
        self.column_ID: Locator = page.locator("//span[text()='ID']")
        self.column_category: Locator = page.locator("//span[text()='Категория']")
        self.column_type: Locator = page.locator("//span[text()='Тип']")
        self.column_name: Locator = page.locator("//span[text()='Название']")
        self.column_to_whom: Locator = page.locator("//span[text()='Кому']")
        self.column_from_whom: Locator = page.locator("//span[text()='От кого']")
        self.column_due_date: Locator = page.locator("//span[text()='Дата устранения']")
        self.column_created_date: Locator = page.locator("//span[text()='Дата создания']")
        self.column_modified_date: Locator = page.locator("//span[text()='Дата изменения']")
        self.column_modified_by: Locator = page.locator("//span[text()='Кем изменено']")

 
    @allure.step('Check issues page elements')
    def check_issues_page_elements(self, timeout=60000):
        self.check_element_is_visible(self.button_filters, timeout=timeout)
        self.check_element_is_visible(self.button_all, timeout=timeout)
        self.check_element_is_visible(self.button_only_mine, timeout=timeout)
        self.check_element_is_visible(self.button_assigned_to_me, timeout=timeout)
        self.check_element_is_visible(self.field_search, timeout=timeout)
        self.check_element_is_visible(self.icon_search, timeout=timeout)
        self.check_element_is_visible(self.icon_download, timeout=timeout)

        self.check_element_is_visible(self.column_ID, timeout=timeout)
        self.check_element_is_visible(self.column_category, timeout=timeout)
        self.check_element_is_visible(self.column_type, timeout=timeout)
        self.check_element_is_visible(self.column_name, timeout=timeout)
        self.check_element_is_visible(self.column_to_whom, timeout=timeout)
        self.check_element_is_visible(self.column_from_whom, timeout=timeout)
        self.check_element_is_visible(self.column_due_date, timeout=timeout)
        self.check_element_is_visible(self.column_created_date, timeout=timeout)
        self.check_element_is_visible(self.column_modified_date, timeout=timeout)
        self.check_element_is_visible(self.column_modified_by, timeout=timeout)
