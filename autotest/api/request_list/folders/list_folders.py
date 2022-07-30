import requests

from autotest.api.const.URLs import URL_FOLDER
from autotest.api.const.headers import headers
from autotest.api.const.shemas.folders_shemas import schema_create_folder
from autotest.api.request_list.asserts.asset_create_folder import assert_create_folder
from autotest.auxiliary.auxiliary_func import string_generate
from jsonschema import validate

name_folder = string_generate(10)


def create_folder():
    """Создание папки"""
    response = requests.put(url=f"{URL_FOLDER}?path={name_folder}", headers=headers)
    validate(response.json(), schema_create_folder)
    assert_create_folder(response, name_folder)


def delete_folder():
    """Удаление папки"""
    response = requests.delete(url=f"{URL_FOLDER}?path={name_folder}", headers=headers)
    assert response.status_code == 204, f"Папка не удалилась. Код ответа сервера {response.status_code}"
