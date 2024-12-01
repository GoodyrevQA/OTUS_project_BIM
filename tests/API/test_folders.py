import warnings
import allure
import pytest

from steps import support_steps, assert_steps
from steps.support_steps import get_folders, get_folder, post_folders
from steps.start_session import *

warnings.filterwarnings("ignore")


#################################################################
#                        GET /v2/folders                        #
#################################################################
# region
''' тест проверяет GET /v2/folders '''
@allure.feature("Folders")
@allure.epic("Get_documents")
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.folders
def test_get_folders(external_password):
    ''' тест проверяет GET /v2/folders '''
    get_folders(check=True, external_password=external_password)

# endregion


#################################################################
#                   GET /v2/folders/{folderId}                  #
#################################################################
# region
''' тест проверяет GET /v2/folders/{folderId}  '''
@allure.feature("Folders")
@allure.epic("Get_documents")
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.folders
def test_get_folder(external_password):
    ''' тест проверяет GET /v2/folders/{folderId}  '''
    some_folder_id = post_folders(external_password=external_password).json()
    get_folder(external_password=external_password, folder_id=some_folder_id, check=True)

# endregion


#################################################################
#                       POST /v2/folders                        #
#################################################################
# region
''' тест проверяет POST /v2/folders с граничными значениями длины имени '''
@allure.feature("Folders")
@allure.epic("Post_documents")
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.folders
@pytest.mark.parametrize('ln', (1, 255))
def test_post_folders(external_password, ln):
    ''' тест проверяет POST /v2/folders с граничными значениями длины имени '''
    folder_name = support_steps.generate_random_string(ln)
    folder_id = post_folders(folder_name=folder_name,
                             parent_id=None,
                             external_password=external_password,
                             check=True).json()

    with allure.step('выполняем GET /v2/folders/id, проверяем, что папка создана с переданным именем'):
        folder = get_folder(external_password=external_password, folder_id=folder_id).json()
        assert folder['name'] == folder_name
        assert folder['parentId'] is None


''' негативный тест. нельзя создать папку длиной 0 или более 255 символов '''
@pytest.mark.regress
@pytest.mark.folders
@allure.feature("Folders")
@allure.epic("Post_documents")
@pytest.mark.parametrize('ln', (0, 256))
def test_400_post_folders(external_password, ln, method='POST /v2/folders'):
    ''' негативный тест. нельзя создать папку длиной 0 или более 255 символов '''
    folder_name = support_steps.generate_random_string(ln)
    response = post_folders(folder_name=folder_name, external_password=external_password, check=False)
    assert_steps.assert_status_code(response=response, method=method, status_code=400)


''' Негативный тест. методом POST /v2/folders нельзя создать больше 10 уровней вложенности '''
@pytest.mark.regress
@pytest.mark.folders
@allure.feature("Folders")
@allure.epic("Post_documents")
def test_post_400_folders_11th_level(external_password, method='POST /v2/folders'):
    ''' Негативный тест. методом POST /v2/folders нельзя создать больше 10 уровней вложенности '''
    with allure.step(f"создаем 10 уровней вложенности папок методом {method}"):
        parent_folder_id = post_folders(external_password=external_password).json()
        for _ in range(9):
            parent_folder_id = post_folders(parent_id=parent_folder_id, external_password=external_password).json()

    with allure.step(f"пытаемся создать папку на 11-м уровне вложенности методом {method}, проверяем статус код ответа 400"):
        response = post_folders(parent_id=parent_folder_id, external_password=external_password, check=False)
        assert_steps.assert_status_code(response=response, method=method, status_code=400)
        

''' Негативный тест POST /v2/folders. Нельзя создать папку с именем "Корзина" независимо от регистра '''
@pytest.mark.regress
@pytest.mark.folders
@allure.feature("Folders")
@allure.epic("Post_documents")
@pytest.mark.parametrize('folder_name', ('корзина', 'КОРЗИНА', 'Корзина'))
def test_post_400_folders_folder_is_named_BIN(external_password, folder_name, method='POST /v2/folders'):
    ''' Негативный тест POST /v2/folders. Нельзя создать папку с именем "Корзина" независимо от регистра '''
    with allure.step("пытаемся создать папку с именем Корзина, проверяем статус код ответа 400"):
        response = post_folders(folder_name=folder_name, external_password=external_password, check=False)
        assert_steps.assert_status_code(response=response, method=method, status_code=400)
        

''' Негативный тест POST /v2/folders. Папка с этим именем уже существует в родительской папке '''
@pytest.mark.regress
@pytest.mark.folders
@allure.feature("Folders")
@allure.epic("Post_documents")
def test_post_400_folders_reply_name(external_password, method='POST /v2/folders'):
    ''' Негативный тест POST /v2/folders. Папка с этим именем уже существует в родительской папке '''
    with allure.step(f"выполняем {method} в поле name передаем имя папки, которое уже существует в родительской папке, проверяем статус код ответа 400"):
        some_name = f'folder_{support_steps.generate_datetime_long()}'
        post_folders(folder_name=some_name, external_password=external_password, check=True)

        response = post_folders(folder_name=some_name, external_password=external_password, check=False)
        assert_steps.assert_status_code(response=response, method=method, status_code=400)


''' Негативный тест POST /v2/folders. Невалидный id родительской папки '''
@pytest.mark.regress
@pytest.mark.folders
@allure.feature("Folders")
@allure.epic("Post_documents")
def test_post_400_folders_invalid_parentId(external_password, method='POST /v2/folders'):
    ''' Негативный тест POST /v2/folders. Невалидный id родительской папки '''
    with allure.step(f"выполняем {method} в поле parentId передаем невалидный id, проверяем статус код ответа 400"):
        invalid_id = support_steps.generate_invalid_uuid()
        response = post_folders(parent_id=invalid_id, external_password=external_password, check=False)
        assert_steps.assert_status_code(response=response, method=method, status_code=400)


''' Негативный тест POST /v2/folders. Несуществующий id родительской папки '''
@pytest.mark.regress
@pytest.mark.folders
@allure.feature("Folders")
@allure.epic("Post_documents")
def test_post_404_folders_nonexistent_parentId(external_password, method='POST /v2/folders'):
    ''' Негативный тест POST /v2/folders. Несуществующий id родительской папки '''
    with allure.step(f"выполняем {method} в поле parentId передаем несуществующий id, проверяем статус код ответа 400"):
        nonexistent_id = support_steps.generate_valid_uuid()
        response = post_folders(parent_id=nonexistent_id, external_password=external_password, check=False)
        assert_steps.assert_status_code(response=response, method=method, status_code=404)

# endregion
