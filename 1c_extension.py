import subprocess

v8unpack_exe_path = "путь_к_v8unpack.exe"

source_extension_path = "путь_к_исходному_файлу_расширения"

destination_path = "путь_куда_распаковать"

command = [v8unpack_exe_path, "-D", source_extension_path, destination_path]

try:
    subprocess.run(command, check=True)
    print("Распаковка успешно завершена.")
except subprocess.CalledProcessError as e:
    print(f"Ошибка при выполнении команды: {e}")