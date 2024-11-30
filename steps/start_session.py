import requests
import pytest
import warnings

from resources import urls
from resources import certs

warnings.filterwarnings("ignore")


session = requests.Session()
'''дергаем любой метод гет, чтобы создать сессию админом аккаунта'''
def start_session():
    session.get(url=urls.url_get_me, cert=certs.admin_cert, verify=False)

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
