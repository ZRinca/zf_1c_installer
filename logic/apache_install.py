from logic.installing_file import copy_file
from settings import the_path_to_Apache


def copy_apache_and_exp(bit):
    source_dir = None
    if bit == 32:
        source_dir = r'Apache/Apache_32/Apache24'
    if bit == 64:
        source_dir = r'Apache/Apache_64/Apache24'
    copy_file(source_dir, the_path_to_Apache)
    copy_file('extension', f"{the_path_to_Apache}\\Api")
    return


def parsing_apache_httpd():
    with open(r'C:\Apache24\conf\httpd.conf', 'r') as file_read:
        httpd = file_read.read()