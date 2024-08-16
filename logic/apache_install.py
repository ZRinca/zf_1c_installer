from logic.command_line_and_permissions import re_parser, read_the_file
from logic.installing_file import copy_file
from settings import the_path_to_Apache
import os


def copy_apache_and_exp(bit):
    source_dir = None
    if bit == 32:
        source_dir = r'Apache/Apache_32/Apache24'
    if bit == 64:
        source_dir = r'Apache/Apache_64/Apache24'
    copy_file(source_dir, the_path_to_Apache)
    copy_file('extension', f"{the_path_to_Apache}\\Api")
    return


def find_publication_apache(global_config):
    base_user_one_c = global_config['base_the_One_C']
    base = global_config['base']
    base_user = re_parser(base[base_user_one_c], 'File="', '";')
    link_vrd = re_parser(read_the_file(r'C:\Apache24\conf\httpd.conf'), 'ManagedApplicationDescriptor', '</Directory>')
    for link in link_vrd:
        if not os.path.exists(link):
            continue
        link_vrd = re_parser(read_the_file(link), 'File=&quot;', '&quot;;')
        if base_user[0] in link_vrd[0]:
            return re_parser(read_the_file(link), 'base="', '"')[0]
