import requests


def checking_code_status():
    url = "http://localhost/Base/ru_RU/"
    www = requests.get(url)

    if www.status_code == 200:
        return 200