import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage
from resources.static_data import ACCOUNT_ID, PROJECT_ID


class MidpPage(BasePage):
    REL_URL = f'accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}/midp'

    def __init__(self, page: Page):
        self.page = page

        # иконка Фильтры и все, что справа от нее
        self.button_filters: Locator = page.locator("//*[@data-testid='icon__setting_slider']")
        self.button_overdue: Locator = page.get_by_role("button", name="Просрочено")
        self.button_assigned_to_me: Locator = page.get_by_role("button", name="Назначено мне")
        self.field_search: Locator = page.get_by_placeholder("Комплект, Шифр, ВПР")
        self.icon_search: Locator = page.locator("//*[@data-testid='SearchOutline']")
        self.icon_download: Locator = page.locator("//*[@data-testid='ExportOutline']")
        self.icon_upload: Locator = page.locator("//*[@data-testid='ImportOutline']")

        # шапка таблицы
        self.column_section: Locator = page.locator("//span[text()='Раздел']")
        self.column_executor: Locator = page.locator("//span[text()='Исполнитель']")
        self.column_BIM_model_code: Locator = page.locator("//span[text()='Шифр BIM-модели']")
        self.column_kit_code: Locator = page.locator("//span[text()='Шифр комплекта']")
        self.column_kit_name: Locator = page.locator("//span[text()='Наименование комплекта']")
        self.column_planned_date_of_BIM_model_transfer: Locator = page.locator("//span[text()='Плановая дата передачи BIM-модели']")
        self.column_kit_status: Locator = page.locator("//span[text()='Статус комплекта']")
        self.column_actual_date_of_BIM_model_transfer: Locator = page.locator("//span[text()='Фактическая дата передачи BIM-модели']")
        self.column_VPR: Locator = page.locator("//span[text()='ВПР']")
        self.column_version: Locator = page.locator("//span[text()='Версия']")


    @allure.step('Check MIDP page elements')
    def check_midp_page_elements(self, timeout=60000):
        self.check_element_is_visible(self.button_filters, timeout=timeout)
        self.check_element_is_visible(self.button_overdue, timeout=timeout)
        self.check_element_is_visible(self.button_assigned_to_me, timeout=timeout)
        self.check_element_is_visible(self.field_search, timeout=timeout)
        self.check_element_is_visible(self.icon_search, timeout=timeout)
        self.check_element_is_visible(self.icon_download, timeout=timeout)
        self.check_element_is_visible(self.icon_upload, timeout=timeout)

        self.check_element_is_visible(self.column_section, timeout=timeout)
        self.check_element_is_visible(self.column_executor, timeout=timeout)
        self.check_element_is_visible(self.column_BIM_model_code, timeout=timeout)
        self.check_element_is_visible(self.column_kit_code, timeout=timeout)
        self.check_element_is_visible(self.column_kit_name, timeout=timeout)
        self.check_element_is_visible(self.column_planned_date_of_BIM_model_transfer, timeout=timeout)
        self.check_element_is_visible(self.column_kit_status, timeout=timeout)
        self.check_element_is_visible(self.column_actual_date_of_BIM_model_transfer, timeout=timeout)
        self.check_element_is_visible(self.column_VPR, timeout=timeout)
        self.check_element_is_visible(self.column_version, timeout=timeout)
