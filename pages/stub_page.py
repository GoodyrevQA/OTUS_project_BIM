import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class StubPage(BasePage):
    
    def __init__(self, page: Page):
        self.page = page

        self.icon_lock: Locator = page.locator("//*[@data-testid='LockOutline']")

        # У вас нет доступа к аккаунту
        self.text_you_do_not_have_access_to_account: Locator = page.get_by_text("У вас нет доступа к аккаунту")
        # У вас нет доступа к проекту
        self.text_you_do_not_have_access_to_project: Locator = page.get_by_text("У вас нет доступа к проекту")
        # У вас нет доступа к папке
        self.text_you_do_not_have_access_to_folder: Locator = page.get_by_text("У вас нет доступа к папке")
        # У вас нет доступа к разделу Настройки
        self.text_you_do_not_have_access_to_section_settings: Locator = page.get_by_text("У вас нет доступа к разделу Настройки")
        # Нет доступных документов
        self.text_no_documents_available: Locator = page.get_by_text("Нет доступных документов")
        # Обратитесь к Администратору проекта для получения доступа
        self.text_contact_the_project_admin_to_get_access: Locator = page.get_by_text("Обратитесь к Администратору проекта для получения доступа")

        # Кнопка Написать Администратору
        self.button_write_to_admin: Locator = page.locator("//span[text()='Написать администратору']/ancestor::button")

        # Аватар аккаунта"
        self.text_account: Locator = page.get_by_text("Аккаунт", exact=True)

        # Модальное окно "Написать администратору"
        self.text_write_to_admin: Locator = page.locator("//div[@class='ant-modal-title' and text()='Написать администратору']")
        self.text_email_will_be_sent_to_the_admin: Locator = page.get_by_text("Письмо будет отправлено администратору на почту")
        self.text_to_whom: Locator = page.get_by_text("Кому")
        self.text_text: Locator = page.get_by_text("Текст")
        self.text_please_provide_access_to_the_project: Locator = page.get_by_text("Прошу предоставить доступ в проект")
        self.text_sender: Locator = page.get_by_text("Отправитель:")
        self.button_send: Locator = page.get_by_role("button", name="Отправить")
        self.icon_close: Locator = page.get_by_label("Close")


    @allure.step('click write to admin button"')
    def click_button_write_to_admin(self, force=False):
        self.click(self.button_write_to_admin, force=force)
 

    @allure.step('Проверка модального окна "Написать администратору"')
    def check_modal_write_to_admin(self, timeout=10000):
        self.check_element_is_visible(self.text_write_to_admin, timeout=timeout)
        self.check_element_is_visible(self.text_email_will_be_sent_to_the_admin, timeout=timeout)
        self.check_element_is_visible(self.text_to_whom, timeout=timeout)
        self.check_element_is_visible(self.text_text, timeout=timeout)
        self.check_element_is_visible(self.text_please_provide_access_to_the_project, timeout=timeout)
        self.check_element_is_visible(self.text_sender, timeout=timeout)
        self.check_element_is_visible(self.button_send, timeout=timeout)
        self.check_element_is_visible(self.icon_close, timeout=timeout)


    @allure.step('Проверка заглушки "У вас нет доступа к аккаунту" с кнопкой "Написать администратору"')
    def check_stub_you_dont_have_access_to_account_with_button_write_to_admin(self, timeout=60000):
        self.check_element_is_visible(self.icon_lock, timeout=timeout)
        self.check_element_is_visible(self.text_you_do_not_have_access_to_account, timeout=timeout)
        self.check_element_is_visible(self.text_contact_the_project_admin_to_get_access, timeout=timeout)
        self.check_element_is_visible(self.button_write_to_admin, timeout=timeout)
        

    @allure.step('Проверка заглушки "У вас нет доступа к аккаунту" без кнопки "Написать администратору"')
    def check_stub_you_dont_have_access_to_account_without_button_write_to_admin(self, timeout=60000):
        self.check_element_is_visible(self.icon_lock, timeout=timeout)
        self.check_element_is_visible(self.text_you_do_not_have_access_to_account, timeout=timeout)
        self.check_element_is_visible(self.text_contact_the_project_admin_to_get_access, timeout=timeout)
        self.check_element_is_not_visible(self.button_write_to_admin)


    @allure.step('Проверка заглушки "У вас нет доступа к проекту" с кнопкой "Написать администратору"')
    def check_stub_you_dont_have_access_to_project_with_button_write_to_admin(self, timeout=60000):
        self.check_element_is_visible(self.icon_lock, timeout=timeout)
        self.check_element_is_visible(self.text_you_do_not_have_access_to_project, timeout=timeout)
        self.check_element_is_visible(self.text_contact_the_project_admin_to_get_access, timeout=timeout)
        self.check_element_is_visible(self.button_write_to_admin, timeout=timeout)
        # self.check_element_has_css(self.button_write_to_admin, css_key='opacity', css_value='1')
        self.check_element_is_visible(self.text_account, timeout=timeout)
        self.page.wait_for_timeout(timeout=10000)


    @allure.step('Проверка заглушки "У вас нет доступа к проекту" без кнопки "Написать администратору"')
    def check_stub_you_dont_have_access_to_project_without_button_write_to_admin(self, timeout=60000):
        self.check_element_is_visible(self.icon_lock, timeout=timeout)
        self.check_element_is_visible(self.text_you_do_not_have_access_to_project, timeout=timeout)
        self.check_element_is_visible(self.text_contact_the_project_admin_to_get_access, timeout=timeout)
        self.check_element_is_not_visible(self.button_write_to_admin)
        self.check_element_is_visible(self.text_account, timeout=timeout)


    @allure.step('Проверка заглушки "У вас нет доступа к папке" с кнопкой "Написать администратору"')
    def check_stub_you_dont_have_access_to_folder_with_button_write_to_admin(self, timeout=60000):
        self.check_element_is_visible(self.icon_lock, timeout=timeout)
        self.check_element_is_visible(self.text_you_do_not_have_access_to_folder, timeout=timeout)
        self.check_element_is_visible(self.text_contact_the_project_admin_to_get_access, timeout=timeout)
        self.check_element_is_visible(self.button_write_to_admin, timeout=timeout)


    @allure.step('Проверка заглушки "У вас нет доступа к папке" без кнопки "Написать администратору"')
    def check_stub_you_dont_have_access_to_folder_without_button_write_to_admin(self, timeout=60000):
        self.check_element_is_visible(self.icon_lock, timeout=timeout)
        self.check_element_is_visible(self.text_you_do_not_have_access_to_folder, timeout=timeout)
        self.check_element_is_visible(self.text_contact_the_project_admin_to_get_access, timeout=timeout)
        self.check_element_is_not_visible(self.button_write_to_admin)


    @allure.step('Проверка заглушки "У вас нет доступа к разделу Настройки" с кнопкой "Написать администратору"')
    def check_stub_you_dont_have_access_to_section_settings_with_button_write_to_admin(self, timeout=60000):
        self.check_element_is_visible(self.icon_lock, timeout=timeout)
        self.check_element_is_visible(self.text_you_do_not_have_access_to_section_settings, timeout=timeout)
        self.check_element_is_visible(self.text_contact_the_project_admin_to_get_access, timeout=timeout)
        self.check_element_is_visible(self.button_write_to_admin, timeout=timeout)
        self.check_element_is_visible(self.text_account, timeout=timeout)


    @allure.step('Проверка заглушки "Нет доступных документов" с кнопкой "Написать администратору"')
    def check_stub_no_documents_available_with_button_write_to_admin(self, timeout=60000):
        self.check_element_is_visible(self.icon_lock, timeout=timeout)
        self.check_element_is_visible(self.text_no_documents_available, timeout=timeout)
        self.check_element_is_visible(self.text_contact_the_project_admin_to_get_access, timeout=timeout)
        self.check_element_is_visible(self.button_write_to_admin)
        self.check_element_is_visible(self.text_account, timeout=timeout)
        