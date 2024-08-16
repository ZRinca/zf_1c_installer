import subprocess
import json
import re


def sub_run(commands):
    print(commands)
    p = subprocess.run(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       encoding='CP866')
    if p.stderr == '':
        return p.stdout
    if p.stdout == '':
        return p.stderr
    else:
        return 'output is empty !'


def extract_bases(file_content):
    pattern = re.compile(r'\[([^\]]+)\]\s+Connect=(.*)')
    matches = pattern.findall(file_content)
    return {key: value for key, value in matches}


def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_read_json(link_file, key, value):
    with open(link_file, 'r') as json_read:
        json_r = json.load(json_read)

    json_r[key] = value

    with open(link_file, 'w') as json_write:
        json.dump(json_r, json_write, indent=4)


def re_parser(text, beginning_line, end_line):
    pattern_re = f'{beginning_line}(.*?){end_line}'
    matches = re.finditer(pattern_re, text, re.DOTALL)

    link_found = []

    for match in matches:
        link = match.group(1).strip()
        link_found.append(link.strip('"'))
    return link_found


def read_the_file(path):
    try:
        with open(path, 'r') as file:
            file_r = file.read()
        return file_r
    except FileNotFoundError:
        return 'Файл не найден'
