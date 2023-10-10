# файл с тестами и вспомогательными функциями
import sender_stand_request
from sender_stand_request import auth


def positive_assert(kit_name) -> None:
    """
    Функция для запуска позитивной проверки создания нового набора пользователя
    :param kit_name: имя набора
    :return: None
    """
    kit_body = sender_stand_request.get_body(kit_name)  # получаем тело запроса с именем из параметра kit_name
    auth_token = auth  # получаем токен пользователя
    create_kit_response = sender_stand_request.post_new_user_kit(kit_body, auth_token)  # отправляем запрос и записываем ответ

    assert create_kit_response.status_code == 201  # проверяем, что код ответа 201
    assert create_kit_response.json()["name"] == kit_name  # проверяем, что имя набора в ответе равно значению kit_name


def negative_assert (kit_name) -> None:
    """
    Функция для запуска негативных проверок создания набора пользователя
    :param kit_name: невалидное имя набора
    :return: None
    """
    kit_body = sender_stand_request.get_body(kit_name)  # получаем тело запроса с именем из параметра kit_name
    auth_token = auth  # получаем токен пользователя
    create_kit_response = sender_stand_request.post_new_user_kit(kit_body, auth_token)  # отправляем запрос и записываем ответ

    assert create_kit_response.status_code == 400  # проверяем, что код ответа 400


def negative_assert_with_no_parametr() -> None:
    """
    Функция для запуска негативных проверок создания набора пользователя, когда не передан ни один параметр
    :return: None
    """
    kit_body = {}  # записываем в тело пустое значение (без параметров)
    auth_token = auth  # получаем токен пользователя
    create_kit_response = sender_stand_request.post_new_user_kit(kit_body, auth_token)  # отправляем запрос и записываем ответ

    assert create_kit_response.status_code == 400  # проверяем, что код ответа 400


# Тест 1. Успешное создание набора пользоваеля с именем набора, состоящим из 1 символа
def test_create_user_kit_with_1_symbol_name_get_success_response():
    positive_assert("a")


# Тест 2. Успешное создание набора пользоваеля с именем набора, состоящим из 511 символов
def test_create_user_kit_with_511_symbol_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Тест 3. Ошибка при создании набора пользоваеля с именем набора, состоящим из 0 символов
def test_create_user_kit_with_0_symbol_name_get_error_response():
    negative_assert("")


# Тест 4. Ошибка при создании набора пользоваеля с именем набора, состоящим из 512 символов
def test_create_user_kit_with_512_symbol_name_get_error_response():
    negative_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Тест 5. Успешное создание набора пользоваеля с именем набора, состоящим из символов англ алфавита
def test_create_user_kit_with_eng_letters_name_get_success_response():
    positive_assert("QWErty")


# Тест 6. Успешное создание набора пользоваеля с именем набора, состоящим из символов русского алфавита
def test_create_user_kit_with_rus_letters_name_get_success_response():
    positive_assert("Мария")


# Тест 7. Успешное создание набора пользоваеля с именем набора, состоящим из спец символов
def test_create_user_kit_with_spec_symbols_name_get_success_response():
    positive_assert("\"№%@\",")


# Тест 8. Успешное создание набора пользоваеля с именем набора, в котором есть пробел
def test_create_user_kit_with_spece_in_name_get_success_response():
    positive_assert("Человек и КО")


# Тест 9. Успешное создание набора пользоваеля с именем набора, в котором есть цифры
def test_create_user_kit_with_digits_in_name_get_success_response():
    positive_assert("123")


# Тест 10. Ошибка при создании набора пользоваеля, если не передано ни одного параметра
def test_create_user_kit_with_no_parametr_get_error_response():
    negative_assert_with_no_parametr()


# Тест 11. Ошибка при создании набора пользоваеля, если в параметре имени набора передан не строковый тип данных - int
def test_create_user_kit_with_not_str_type_in_name_get_error_response():
    negative_assert(123)

