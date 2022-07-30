"""Create folder"""


def folder_dont_create(response):
    return f"Папка не создалась. Код ответа сервера {response.status_code}"


def bad_server_request(response):
    return f"Неверный ответ сервера: {response.reason}"


bad_folder_name = "Имя папки неверно"


def folder_not_delete(response):
    return f"Папка не удалилась. Код ответа сервера {response.status_code}"
