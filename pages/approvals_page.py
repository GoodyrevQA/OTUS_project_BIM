import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage
from resources.static_data import ACCOUNT_ID, PROJECT_ID


class ApprovalsPage(BasePage):
    REL_URL = f'accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}/approvals'

    def __init__(self, page: Page):
        self.page = page

        # иконка Фильтры и все, что справа от нее
        self.button_filters: Locator = page.locator("//*[@data-testid='icon__setting_slider']")
        self.button_active: Locator = page.get_by_role("button", name="Активные")
        self.button_archived: Locator = page.get_by_role("button", name="Архивные")
        self.button_assigned_to_me: Locator = page.get_by_role("button", name="Назначенные мне")
        self.button_all: Locator = page.get_by_role("button", name="Все")
        self.field_search: Locator = page.get_by_placeholder("Название файла, маршрут или этап согласования, согласующие")
        self.icon_search: Locator = page.locator("//*[@data-testid='SearchOutline']")

        # поля в Фильтрах
        self.field_choose_route: Locator = page.locator("//*[text()='Выберите маршрут']")
        self.field_choose_stage: Locator = page.locator("//*[text()='Выберите этап']")
        self.field_choose_folders: Locator = page.locator("//*[text()='Выберите папки']")
        self.text_bin: Locator = page.locator("//*[text()='Корзина']")
        self.text_period_up_to: Locator = page.locator("//label[text()='Срок до']")
        self.field_choose_approver: Locator = page.locator("//*[text()='Выберите согласующего']")
        self.field_choose_decision: Locator = page.locator("//*[text()='Выберите решение']")
        self.button_clear: Locator = page.locator("//*[text()='Очистить']")

        # шапка таблицы
        self.column_file_name: Locator = page.locator("//span[text()='Имя файла']")
        self.column_status: Locator = page.locator("//span[text()='Статус']")
        self.column_route: Locator = page.locator("//span[text()='Маршрут']")
        self.column_stage: Locator = page.locator("//span[text()='Этап']")
        self.column_related_folders: Locator = page.locator("//th[text()='Связанные папки']")
        self.column_period_up_to: Locator = page.locator("//span[text()='Срок до']")
        self.column_approvers: Locator = page.locator("//th[text()='Согласующие']")
        self.column_decision: Locator = page.locator("//span[text()='Решение']")
        self.column_delegation: Locator = page.locator("//th[text()='Делегирование']")
        self.column_version: Locator = page.locator("//span[text()='Версия']")
        

    @allure.step('Check approvals page elements')
    def check_approvals_page_elements(self, timeout=60000):
        self.check_element_is_visible(self.button_filters, timeout=timeout)
        self.check_element_is_visible(self.button_active, timeout=timeout)
        self.check_element_is_visible(self.button_archived, timeout=timeout)
        self.check_element_is_visible(self.button_assigned_to_me, timeout=timeout)
        self.check_element_is_visible(self.button_all, timeout=timeout)
        self.check_element_is_visible(self.field_search, timeout=timeout)
        self.check_element_is_visible(self.icon_search, timeout=timeout)

        self.check_element_is_visible(self.field_choose_route, timeout=timeout)
        self.check_element_is_visible(self.field_choose_stage, timeout=timeout)
        self.check_element_is_visible(self.field_choose_folders, timeout=timeout)
        self.check_element_is_visible(self.text_bin, timeout=timeout)
        self.check_element_is_visible(self.text_period_up_to, timeout=timeout)
        self.check_element_is_visible(self.field_choose_approver, timeout=timeout)
        self.check_element_is_visible(self.field_choose_decision, timeout=timeout)

        self.check_element_is_visible(self.column_file_name, timeout=timeout)
        self.check_element_is_visible(self.column_status, timeout=timeout)
        self.check_element_is_visible(self.column_route, timeout=timeout)
        self.check_element_is_visible(self.column_stage, timeout=timeout)
        self.check_element_is_visible(self.column_related_folders, timeout=timeout)
        self.check_element_is_visible(self.column_period_up_to, timeout=timeout)
        self.check_element_is_visible(self.column_approvers, timeout=timeout)
        self.check_element_is_visible(self.column_decision, timeout=timeout)
        self.check_element_is_visible(self.column_delegation, timeout=timeout)
        self.check_element_is_visible(self.column_version, timeout=timeout)
