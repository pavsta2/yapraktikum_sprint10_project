# Заголоовок для запроса создания нового пользователя
headers_create_user = {
    "Content-Type": "application/json"
}

# Шаблон заголовков запроса для создания нового набора пользователя
headers_create_user_kit = {
    "Content-Type": "application/json",
    "Authorization": "Bearer auth_token"
}

# Тело для запроса создания нового пользователя
create_user_body = {
    "firstName": "pavel",
    "phone": "+74441237887",
    "address": "г. Москва, ул. Хохотушкина, д. 16"}

# Шаблон тела запроса для создания нового набора пользователя
create_kit_body = {
    "name": "name"
}
