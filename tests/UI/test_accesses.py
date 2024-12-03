import allure
import pytest

from pages.documentation_page import DocumentationPage
from pages.header_page import HeaderPage
from pages.projects_page import ProjectsPage
from pages.stub_page import StubPage
from resources.static_data import BASE_URL, ACCOUNT_ID, ACCOUNT_WITHOUT_ACCESS_ID, PROJECT_WITHOUT_ACCESS_ID


@allure.feature("Access_to_account")
@allure.epic("Clicking_on_links_in_the_application")
@pytest.mark.accesses
@pytest.mark.ui
def test_access_to_account_by_project_admin_403(external_password,
                                                projects_page: ProjectsPage,
                                                header_page: HeaderPage,
                                                stub_page: StubPage):
    '''тест проверяет доступ к аккаунту пользователя без доступа к этому аккаунту'''
    projects_page.change_role_to_('project_admin', external_password)
    projects_page.go_to_the_page(f'{BASE_URL}/accounts/{ACCOUNT_WITHOUT_ACCESS_ID}')
    projects_page.check_url(f'{BASE_URL}/accounts/{ACCOUNT_WITHOUT_ACCESS_ID}')

    header_page.check_head_icons()

    stub_page.check_stub_you_dont_have_access_to_account_without_button_write_to_admin()


@allure.feature("Access_to_project")
@allure.epic("Clicking_on_links_in_the_application")
@pytest.mark.accesses
@pytest.mark.ui
def test_access_to_project_by_user_403(external_password,
                                       header_page: HeaderPage,
                                       documentation_page: DocumentationPage,
                                       stub_page: StubPage):
    '''тест проверяет доступ к проекту пользователя без доступа к этому проекту'''
    documentation_page.change_role_to_('project_admin', external_password)
    documentation_page.go_to_the_page(f'{BASE_URL}/accounts/{ACCOUNT_ID}/projects/{PROJECT_WITHOUT_ACCESS_ID}')
    documentation_page.check_url(f'{BASE_URL}/accounts/{ACCOUNT_ID}/projects/{PROJECT_WITHOUT_ACCESS_ID}')

    header_page.check_head_icons()
    header_page.check_link_to_projects()

    stub_page.check_stub_you_dont_have_access_to_project_with_button_write_to_admin()
    stub_page.click_button_write_to_admin(force=True)
    stub_page.check_modal_write_to_admin()
