# в данном файле содержатся функции для отправки запросов к API
import requests
import configuration, data


def get_body(kit_name) -> dict:
    """
    Функция для получения тела запроса под конкретный тест
    :param kit_name: имя набора
    :return: словарь с телом запроса
    """
    new_body = data.create_kit_body.copy()  # копируем шаблон тела запроса из data
    new_body['name'] = kit_name  # изменяем параметр тела name на параметр функции kit_name
    return new_body  # возвращаем новое значение тела запроса


def post_new_user() -> requests.Response:
    """
    Функция для отправки запроса создания нового пользователя
    :param body: словарь с параметрами пользователя
    :return: объект Response
    """
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=data.create_user_body,  # тут тело
                         headers=data.headers_create_user)  # а здесь заголовки



def post_new_user_kit(kit_body, auth_token) -> requests.Response:
    """
    Функция для отправки запроса создания набора пользователя
    :param kit_name: имя набора
    :param auth_token: токен пользователя
    :return: объект Response
    """
    request_headers = data.headers_create_user_kit.copy()  # копируем шаблон тела запроса из data
    request_headers["Authorization"] = f"Bearer {auth_token}"  # вставляем значение токена пользователя

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,  # подставляем полный url
                         json=kit_body,  # тут тело
                         headers=request_headers) # заголовки


def get_auth_token() -> str:
    """
    Функция для получения authToken пользователя
    :return: строка со значением токена
    """
    server_response = post_new_user()  # отправляем запрос на создание пользователя, записываем ответ
    response_dict = server_response.json()  # json из ответа записываем в переменную response_dict
    auth_token = response_dict['authToken']  # записываем значение токена в переменную auth_token
    return auth_token  # возвращаем переменную с токеном


if __name__ == "__main__":
    auth = get_auth_token()
