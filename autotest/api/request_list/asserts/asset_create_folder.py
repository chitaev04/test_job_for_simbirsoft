from autotest.api.const.URLs import CHECK_FOLDER_NAME
from autotest.api.const.messeges.assert_messeges import folder_dont_create, bad_server_request, bad_folder_name, \
    folder_not_delete
from autotest.api.const.reasons import reasons


def assert_create_folder(response, name_folder):
    assert response.status_code == 201, folder_dont_create(response)
    assert response.reason == reasons['created'], bad_server_request(response)
    assert response.url == f"{CHECK_FOLDER_NAME}{name_folder}", bad_folder_name


def assert_delete_folder(response):
    assert response.status_code == 204, folder_not_delete(response)
