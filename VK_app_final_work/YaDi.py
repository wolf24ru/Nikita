import requests

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self, path_file):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': path_file}
        response = requests.get(files_url, params=params, headers=headers)
        return response.json()

    def create_folder(self, name_folder):
        folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': name_folder}
        headers = self.get_headers()
        response = requests.put(folder_url, params=params, headers=headers)
        return response.status_code

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(
            disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

    def upload_file_link_to_disk(self, disk_file_path, link):
        href = self._get_upload_link(
            disk_file_path=disk_file_path).get("href", "")
        file = requests.get(link)
        response = requests.put(href, data=file.content)
        response.raise_for_status()
        # if response.status_code == 201:
        #     print("Success")