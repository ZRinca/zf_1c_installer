from window_creator import show_error_window
import requests
import os


def checking_code_status():
    url = "http://localhost/Base/ru_RU/"
    www = requests.get(url)

    if www.status_code == 200:
        return 200


def check_file_availability(file):
    print(file)
    if os.path.isfile(file):
        return True
    else:
        return False
