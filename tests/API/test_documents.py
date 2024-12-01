import warnings
import pytest
import allure

from steps import assert_steps
from resources.static_data import APPROVED_EXTENSIONS
from steps.support_steps import post_documents

warnings.filterwarnings("ignore")


#################################################################
#                         POST /v2/documents                    #
#################################################################
# region
''' тест проверяет POST /v2/documents для всех разрешенных к загрузке расширений '''
@allure.feature("Documents")
@allure.epic("Post_documents")
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.documents
@pytest.mark.parametrize('ext', APPROVED_EXTENSIONS)
def test_post_documents(external_password, ext):
    ''' тест проверяет POST /v2/documents для всех разрешенных к загрузке расширений '''
    post_documents(external_password=external_password, file_extension=ext, check=True)


''' негативный тест. нельзя загрузить файл неразрешенного формата '''
@allure.feature("Documents")
@allure.epic("Post_documents")
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.documents
def test_400_post_documents(external_password, method='POST /v2/documents'):
    ''' негативный тест. нельзя загрузить файл неразрешенного формата '''
    response = post_documents(external_password=external_password, file_extension='random_format', check=False)
    assert_steps.assert_status_code(response=response, method=method, status_code=400)

# endregion