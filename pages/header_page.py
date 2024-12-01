import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class HeaderPage(BasePage):
    REL_URL = ''

    def __init__(self, page: Page):
        self.page = page

        self.tab_documentation: Locator = page.get_by_role("tab", name="Документация")
        self.tab_issues: Locator = page.get_by_role("tab", name="Замечания")
        self.tab_approvals: Locator = page.get_by_role("tab", name="Согласования", exact=True)
        self.tab_midp: Locator = page.get_by_role("tab", name="MIDP")
        self.tab_settings: Locator = page.get_by_role("tab", name="Настройки")
        self.tab_registry: Locator = page.get_by_role("tab", name="Реестр документов")
        self.tab_members: Locator = page.get_by_role("tab", name="Участники")

        self.link_to_projects: Locator = page.get_by_role("img", name="Main Logo")
 
        # self.icon_bell: Locator = page.locator("//*[@data-testid='BellOutline']")
        self.icon_bell: Locator = page.get_by_role("banner").get_by_test_id("BellOutline")
        self.icon_question: Locator = page.locator("//*[@data-testid='NotificationQuestionOutline']")
        

    @allure.step('Check head icons')
    def check_head_icons(self, timeout=60000):
        self.check_element_is_visible(self.icon_bell, timeout=timeout)
        self.check_element_is_visible(self.icon_question, timeout=timeout)


    @allure.step('Check link to projects')
    def check_link_to_projects(self, timeout=5000):
        self.check_element_is_visible(self.link_to_projects, timeout=timeout)


    @allure.step('Check head tabs of page with Settings tab')
    def check_head_tabs_with_settings(self, timeout=5000):
        self.check_element_is_visible(self.tab_documentation, timeout=timeout)
        self.check_element_is_visible(self.tab_issues, timeout=timeout)
        self.check_element_is_visible(self.tab_approvals, timeout=timeout)
        self.check_element_is_visible(self.tab_settings, timeout=timeout)
        self.check_element_is_visible(self.tab_registry, timeout=timeout)
        self.check_element_is_visible(self.tab_members, timeout=timeout)


    @allure.step('Check head tabs of page without Settings tab')
    def check_head_tabs_without_settings(self, timeout=30000):
        self.check_element_is_visible(self.tab_documentation, timeout=timeout)
        self.check_element_is_visible(self.tab_issues, timeout=timeout)
        self.check_element_is_visible(self.tab_approvals, timeout=timeout)
        self.check_element_is_not_visible(self.tab_settings)
        self.check_element_is_visible(self.tab_registry, timeout=timeout)
        self.check_element_is_visible(self.tab_members, timeout=timeout)
