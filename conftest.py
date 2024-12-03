import pytest
import allure
from playwright.sync_api import Page, BrowserContext

from pages.accounts_page import AccountsPage
from pages.approvals_page import ApprovalsPage
from pages.base_page import BasePage
from pages.documentation_page import DocumentationPage
from pages.header_page import HeaderPage
from pages.issues_page import IssuesPage
from pages.members_page import MembersPage
from pages.projects_page import ProjectsPage
from pages.registry_page import RegistryPage
from pages.settings_page import SettingsPage
from pages.stub_page import StubPage
from pages.viewer_page import ViewerPage


# для корректного отображения кириллицы в параметризаторах
def pytest_make_parametrize_id(val):
    return repr(val)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request):
    # Проверяем, помечен ли тест как 'ui'
    if 'ui' not in request.keywords:
        yield
        return

    # Получаем фикстуру 'page' только для UI тестов
    page = request.getfixturevalue("page")
    yield
    # Проверяем, упал ли тест
    if hasattr(request.node, "rep_call") and not request.node.rep_call.passed:
        allure.attach(
            page.screenshot(full_page=True),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )


def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--external-password",
                     action="store",
                     default="pandom_password",
                     help="Password for authentication external_user")


@pytest.fixture
def external_password(request: pytest.FixtureRequest):
    return request.config.getoption("--external-password")


@pytest.fixture()
def page(context: BrowserContext, request):
    if "ui" in request.keywords:
        context_with_https_ignore = context.browser.new_context(ignore_https_errors=True)
        page: Page = context_with_https_ignore.new_page()
        page.set_viewport_size({'width': 1920, 'height': 1080})
        yield page
        page.close()  # Закрываем страницу после завершения теста
        context_with_https_ignore.close()  # Закрываем контекст
    else:
        yield None


@pytest.fixture()
def base_page(page: Page) -> BasePage:
    return BasePage(page)

@pytest.fixture()
def accounts_page(page: Page) -> AccountsPage:
    return AccountsPage(page)

@pytest.fixture()
def approvals_page(page: Page) -> ApprovalsPage:
    return ApprovalsPage(page)

@pytest.fixture()
def documentation_page(page: Page) -> DocumentationPage:
    return DocumentationPage(page)

@pytest.fixture()
def header_page(page: Page) -> HeaderPage:
    return HeaderPage(page)

@pytest.fixture()
def issues_page(page: Page) -> IssuesPage:
    return IssuesPage(page)

@pytest.fixture()
def members_page(page: Page) -> MembersPage:
    return MembersPage(page)

@pytest.fixture()
def projects_page(page: Page) -> ProjectsPage:
    return ProjectsPage(page)

@pytest.fixture()
def registry_page(page: Page) -> RegistryPage:
    return RegistryPage(page)

@pytest.fixture()
def settings_page(page: Page) -> SettingsPage:
    return SettingsPage(page)

@pytest.fixture()
def stub_page(page: Page) -> StubPage:
    return StubPage(page)

@pytest.fixture()
def viewer_page(page: Page) -> ViewerPage:
    return ViewerPage(page)
