import requests
import pytest
from pprint import pprint

class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.json())
        return response.json()

    def put_create_folder(self, pah_folder):
        resources_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {
            'path': pah_folder
        }
        respose = requests.put(resources_url, params=params, headers=headers)
        return respose


class TestYndexAPI:

    @pytest.mark.parametrize('name_folder',[
        '',
        'new_folder_from_py',
        132,
        None,
        False,
        'new_folder_from_py',
        '234sd',
        '__43__',
        [123, 123],
        ['fdf', 213],
        [i for i in range(200)]
    ])
    def test_add_file_reqest(self, name_folder):
        TOKEN = ''
        Ydisk = YandexDisk(TOKEN)
        path = f'python_test/{name_folder}'
        folder = Ydisk.put_create_folder(path)
        print(f'{folder}\n{folder.json()}')
        assert folder.status_code == 201


if __name__ == '__main__':
    pytest.main()