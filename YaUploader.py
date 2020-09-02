import requests
import os


class YaUploader:

    def __init__(self, file_path: str, yandex_token: str):
        self.file_path = file_path
        self.file_name = os.path.basename(self.file_path)
        self.YANDEX_TOKEN = yandex_token

    def get_upload_url(self):
        result = dict()
        header = dict()
        url_for_request = f"https://cloud-api.yandex.net/v1/disk/resources/upload?path=%2f{self.file_name}&overwrite=true"
        header["Authorization"] = self.YANDEX_TOKEN
        response = requests.get(url_for_request, params={}, headers=header)
        result["status_code"] = response.status_code
        if response.status_code == 200:
            result["href"] = response.json()['href']
            result["message"] = "Сервер вернул адрес для загрузки"
        else:
            result["message"] = response.json()['message']

        return result

    def upload_file(self, url_for_upload):
        result = dict()
        with open(file=self.file_path, mode="rb") as f:
            response = requests.put(url=url_for_upload, data=f)
        result["status_code"] = response.status_code

        if response.status_code in (200, 201):
            result["message"] = f"Файл успешно загружен"
        else:
            result["message"] = response.json()["message"]
        return result

    def upload(self):
        result = dict()
        response = self.get_upload_url()
        if response["status_code"] in (200, 201):
            result = self.upload_file(response["href"])
        else:
            result = response

        print(result["message"])

        return result


if __name__ == '__main__':
    uploader = YaUploader('files\\testupload.txt',
                          "there is must be a token for Yandex Disk")
    result = uploader.upload()
    print(result["message"], result["status_code"])
