import allure
from playwright.sync_api import Page, expect, Locator

import re
import logging

from resources.static_data import BASE_URL
from steps.support_steps import get_cookies


class BasePage:
    BASE_URL = BASE_URL
    REL_URL = ''
    LOGGER = logging.getLogger(__name__)
    LOGGER.setLevel(logging.DEBUG)


    def __init__(self, page: Page):
        self.page = page
        self.page.context.clear_cookies()
        # cookies = get_cookies(pssw)
        # self.page.context.add_cookies(cookies=cookies)


    @allure.step('Add cookies')
    def add_cookies(self, cookies):
        self.LOGGER.debug(f"{self.__class__.__name__}--Adding cookies\n")
        self.page.context.add_cookies(cookies=cookies)


    @allure.step('Change role to {role}')
    def change_role_to_(self, role, pssw=None):
        self.LOGGER.debug(f"{self.__class__.__name__}--Changing role to: {role}\n")
        self.clear_cookies()
        cookies = get_cookies(pssw)
        self.add_cookies(cookies=cookies)


    @allure.step('Check element {some_locator} is disabled')
    def check_element_is_disabled(self, some_locator: Locator, timeout=60000):
        self.LOGGER.debug(f"{self.__class__.__name__}--Checking element is disabled: {some_locator}\n")
        expect(some_locator).to_be_disabled(timeout=timeout)


    @allure.step('Check element {some_locator} is enabled')
    def check_element_is_enabled(self, some_locator: Locator, timeout=60000):
        self.LOGGER.debug(f"{self.__class__.__name__}--Checking element is enabled: {some_locator}\n")
        expect(some_locator).to_be_enabled(timeout=timeout)


    @allure.step('Check element {some_locator} is visible')
    def check_element_is_visible(self, some_locator: Locator, timeout=120000):
        self.LOGGER.debug(f"{self.__class__.__name__}--Checking element is visible: {some_locator}\n")
        expect(some_locator).to_be_visible(timeout=timeout)


    @allure.step('Check element {some_locator} is not visible')
    def check_element_is_not_visible(self, some_locator: Locator):
        self.LOGGER.debug(f"{self.__class__.__name__}--Checking element is not visible: {some_locator}\n")
        expect(some_locator).not_to_be_visible()


    @allure.step('Check element has CSS properties: {css_key}: {css_value}')
    def check_element_has_css(self, some_locator: Locator, css_key, css_value, timeout=60000):
        self.LOGGER.debug(f"{self.__class__.__name__}--Checking element {some_locator} has CSS properties: {css_key}:{css_value}\n")
        expect(some_locator).to_have_css(css_key, css_value, timeout=timeout)


    @allure.step('Check element {some_locator} has attribute {attribute_name} with value {attribute_value}')
    def check_element_has_attribute_with_value(self, some_locator: Locator, attribute_name, attribute_value, timeout=60000):
        self.LOGGER.debug(f"{self.__class__.__name__}--Checking element {some_locator} has CSS properties: \n")
        expect(some_locator).to_have_attribute(name=attribute_name, value=attribute_value, timeout=timeout)


    @allure.step('Check part of URL: {part_of_url}')
    def check_part_of_url(self, part_of_url, timeout=60000):
        self.LOGGER.debug(f"{self.__class__.__name__}--Checking part of URL: {part_of_url}\n")
        expect(self.page).to_have_url(re.compile(part_of_url), timeout=timeout)


    @allure.step('Check text on the page: {some_text}')
    def check_text_on_the_page(self, some_text, timeout=120000):
        self.LOGGER.debug(f"{self.__class__.__name__}--Checking text on the page: {some_text}\n")
        element_with_text = self.page.get_by_text(some_text).first
        expect(element_with_text).to_be_visible(timeout=timeout)


    @allure.step('Check text is not on the page: {some_text}')
    def check_text_is_not_on_the_page(self, some_text):
        self.LOGGER.debug(f"{self.__class__.__name__}--Checking text is not on the page: {some_text}\n")
        elements_with_text = self.page.get_by_text(some_text)
        # assert elements_with_text.count() == 0
        for el in elements_with_text.all():
            expect(el).not_to_be_visible()


    @allure.step('Check URL {some_url}')
    def check_url(self, some_url, timeout=60000):
        self.LOGGER.debug(f"{self.__class__.__name__}--Checking URL: {some_url}\n")
        expect(self.page).to_have_url(some_url, timeout=timeout)


    @allure.step('Clear cookies')
    def clear_cookies(self):
        self.LOGGER.debug(f"{self.__class__.__name__}--Clearing cookies\n")
        self.page.context.clear_cookies()


    @allure.step('Click {some_locator}')
    def click(self, some_locator: Locator, force=False) -> None:
        self.LOGGER.debug(f"{self.__class__.__name__}--Clicking: {some_locator}\n") 
        some_locator.click(force=force)


    @allure.step('Find element by locator: {locator}')
    def find(self, locator: Locator):
        self.LOGGER.debug(f"{self.__class__.__name__}--Finding element by locator: {locator}\n")
        return self.page.locator(locator)
    

    @allure.step('Find all elements by locator {locator}')
    def find_all_elements(self, locator: Locator):
        self.LOGGER.debug(f"{self.__class__.__name__}--Finding all elements: {locator}\n")
        return self.page.query_selector_all(locator)
    

    @allure.step('Find element by role {by_role_locator}')
    def find_by_role(self, by_role_locator):
        self.LOGGER.debug(f"{self.__class__.__name__}--Finding element by role: {by_role_locator}\n")
        return self.page.get_by_role(by_role_locator[0], name=by_role_locator[1])
    

    @allure.step('Go to the page {some_page}')
    def go_to_the_page(self, some_page, timeout=30000):
        self.LOGGER.debug(f"{self.__class__.__name__}--Going to the page: {some_page}\n")
        self.page.goto(some_page, wait_until='domcontentloaded', timeout=timeout)


    @allure.step('Get attribute {attribute_name} of element with locator {some_locator}')
    def get_attribute_of_element_by_locator(self, some_locator: Locator, attribute_name: str) -> str:
        self.LOGGER.debug(f"{self.__class__.__name__}--Taking value of attribute {attribute_name} for {some_locator}\n")
        return some_locator.get_attribute(attribute_name)


    @allure.step('Hover {some_locator}')
    def hover(self, some_locator: Locator) -> None:
        self.LOGGER.debug(f"{self.__class__.__name__}--Hovering: {some_locator}\n") 
        some_locator.hover()


    @allure.step('Input {value} into {some_locator}')
    def input_value(self, some_locator: Locator, value: str) -> None:
        self.LOGGER.debug(f"{self.__class__.__name__}--Inputing {value} into {some_locator}\n")
        self.page.locator(some_locator).type(value)


    @allure.step('Open the page')
    def open(self, timeout=30000):
        self.LOGGER.debug(f"{self.__class__.__name__}--Opening the page\n")
        self.page.goto(f'{self.BASE_URL}{self.REL_URL}', wait_until='domcontentloaded', timeout=timeout)
