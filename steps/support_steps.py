from PIL import Image, ImageDraw, ImageFont
import allure
import requests

import base64
import datetime
import os
import random
import string
import time
import uuid
import warnings

from resources import static_data
from resources.schemas.schema_folders import valid_folder, valid_folders
from resources.schemas.schema_documents import valid_document
from steps.start_session import *
from steps.assert_steps import *

warnings.filterwarnings("ignore")


project_admin_session = requests.Session()
project_admin_session.headers.update({'User-Agent': 'Python_autotests'})
project_admin_session.verify = False


'''функция возвращает строку в даты 2023-06-26'''
def generate_date():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d')

'''функция возвращает строку в формате 2023-06-26T19:10:18'''
def generate_datetime():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%dT%H:%M:%S')

'''функция возвращает строку в формате 2023-06-26T19-10-18'''
def generate_datetime_for_file_name():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%dT%H-%M-%S')

'''функция возвращает строку в формате 2023-06-26T19-10-18.111111'''
def generate_datetime_for_file_name_long():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%dT%H-%M-%S.%f')

'''функция количество дней и возвращает дату = сегодня + переданные дни в формате 2023-06-26T19:10:18'''
def generate_future_datetime(d):
    now = datetime.datetime.now()
    future = now + datetime.timedelta(days=int(d))
    return future.strftime('%Y-%m-%dT%H:%M:%S')

'''функция возвращает строку в формате 2023-06-26T19:10:18.111111'''
def generate_datetime_long():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%dT%H:%M:%S.%f')

'''функция возвращает валидный uuid'''
def generate_valid_uuid():
    return str(uuid.uuid4())

'''функция возвращает невалидный uuid'''
def generate_invalid_uuid():
    x = uuid.uuid4()
    return 'Ы' + str(x)[1:]

'''функция принимает длину строки и возвращает случайную строку заданной длины'''
def generate_random_string(length):
    characters = string.ascii_lowercase + string.digits
    x = ''.join(random.choice(characters) for _ in range(length))
    return x

'''функция принимает число и возвращает случайное число от start=1 до этого числа'''
def generate_random_number(num, start=1):
    return random.randint(start, num)

def encode_to_base64(input_string):
    # Преобразуем строку в байты
    byte_string = input_string.encode('utf-8')
    # Кодируем байты в base64
    base64_bytes = base64.b64encode(byte_string)
    # Преобразуем закодированные байты обратно в строку
    base64_string = base64_bytes.decode('utf-8')
    return base64_string


#################################################################
#                          get_cookies                          #
#################################################################
# region
'''функция выполняет запрос с помощью библиотеки requests, и возвращает список cookies в требуемом playwright формате'''
def get_cookies(pssw, ui_url=static_data.BASE_URL) -> list:

    response_me = project_admin_session.get(url=f'{urls.url_base}/v2/users/me', verify=False)
    if response_me.status_code in (400, 401):
        project_admin_session.cookies.clear()

        password_in_base64 = encode_to_base64(pssw)
        json_data = {"email": "iegudyrev@yandex.ru","password": password_in_base64}
        response_login = project_admin_session.post(url=urls.url_login, json=json_data, verify=False)

        ck = response_login.json()["confirmationKey"]
        json_data = {"code": "777777","confirmationKey": ck}
        response_confirm = project_admin_session.post(url=urls.url_confirm, json=json_data)

        response_me = project_admin_session.get(url=f'{urls.url_base}/v2/users/me', verify=False)
        if response_me.status_code != 200:
            raise Exception('something wrong with user authorization')

    cookie = response_me.request.headers.get('Cookie', None)
    cookie_name, cookie_value = cookie.split('=')
    list_of_cookies = [{"name": cookie_name, "value": cookie_value, "url": ui_url}]

    return list_of_cookies

# endregion



#################################################################
#                     create_rectangle_image                    #
#################################################################
# region
'''функция создает изображение JPG'''
def create_rectangle_image(only_name='output', width=512, height=256, indent=12, canvas_color=None, big_title='OTUS'):
    '''функция создает изображение JPG'''
    # Создаём пустое изображение заданного цвета
    if canvas_color is None:
        canvas_color = (255, 255, 245)
    image = Image.new('RGB', (width, height), canvas_color)
    draw = ImageDraw.Draw(image)
 
    # Настройки шрифта
    font = ImageFont.load_default(size=18)
    font_2 = ImageFont.load_default(size=180)

    # Позиция текста
    bbox = draw.textbbox((0, 0), only_name, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    text_x = int((width - text_width) / 2)
    text_y = (height - text_height) // 5.5

    bbox2 = draw.textbbox((0, 0), big_title, font=font_2)
    text_width2, text_height2 = bbox2[2] - bbox2[0], bbox2[3] - bbox2[1]
    text_x2 = int((width - text_width2) / 2)
    text_y2 = (height - text_height2) // 3.8
 
    # Добавляем текст на изображение
    draw.text((text_x, text_y), only_name, fill="black", font=font)
    x, y, z = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    x2, y2, z2 = abs(255 - x), abs(255 - y), abs(255 - z)
    draw.text((text_x2, text_y2), big_title, fill=(x, y, z), font=font_2)

    # Рисуем квадрат
    square_x0 = square_y0 = indent
    square_x1 = width - indent
    square_y1 = height - indent
    draw.rectangle([square_x0, square_y0, square_x1, square_y1], outline=(x2, y2, z2), width=5)

    # Сохраняем изображение
    image.save(f'{only_name}.jpg')

# endregion

#################################################################
#                      create_binary_file                       #
#################################################################
# region
'''функция создает бинарный документ'''
def create_binary_file(only_name=None, file_extension='txt', line_to_fill='random', n=None):

    with allure.step("создаем имя файла с переданным в функцию расширением"):
        if only_name is None:
            only_name = f'file_{generate_datetime_for_file_name()}'
        file_name = f'{only_name}.{file_extension}'

    with allure.step("задаем количество строк в файле"):
        if n is None:
            n = generate_random_number(100)

    with allure.step("создаем бинарный файл"):
        with open(file_name, 'wb') as my_file:
            f_str = f'''{generate_datetime_long()} {line_to_fill}\n''' * n
            my_file.write(f_str.encode('utf-8'))

# endregion



#################################################################
#                       POST /v2/folders                        #
#################################################################
# region
''' функция выполняет метод POST /v2/folders, проверяет и возвращает ответ '''
def post_folders(external_password, project_id=None, folder_name=None, parent_id=None,
                 url=urls.url_folders, method='POST /v2/folders', role='project_admin', check=True):
    ''' функция выполняет метод POST /v2/folders, проверяет и возвращает ответ '''
    start_session(pssw=external_password)

    if project_id is None:
        project_id = static_data.PROJECT_ID

    if folder_name is None:
        folder_name = f'folder_{generate_datetime_long()}'

    with allure.step(f"подготавливаем пэйлоад {method} для создания папки"):
        json_data = {
                    "projectId": project_id,
                    "name": folder_name,
                    "parentId": parent_id
                    }
        
    with allure.step(f"выполняем метод {method}"):
        response = session.post(url=url, json=json_data)
    
    if check:
        assert_status_code(response=response, method=method, role=role, status_code=200)

    return response

# endregion

#################################################################
#                        GET /v2/folders                        #
#################################################################
# region
''' функция выполняет метод GET /v2/folders, проверяет и возвращает ответ '''
def get_folders(external_password, project_id=None, search_string=None, parent_id=None, apply_parent_id='true',
                url=urls.url_folders, method='GET /v2/folders', role='project_admin', check=True):
    ''' функция выполняет метод GET /v2/folders, проверяет и возвращает ответ '''
    start_session(pssw=external_password)

    if project_id is None:
        project_id = static_data.PROJECT_ID

    with allure.step(f"Подготавливаем квери-параметры для запроса {method}"):
        params_data = {"projectId": project_id,
                        "searchString": search_string,
                        "parentId": parent_id,
                        "applyParentId": apply_parent_id}
        
    with allure.step(f"выполняем метод {method}"):
        response = session.get(url=url, params=params_data)

    if check:
        assert_status_code_and_json_schema(response=response, method=method, role=role, json_schema=valid_folders)

    return response

# endregion

#################################################################
#                        GET /v2/folders/id                     #
#################################################################
# region
''' функция выполняет метод GET /v2/folders/{folderId} и возвращает ответ '''
def get_folder(external_password, folder_id,
               role='project_admin', url=urls.url_folders, method='GET /v2/folders/id', check=True):
    ''' функция выполняет метод GET /v2/folders/{folderId} и возвращает ответ '''
    start_session(pssw=external_password)

    params_data = {"folderId": folder_id}

    with allure.step(f"Выполняем {method}"):
        response = session.get(url=f'{url}/{folder_id}', params=params_data)
    
    if check:
        assert_status_code_and_json_schema(response=response, method=method, role=role, json_schema=valid_folder)

    return response

# endregion




#################################################################
#                         POST documents                        #
#################################################################
# region
''' функция проверяет метод POST /v2/documents и возвращает response '''
def post_documents(external_password, project_id=None, folder_id=None, only_name=None, file_extension='txt', use_folder=True,
                   line_to_fill='hello, OTUS', n=None,
                   url=urls.url_documents, method='POST /v2/documents', role='project_admin', check=True):
    ''' функция проверяет метод POST /v2/documents и возвращает response '''
    start_session(pssw=external_password)

    if project_id is None:
        project_id = static_data.PROJECT_ID

    if only_name is None:
        only_name = f'file_{generate_datetime_for_file_name()}'

    if n is None:
        n = generate_random_number(100)

    if folder_id is None:
        with allure.step("создаем папку для загрузки, получаем ее id"):
            folder_id = post_folders(external_password=external_password).json()

    with allure.step("создаем файл"):
        create_binary_file(only_name=only_name, file_extension=file_extension, line_to_fill=line_to_fill, n=n)

    with allure.step("открываем созданный файлик для чтения"):
        with open(f'{only_name}.{file_extension}', 'rb') as my_file:
            # получаем содержимое файла
            file_content = my_file.read()

            with allure.step(f"выполняем метод {method}, в пэйлоаде передаем id проекта, id папки и созданный файлик"):
                response = session.post(url=url, files={'file': (my_file.name, file_content, 'text/plain')},
                data={'projectId': project_id, "folderId": folder_id, "useFolder": use_folder})

    #удаляем созданный файлик
    os.remove(f'{only_name}.{file_extension}')

    if check:
        assert_status_code(response=response, method=method, role=role, status_code=200)

    return response

# endregion

#################################################################
#                       POST JPG_documents                      #
#################################################################
# region
''' функция возвращает response метода POST /v2/documents '''
def post_JPG_documents(external_password, project_id=static_data.PROJECT_ID, folder_id=None, only_name=None,
                       width=512, height=256, indent=12, attempts=60, canvas_color=None):
    ''' функция возвращает response метода POST /v2/documents '''
    start_session(pssw=external_password)
    if folder_id is None:
        with allure.step("создаем папку для загрузки, получаем ее id"):
            folder_id = post_folders(external_password=external_password).json()

    if only_name is None:
        only_name = f'file_{generate_datetime_for_file_name_long()}'

    create_rectangle_image(only_name=only_name, width=width, height=height, indent=indent, canvas_color=canvas_color)

    # открываем созданный файлик для чтения
    with open(f'{only_name}.jpg', 'rb') as my_file: 
        # получаем содержимое файла
        file_content = my_file.read()

    with allure.step("выполняем метод POST documents, в пэйлоаде передаем id проекта, id папки и созданный файлик"):
        response = session.post(url=urls.url_documents, files={'file': (f'{only_name}.jpg', file_content, 'image/jpeg')},
        data={'projectId': project_id, "folderId": folder_id, "useFolder": True}, headers={})

    with allure.step("проверяем, что статус код ответа 200"):
        assert response.status_code == 200, f"статус код ответа метода POST /v2/documents != 200. текст ошибки: {response.text}"
    
    #удаляем созданный файлик
    os.remove(f'{only_name}.jpg')

    status = False
    with allure.step("дожидаемся optimizationStatus=DONE"):
        for _ in range(attempts):
            response_get = get_document(document_id=response.json(), external_password=external_password)
            if response_get.json()['optimizationStatus'] == 'DONE':
                status = True
                break
            time.sleep(0.5)

    if status:
        return response
    else:
        raise TimeoutError(f'Документ не оптимизировался за {attempts / 2} секунд')

# endregion

#################################################################
#                   GET /v2/documents/documentId                #
#################################################################
# region
''' функция проверяет метод GET /v2/documents/{documentId} и возвращает response '''
def get_document(document_id, external_password,
                 role='project_admin', url=urls.url_documents, method='GET /v2/documents/id', check=True):
    ''' функция проверяет метод GET /v2/documents/{documentId} и возвращает response '''
    start_session(pssw=external_password)
    with allure.step(f"выполняем метод {method}"):
        response = session.get(url=f'{urls.url_documents}/{document_id}')
    
    if check:
        assert_status_code_and_json_schema(response=response, method=method, role=role, json_schema=valid_document)

    return response

# endregion
