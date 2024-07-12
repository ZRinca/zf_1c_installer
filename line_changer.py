import os
import re


def replace_line_in_file(input_file, output_file, old_line_pattern, new_line):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        content_new = re.sub(old_line_pattern, new_line, content)

        with open(output_file, 'w', encoding='utf-8') as fout:
            fout.write(content_new)

        print(f'Строка успешно заменена и записана в файл: {output_file}')
    except IOError as e:
        print(f'Ошибка при чтении или записи файла: {e}')



folder = 'folder'
input_file_name = 'без_галочек.vrd'
output_file_name = 'новый_файл.vrd'
input_file_path = os.path.join(folder, input_file_name)
output_file_path = os.path.join(folder, output_file_name)

old_line_pattern = r'<ws enable="false"\s*pointEnableCommon="false">'
new_line = '<ws publishExtensionsByDefault="true">'

replace_line_in_file(input_file_path, output_file_path, old_line_pattern, new_line)

old_line_pattern = r'<httpServices publishByDefault="false">'
new_line = '<httpServices publishExtensionsByDefault="true">'

replace_line_in_file(input_file_path, output_file_path, old_line_pattern, new_line)