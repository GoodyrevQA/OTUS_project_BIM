import allure
import pytest

from pages.approvals_page import ApprovalsPage
from pages.documentation_page import DocumentationPage
from pages.header_page import HeaderPage
from pages.issues_page import IssuesPage
from pages.members_page import MembersPage
from pages.midp_page import MidpPage
from pages.registry_page import RegistryPage
from pages.settings_page import SettingsPage
from resources.static_data import BASE_URL, ACCOUNT_ID, PROJECT_ID


@allure.feature("Main_pages")
@allure.epic("Access_to_main_pages")
@pytest.mark.main_pages
def test_access_to_documentation_page(header_page: HeaderPage,
                                                       documentation_page: DocumentationPage,
                                                       external_password):
    '''тест проверяет доступ к экрану Документация Внешнего Администратор проекта'''
    documentation_page.change_role_to_('project_admin', pssw=external_password)
    documentation_page.go_to_the_page(f'{BASE_URL}/accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}')
    documentation_page.check_url(f'{BASE_URL}/{documentation_page.REL_URL}')
    documentation_page.check_documentation_page_elements()
    header_page.check_head_icons()
    header_page.check_link_to_projects()
    header_page.check_head_tabs_with_settings()


@allure.feature("Main_pages")
@allure.epic("Access_to_main_pages")
@pytest.mark.main_pages
def test_access_to_issues_page(header_page: HeaderPage,
                                                issues_page: IssuesPage,
                                                external_password):
    '''тест проверяет доступ к экрану Замечания Внешнего Администратор проекта'''
    issues_page.change_role_to_('external_project_admin', pssw=external_password)
    issues_page.go_to_the_page(f'{BASE_URL}/accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}/issues')
    issues_page.check_part_of_url(f'{BASE_URL}/{issues_page.REL_URL}')
    issues_page.check_issues_page_elements()
    header_page.check_head_icons()
    header_page.check_link_to_projects()
    header_page.check_head_tabs_with_settings()


@allure.feature("Main_pages")
@allure.epic("Access_to_main_pages")
@pytest.mark.main_pages
def test_access_to_approvals_page(header_page: HeaderPage,
                                                   approvals_page: ApprovalsPage,
                                                   external_password):
    '''тест проверяет доступ к экрану Согласования Внешнего Администратор проекта'''
    approvals_page.change_role_to_('external_project_admin', pssw=external_password)
    approvals_page.go_to_the_page(f'{BASE_URL}/accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}/approvals')
    approvals_page.check_part_of_url(f'{BASE_URL}/{approvals_page.REL_URL}')
    approvals_page.click(approvals_page.button_all)
    approvals_page.check_approvals_page_elements()
    header_page.check_head_icons()
    header_page.check_link_to_projects()
    header_page.check_head_tabs_with_settings()


@allure.feature("Main_pages")
@allure.epic("Access_to_main_pages")
@pytest.mark.main_pages
def test_access_to_settings_page(header_page: HeaderPage,
                                                  settings_page: SettingsPage,
                                                  external_password):
    '''тест проверяет доступ к экрану Настройки Внешнего Администратор проекта'''
    settings_page.change_role_to_('external_project_admin', pssw=external_password)
    settings_page.go_to_the_page(f'{BASE_URL}/accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}/settings')
    settings_page.check_part_of_url(f'{BASE_URL}/{settings_page.REL_URL}')
    settings_page.check_settings_page_elements()
    header_page.check_head_icons()
    header_page.check_link_to_projects()
    header_page.check_head_tabs_with_settings()


@allure.feature("Main_pages")
@allure.epic("Access_to_main_pages")
@pytest.mark.main_pages
def test_access_to_registry_page(header_page: HeaderPage,
                                                  registry_page: RegistryPage,
                                                  external_password):
    '''тест проверяет доступ к экрану Реестр документов Внешнего Администратор проекта'''
    registry_page.change_role_to_('external_project_admin', pssw=external_password)
    registry_page.go_to_the_page(f'{BASE_URL}/accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}/registry')
    registry_page.check_url(f'{BASE_URL}/{registry_page.REL_URL}')
    registry_page.check_registry_page_elements()
    header_page.check_head_icons()
    header_page.check_link_to_projects()
    header_page.check_head_tabs_with_settings()


@allure.feature("Main_pages")
@allure.epic("Access_to_main_pages")
@pytest.mark.main_pages
def test_access_to_members_page(header_page: HeaderPage,
                                                 members_page: MembersPage,
                                                 external_password):
    '''тест проверяет доступ к экрану Участники Внешнего Администратор проекта'''
    members_page.change_role_to_('external_project_admin', pssw=external_password)
    members_page.go_to_the_page(f'{BASE_URL}/accounts/{ACCOUNT_ID}/projects/{PROJECT_ID}/members')
    members_page.check_url(f'{BASE_URL}/{members_page.REL_URL}')
    members_page.check_members_page_elements_with_add_buttons()
    header_page.check_head_icons()
    header_page.check_link_to_projects()
    header_page.check_head_tabs_with_settings()
    