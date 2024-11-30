from voluptuous import MultipleInvalid

'''
функция проверяет статус код и соответствие ответа json-схеме
'''
def assert_status_code_and_json_schema(response=None, status_code=200, json_schema=None, method=None, role=None ):
    if role:
        assert response.status_code == status_code, f'''status code ответа метода {method}, выполненного ролью {role} != {status_code}.
            код ответа: {response.status_code}, текст ответа: {response.text}'''
    else:
        assert response.status_code == status_code, f'''status code ответа метода {method} != {status_code}.
            код ответа: {response.status_code}, текст ответа: {response.text}'''

    try: 
        json_schema(response.json())
    except MultipleInvalid as e: 
        assert False, f"json-схема ответа метода {method} не соответствует ФТ: {str(e)}"


'''
функция проверяет статус код ответа 
'''
def assert_status_code(response=None, status_code=None, method=None, role=None ):
    if isinstance(status_code, int):
        if role:
            assert response.status_code == status_code, f'''status code ответа метода {method}, выполненного ролью {role} != {status_code}.
                код ответа: {response.status_code}, текст ответа: {response.text}'''
        else:
            assert response.status_code == status_code, f'''status code ответа метода {method} != {status_code}.
                код ответа: {response.status_code}, текст ответа: {response.text}'''
    else:
        if role:
            assert response.status_code in status_code, f'''status code ответа метода {method}, выполненного ролью {role} not in {status_code}.
                код ответа: {response.status_code}, текст ответа: {response.text}'''
        else:
            assert response.status_code in status_code, f'''status code ответа метода {method} not in {status_code}.
                код ответа: {response.status_code}, текст ответа: {response.text}'''
            