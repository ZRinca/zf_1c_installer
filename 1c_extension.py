# v8unpack.exe -D <путь_к_исходному_файлу_расширения> <путь_куда_распаковать>

import subprocess

# Путь к исполняемому файлу v8unpack.exe
v8unpack_exe_path = "путь_к_v8unpack.exe"

# Путь к исходному файлу расширения 1С
source_extension_path = "путь_к_исходному_файлу_расширения"

# Путь, куда распаковать файлы из расширения
destination_path = "путь_куда_распаковать"

# Формируем команду для выполнения
command = [v8unpack_exe_path, "-D", source_extension_path, destination_path]

try:
    # Запускаем v8unpack.exe с помощью subprocess
    subprocess.run(command, check=True)
    print("Распаковка успешно завершена.")
except subprocess.CalledProcessError as e:
    print(f"Ошибка при выполнении команды: {e}")