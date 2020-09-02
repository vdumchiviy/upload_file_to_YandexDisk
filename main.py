import YaUploader
YATOKEN = "there is must be a token for Yandex Disk"


def main():
    file_path = input("введите путь к файлу:")
    service = YaUploader.YaUploader(file_path, YATOKEN)
    result = service.upload()
    print(f"{result['status_code']}: {result['message']}")


main()
