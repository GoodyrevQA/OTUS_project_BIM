import warnings
import allure
import pytest

from resources import urls
from steps import support_steps, assert_steps
from steps.support_steps import get_folders, get_folder, post_folders

from steps.start_session import *


warnings.filterwarnings("ignore")


#################################################################
#                        GET /v2/folders                        #
#################################################################
# region
''' тест проверяет GET /v2/folders '''
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.folders
def test_get_folders(external_password):
    ''' тест проверяет GET /v2/folders '''
    get_folders(check=True, external_password=external_password)





#################################################################
#                   GET /v2/folders/{folderId}                  #
#################################################################
# region
''' тест проверяет GET /v2/folders/{folderId}  '''
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.folders
def test_get_folder(external_password):
    ''' тест проверяет GET /v2/folders/{folderId}  '''
    some_folder_id = post_folders(external_password=external_password).json()
    get_folder(external_password=external_password, folder_id=some_folder_id, check=True)





#################################################################
#                       POST /v2/folders                        #
#################################################################
# region
''' тест проверяет POST /v2/folders с граничным значением длины имени '''
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.folders
def test_post_folders(external_password):
    ''' тест проверяет POST /v2/folders с граничным значением длины имени '''
    string_255 = support_steps.generate_random_string(255)
    post_folders(folder_name=string_255, external_password=external_password, check=True)




# ''' Негативный тест. методом POST /v2/folders нельзя создать больше 10 уровней вложенности '''
# @pytest.mark.regress
# @pytest.mark.folders
# def test_post_400_folders_11th_level():
#     ''' Негативный тест. методом POST /v2/folders нельзя создать больше 10 уровней вложенности '''
#     with allure.step("создаем 10 уровней вложенности папок методом POST /v2/folders"):
#         parent_folder_id = post_and_test_folders().json()
#         for _ in range(9):
#             parent_folder_id = post_and_test_folders(parent_id=parent_folder_id).json()

#     with allure.step("пытаемся создать папку на 11-м уровне вложенности методом POST /v2/folders, проверяем статус код ответа 400"):
#         response = post_folders(parent_id=parent_folder_id)
#         assert response.status_code == 400, "статус код ответа метода POST /v2/folders для папки на 11-м уровне вложенности != 400"


# ''' Негативный тест POST /v2/folders. Нельзя создать папку с именем "Корзина" '''
# @pytest.mark.regress
# @pytest.mark.folders
# def test_post_400_folders_folder_is_named_BIN():
#     ''' Негативный тест POST /v2/folders. Нельзя создать папку с именем "Корзина" '''
#     with allure.step("пытаемся создать папку с именем Корзина, проверяем статус код ответа 400"):
#         response = post_folders(folder_name="КОРЗИНА")
#         assert response.status_code == 400, "status code != 400"
#         response = post_folders(folder_name="корзина")
#         assert response.status_code == 400, "status code != 400"
#         response = post_folders(folder_name="кОрЗиНа")
#         assert response.status_code == 400, "status code != 400"


# ''' Негативный тест POST /v2/folders. Не передано имя папки '''
# @pytest.mark.regress
# @pytest.mark.folders
# def test_post_400_folders_name_is_empty():
#     ''' Негативный тест POST /v2/folders. Не передано имя папки '''
#     with allure.step("выполняем POST /v2/folders с пустой строкой в поле name, проверяем статус код ответа 400"):
#         response = post_folders(folder_name="")
#         assert response.status_code == 400, f'''status code ответа метода POST /v2/folders без передачи имени папки != 400.
#                                                     текст ответа: {response.text}'''


# ''' Негативный тест POST /v2/folders. Имя папки > 255 символов '''
# @pytest.mark.regress
# @pytest.mark.folders
# def test_post_400_folders_name_is_long():
#     ''' Негативный тест POST /v2/folders. Имя папки > 255 символов '''
#     with allure.step("выполняем POST /v2/folders в поле name передаем строку длиной 256 символов, проверяем статус код ответа 400"):
#         string_256 = support_steps.generate_random_string(256)
#         response = post_folders(folder_name=string_256)
#         assert response.status_code == 400, f'''status code ответа метода POST /v2/folders с длиной имени папки 256 символов != 400.
#                                                 текст ответа: {response.text}'''


# ''' Негативный тест POST /v2/folders. Папка с этим именем уже существует в родительской папке '''
# @pytest.mark.regress
# @pytest.mark.folders
# def test_post_400_folders_reply_name():
#     ''' Негативный тест POST /v2/folders. Папка с этим именем уже существует в родительской папке '''
#     with allure.step("выполняем POST /v2/folders в поле name передаем имя папки, которое уже существует в родительской папке, проверяем статус код ответа 400"):
#         some_name = f'folder_{support_steps.generate_datetime_long()}'
#         post_and_test_folders(folder_name=some_name)
#         response = post_folders(folder_name=some_name)
#         assert response.status_code == 400, f'''status code ответа метода POST /v2/folders с именем папки,
#         которое уже существует в родительской папке != 400. текст ответа: {response.text}'''


# ''' Негативный тест POST /v2/folders. Невалидный id родительской папки '''
# @pytest.mark.regress
# @pytest.mark.folders
# def test_post_400_folders_invalid_parentId():
#     ''' Негативный тест POST /v2/folders. Невалидный id родительской папки '''
#     with allure.step("выполняем POST /v2/folders в поле parentId передаем невалидный id, проверяем статус код ответа 400"):
#         invalid_id = support_steps.generate_invalid_uuid()
#         response = post_folders(parent_id=invalid_id)
#         assert response.status_code == 400, f'''status code ответа метода POST /v2/folders с невалидным id
#         родительской папки != 400. текст ответа: {response.text}'''


# ''' Негативный тест POST /v2/folders. Несуществующий id родительской папки '''
# @pytest.mark.regress
# @pytest.mark.folders
# def test_post_404_folders_nonexistent_parentId():
#     ''' Негативный тест POST /v2/folders. Несуществующий id родительской папки '''
#     with allure.step("выполняем POST /v2/folders в поле parentId передаем несуществующий id, проверяем статус код ответа 400"):
#         nonexistent_id = support_steps.generate_valid_uuid()
#         response = post_folders(parent_id=nonexistent_id)
#         assert response.status_code == 404, f'''status code ответа метода POST /v2/folders с несуществующим id
#         родительской папки != 404. текст ответа: {response.text}'''


# ''' Негативный тест POST /v2/folders. Несуществующий id проекта '''
# @pytest.mark.regress
# @pytest.mark.folders
# def test_post_404_folders_nonexistent_projecttId():
#     ''' Негативный тест POST /v2/folders. Несуществующий id проекта '''
#     with allure.step("выполняем POST /v2/folders в поле projecttId передаем несуществующий id, проверяем статус код ответа 400"):
#         nonexistent_id = support_steps.generate_valid_uuid()
#         response = post_folders(project_id=nonexistent_id)
#         assert response.status_code == 404, f'''status code ответа метода POST /v2/folders с несуществующим id
#         проекта != 404. текст ответа: {response.text}'''


# # endregion


# #################################################################
# #                       PUT /v2/folders                        #
# #################################################################
# # region
# ''' тест проверяет PUT /v2/folders с граничным значением длины имени '''
# @pytest.mark.smoke
# @pytest.mark.regress
# @pytest.mark.folders
# def test_put_200_folders():
#     ''' тест проверяет PUT /v2/folders с граничным значением длины имени '''
#     string_255 = support_steps.generate_random_string(255)
#     put_and_test_folders(new_folder_name=string_255)




# ''' негативный тест PUT /v2/folders. Не передано новое имя папки '''
# @pytest.mark.regress
# @pytest.mark.folders
# def test_put_400_folders_name_is_empty():
#     ''' негативный тест PUT /v2/folders. Не передано новое имя папки '''
#     with allure.step("выполняем PUT /v2/folders с пустой строкой в поле name, проверяем статус код ответа 400"):
#         response = put_folders(new_folder_name="")
#         assert response.status_code == 400, f'''status code ответа метода PUT /v2/folders без передачи имени папки != 400.
#                                                     текст ответа: {response.text}'''


# ''' негативный тест PUT /v2/folders. Передано новое имя папки длиной > 255 символов '''
# @pytest.mark.regress
# @pytest.mark.folders
# def test_put_400_folders_name_is_long():
#     ''' негативный тест PUT /v2/folders. Передано новое имя папки длиной > 255 символов '''
#     with allure.step("выполняем PUT /v2/folders, передаем имя папки длиной 256 символов, проверяем статус код ответа 400"):
#         string_256 = support_steps.generate_random_string(256)
#         response = put_folders(new_folder_name=string_256)
#         assert response.status_code == 400, f'''status code ответа метода PUT /v2/folders с именем папки длиной 256 символов != 400.
#                                                     текст ответа: {response.text}'''


# ''' негативный тест PUT /v2/folders. Передано новое имя папки 'Корзина' '''
# @pytest.mark.regress
# @pytest.mark.folders
# def test_put_400_folders_folder_is_named_BIN():
#     ''' негативный тест PUT /v2/folders. Передано новое имя папки 'Корзина' '''
#     with allure.step("выполняем PUT /v2/folders, передаем имя папки 'Корзина', проверяем статус код ответа 400"):
#         response = put_folders(new_folder_name='Корзина')
#         assert response.status_code == 400, f'''status code ответа метода PUT /v2/folders с именем папки 'Корзина' != 400.
#                                                     текст ответа: {response.text}'''


# ''' Негативный тест PUT /v2/folders. Папка с этим именем уже существует в родительской папке '''
# @pytest.mark.regress
# @pytest.mark.folders
# def test_put_400_folders_reply_name():
#     ''' Негативный тест PUT /v2/folders. Папка с этим именем уже существует в родительской папке '''
#     with allure.step("выполняем PUT /v2/folders в поле name передаем имя папки, которое уже существует в родительской папке, проверяем статус код ответа 400"):
#         some_name = f'folder_{support_steps.generate_datetime_long()}'
#         post_and_test_folders(folder_name=some_name)
#         response = put_folders(new_folder_name=some_name)
#         assert response.status_code == 400, f'''status code ответа метода PUT /v2/folders с именем папки,
#         которое уже существует в родительской папке != 400. текст ответа: {response.text}'''



# #################################################################
# #                       DELETE /v2/folders                      #
# #################################################################
# # region
# ''' тест проверяет DELETE /v2/folders '''
# @pytest.mark.smoke
# @pytest.mark.regress
# @pytest.mark.folders
# def test_delete_200_folders():
#     ''' тест проверяет DELETE /v2/folders '''
#     delete_and_test_folders()


# ''' тест проверяет DELETE /v2/folders для папки с файлом '''
# @pytest.mark.regress
# @pytest.mark.folders
# def test_delete_200_folders_with_files():
#     ''' тест проверяет DELETE /v2/folders для папки с файлом '''
#     with allure.step("создаем папку, получаем ее id"):
#         folder_id = post_and_test_folders().json()

#     with allure.step("загружаем файл в созданную папку"):
#         post_and_test_documents(folder_id=folder_id)

#     with allure.step("удаляем папку с файлом"):
#         delete_and_test_folders(folder_ids=[folder_id])





