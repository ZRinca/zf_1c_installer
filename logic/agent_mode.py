import os
import queue
import threading
import subprocess
import time
from io import StringIO
from pathlib import Path

from Windows.window_error import show_error_window


# from Windows.window_error import show_error_window


def await_exec(ff, bool_tr, result_queue):
    collected_string = StringIO()

    build_string = ""
    if bool_tr:
        find_string = "\ndesigner>"
    else:
        find_string = "\nFATAL"

    while True:
        if bool_tr:
            char = ff.stdout.read(1)
            # print('two', char)
            if char == '':
                return
        else:
            char = ff.stderr.read(1)
            # print('one', str(char).encode('utf-8'))
            if char == '':
                return
        build_string += char
        if not find_string.startswith(build_string):
            build_string = char
        collected_string.write(char)
        if len(find_string) == len(build_string):
            if build_string in '\nFATAL':
                result_queue.put(True)
                return
            result_queue.put(collected_string.getvalue())
            return


def enter_commands_agent_mod(user, password):

    print(os.getcwd())
    cur_path = Path(os.getcwd()) / "PLINK.EXE"
    ff = subprocess.Popen(f'cmd /k "echo y | {cur_path} 127.0.0.1 && exit"', stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    ff.stdout.read(1)
    ff.kill()

    ff = subprocess.Popen(f'plink.exe -ssh -l {user} -pw "{password}" -P 1543 127.0.0.1', universal_newlines=True, encoding='utf-8',
                          shell=False,
                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    commands = [
        "common connect-ib\n",
        "config load-cfg --file=../InterfaceAPI.cfe --extension=IAPI\n",
        "config extensions properties set --extension=IAPI --safe-mode=no --unsafe-action-protection=no\n",
        "config update-db-cfg --extension=IAPI\n"
    ]
    result_queue = queue.Queue()
    for command in commands:
        result_queue_error = queue.Queue()
        tread_1 = threading.Thread(target=await_exec, args=(ff, False, result_queue_error, ))
        tread_2 = threading.Thread(target=await_exec, args=(ff, True, result_queue, ))
        tread_1.start()
        tread_2.start()
        error_msg = None
        while tread_2.is_alive() and tread_1.is_alive():
            time.sleep(1)

        # if tread_1.isAlive():
        #     tread_1.

        try:
            error_msg = result_queue_error.get_nowait()
            if error_msg:
                print('Произошла ошибка !')
                show_error_window('Не установленно расширение')
                break
        except queue.Empty:
            pass

        try:
            output_msg = result_queue.get_nowait()
            print(output_msg)
        except queue.Empty:
            pass
        if error_msg:
            ff.kill()
            show_error_window('Не было установленно расширение')
            return 'error'
        print('run_command', command)
        ff.stdin.write(command)
        ff.stdin.flush()
    # print(await_exec(ff, False, result_queue))
    ff.kill()
