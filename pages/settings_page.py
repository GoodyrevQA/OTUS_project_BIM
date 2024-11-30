import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage
from resources.static_data import ACCOUNT_ID, PROJECT_ID


class SettingsPage(BasePage):
    REL_URL = f'accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}/settings'

    def __init__(self, page: Page):
        self.page = page

        self.link_routing: Locator = page.get_by_role("link", name="Маршрутизация")
        self.link_issues: Locator = page.get_by_role("link", name="Замечания")
        self.link_locations: Locator = page.get_by_role("link", name="Расположения")
        self.link_extended_access: Locator = page.get_by_role("link", name="Расширенный доступ")
        self.link_midp: Locator = page.get_by_role("link", name="MIDP", exact=True)
        self.link_checking_the_file_name: Locator = page.get_by_role("link", name="Проверка имени файла")
        self.link_disciplines: Locator = page.get_by_role("link", name="Дисциплины")
        self.link_tags: Locator = page.get_by_role("link", name="Метки")
        self.link_bin: Locator = page.get_by_role("link", name="Корзина")


    @allure.step('Check settings page elements')
    def check_settings_page_elements(self, timeout=60000):
        self.check_element_is_visible(self.link_routing, timeout=timeout)
        self.check_element_is_visible(self.link_issues, timeout=timeout)
        self.check_element_is_visible(self.link_locations, timeout=timeout)
        self.check_element_is_visible(self.link_extended_access, timeout=timeout)
        self.check_element_is_visible(self.link_midp, timeout=timeout)
        self.check_element_is_visible(self.link_checking_the_file_name, timeout=timeout)
        self.check_element_is_visible(self.link_disciplines, timeout=timeout)
        self.check_element_is_visible(self.link_tags, timeout=timeout)
        self.check_element_is_visible(self.link_bin, timeout=timeout)
