import requests
import pytest
import warnings
import base64

from resources import urls
from resources import certs


warnings.filterwarnings("ignore")

def encode_to_base64(input_string):
    # Преобразуем строку в байты
    byte_string = input_string.encode('utf-8')
    # Кодируем байты в base64
    base64_bytes = base64.b64encode(byte_string)
    # Преобразуем закодированные байты обратно в строку
    base64_string = base64_bytes.decode('utf-8')
    return base64_string


session = requests.Session()
'''дергаем любой метод гет, чтобы создать сессию админом аккаунта'''
def start_session(pssw):
    response_me = session.get(url=f'{urls.url_base}/v2/users/me', verify=False)
    if response_me.status_code in (400, 401):
        session.cookies.clear()

        password_in_base64 = encode_to_base64(pssw)
        json_data = {"email": "iegudyrev@yandex.ru","password": password_in_base64}
        response_login = session.post(url=urls.url_login, json=json_data, verify=False)

        ck = response_login.json()["confirmationKey"]
        json_data = {"code": "777777","confirmationKey": ck}
        response_confirm = session.post(url=urls.url_confirm, json=json_data)

        response_me = session.get(url=f'{urls.url_base}/v2/users/me', verify=False)
        if response_me.status_code != 200:
            raise Exception('something wrong with user authorization')


user_session = requests.Session()
'''дергаем любой метод гет, чтобы создать сессию участником проекта'''
def start_user_session():
    user_session.get(url=urls.url_get_me, cert=certs.user_cert, verify=False)

access_admin_session = requests.Session()
'''дергаем любой метод гет, чтобы создать сессию администратором доступа'''
def start_access_admin_session():
    access_admin_session.get(url=urls.url_get_me, cert=certs.access_admin_cert, verify=False)

business_admin_session = requests.Session()
'''дергаем любой метод гет, чтобы создать сессию бизнес администратором'''
def start_business_admin_session():
    business_admin_session.get(url=urls.url_get_me, cert=certs.business_admin_cert, verify=False)

unauthorized_session = requests.Session()
'''дергаем любой метод гет, чтобы создать сессию неавторизированным пользователем'''
def start_unauthorized_session():
    unauthorized_session.get(url=urls.url_get_me, cert=certs.unauthorized_cert, verify=False)


START_SESSION = {
                'business_admin': start_business_admin_session,
                'user': start_user_session, 
                'access_admin': start_access_admin_session,
                'project_admin': start_session   
                }

SESSIONS = {
            "user": user_session,
            "business_admin": business_admin_session,
            "access_admin": access_admin_session,
            'project_admin': session  
            }
