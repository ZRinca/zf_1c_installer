from Windows.window_error import show_error_window
from pathlib import Path
from io import StringIO
import subprocess
import threading
import time
import os

from settings import plink


def await_text(stream, find_string, result=None):
    collected_string = StringIO()
    build_string = ''

    while True:
        char = stream.read(1)
        if char == '':
            return
        build_string += char
        if not find_string.startswith(build_string):
            build_string = char
        collected_string.write(char)
        if len(find_string) == len(build_string):
            if result is not None:
                result[0] = collected_string.getvalue()
            return


def enter_commands_agent_mod(user, password):

    while True:
        print(os.getcwd())
        cur_path = Path(os.getcwd()) / plink
        ff = subprocess.Popen(f'cmd /k "echo y | {cur_path} -ssh -P 1543 127.0.0.1 && exit"', stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        ff.stdout.read(1)
        ff.kill()

        error_text = ff.stderr.read()
        print(error_text)
        if not error_text.startswith(b'FATAL ERROR: Network error: Connection refused'):
            break

    ff = subprocess.Popen(f'plink.exe -ssh -P 1543 127.0.0.1', universal_newlines=True, encoding='utf-8',
                          shell=False,
                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    await_text(ff.stdout, 'login as:')

    ff.stdin.write(str(user) + '\n')
    ff.stdin.flush()

    await_text(ff.stdout, 'password:')

    ff.stdin.write(str(password) + '\n')
    ff.stdin.flush()

    a = ff.stderr.read(8)
    if a.startswith('Access'):
        show_error_window('Неправильный логин или пароль!')
        ff.kill()
        return True

    commands = [
        'common connect-ib\n',
        'config load-cfg --file=../InterfaceAPI.cfe --extension=IAPI\n',
        'config extensions properties set --extension=IAPI --safe-mode=no --unsafe-action-protection=no\n',
        'config update-db-cfg --extension=IAPI\n'
    ]

    for command in commands:
        result_queue_error = [None]
        result_queue = [None]

        tread_1 = threading.Thread(target=await_text, args=(ff.stdout, '\ndesigner>', result_queue, ))
        tread_2 = threading.Thread(target=await_text, args=(ff.stderr, '\nFATAL', result_queue_error, ))
        tread_1.start()
        tread_2.start()
        while tread_2.is_alive() and tread_1.is_alive():
            time.sleep(1)

        error_msg = result_queue_error[0]
        if error_msg:
            ff.kill()
            show_error_window('Не установленно расширение')
            break
        output_msg = result_queue[0]
        print(output_msg)
        print('run_command', command)
        ff.stdin.write(command)
        ff.stdin.flush()
    ff.kill()
