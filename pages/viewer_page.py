import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class ViewerPage(BasePage):
    # REL_URL = f'accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}/documentation'

    def __init__(self, page: Page):
        self.page = page

        self.button_back: Locator = page.get_by_role("button", name="Назад")
        
        self.button_download_to_comp: Locator = page.get_by_role("button", name="Скачать на компьютер")

        # уменьшить масштаб
        # xpath //button[@title='По размеру страницы']/preceding-sibling::div[1]/button[1]
        # self.button_zoom_out: Locator = page.get_by_test_id('icon__SearchMinusOutline')
        self.button_zoom_out: Locator = page.locator('//button[@title="По размеру страницы"]/preceding-sibling::div[1]/button[1]')

        # %
        # xpath //button[@title='По размеру страницы']/preceding-sibling::div[1]/div
        self.scale_percents: Locator = page.locator('//button[@title="По размеру страницы"]/preceding-sibling::div[1]/div')

        # увеличить масштаб
        # xpath //button[@title='По размеру страницы']/preceding-sibling::div[1]/button[2]
        # self.button_zoom_in: Locator = page.get_by_test_id('icon__SearchPlusOutline')
        self.button_zoom_in: Locator = page.locator('//button[@title="По размеру страницы"]/preceding-sibling::div[1]/button[2]')

        self.button_by_page_size: Locator = page.get_by_role("button", name="По размеру страницы")
        self.button_turn: Locator = page.get_by_role("button", name="Повернуть")

        # иконка измерения
        self.button_measurements: Locator = page.get_by_test_id('measurementsToggleMode')
        self.button_measurements_open_menu: Locator = page.get_by_test_id('measurementsOpenMenu')

        # иконка сообщений
        self.button_comments: Locator = page.get_by_test_id('anotationsToggleMode')
        self.button_comments_open_menu: Locator = page.get_by_test_id('annotationsOpenMenu')

        self.pdf_viewer: Locator = page.locator("#widgetPDFViewer-container")

        self.button_add_comment: Locator = page.get_by_role("tooltip").get_by_test_id("button").first
        self.button_add_cloud_comment: Locator = page.get_by_role("tooltip").get_by_test_id("button").last

        self.button_issues: Locator = page.get_by_role("button", name="Замечания")


    @allure.step('Check viewer page elements')
    def check_viewer_page_elements(self, timeout=120000):
        self.check_element_is_visible(self.button_back, timeout=timeout)
        self.check_element_is_visible(self.button_download_to_comp, timeout=timeout)
        self.check_element_is_visible(self.button_zoom_out, timeout=timeout)
        self.check_element_is_visible(self.scale_percents, timeout=timeout)
        self.check_element_is_visible(self.button_zoom_in, timeout=timeout)
        self.check_element_is_visible(self.button_by_page_size, timeout=timeout)
        self.check_element_is_visible(self.button_turn, timeout=timeout)
        self.check_element_is_visible(self.button_issues, timeout=timeout)
        self.check_element_is_visible(self.pdf_viewer, timeout=timeout)
        self.check_element_is_visible(self.button_measurements, timeout=timeout)
        self.check_element_is_visible(self.button_measurements_open_menu, timeout=timeout)
        self.check_element_is_visible(self.button_comments, timeout=timeout)
        self.check_element_is_visible(self.button_comments_open_menu, timeout=timeout)


    @allure.step('Add comment')
    def add_comment(self, value='some_text', timeout=30000):
        self.click(self.button_comments_open_menu)
        self.click(self.button_add_comment)
        self.pdf_viewer.click(position={"x":100,"y":100})
        self.pdf_viewer.click(position={"x":300,"y":200})
        self.click(self.find("textarea"))
        self.input_value("textarea", value=value)
        self.page.locator("form").filter(has_text=value).get_by_test_id("button").click()


    @allure.step('Check comment')
    def check_comment_is_added(self, value='some_text', timeout=30000):
        comment = self.page.get_by_text(value)
        self.check_element_is_visible(comment, timeout=timeout)


    @allure.step('Click Zoom_out')
    def click_button_zoom_out(self):
        self.click(self.button_zoom_out)


    @allure.step('Click Zoom_in')
    def click_button_zoom_in(self):
        self.click(self.button_zoom_in)


    @allure.step('Click By_page_size')
    def click_button_by_page_size(self):
        self.click(self.button_by_page_size)


    @allure.step('Click Turn_button')
    def click_button_turn(self):
        self.click(self.button_turn)
        