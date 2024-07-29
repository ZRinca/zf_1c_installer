import os
import subprocess
from io import StringIO
from pathlib import Path


def await_exec(ff):
    collected_string = StringIO()

    build_string = ""
    find_string = "\ndesigner>"

    while True:
        char = ff.stdout.read(1)
        build_string += char
        if not find_string.startswith(build_string):
            build_string = char
        collected_string.write(char)
        if len(find_string) == len(build_string):
            return collected_string.getvalue()


def enter_commands_agent_mod(user, password):

    print(os.getcwd())
    cur_path = Path(os.getcwd()) / "PLINK.EXE"
    ff = subprocess.Popen(f'cmd /k "echo y | {cur_path} 127.0.0.1 && exit"', stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    ff.stdout.read(1)
    ff.kill()

    ff = subprocess.Popen(f'plink.exe -ssh -l {user} -pw "{password}" -P 1543 127.0.0.1', universal_newlines=True, encoding='utf-8',
                          shell=False,
                          stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    commands = [
        "common connect-ib\n",
        "config load-cfg --file=../InterfaceAPI.cfe --extension=IAPI\n",
        "config extensions properties set --extension=IAPI --safe-mode=no --unsafe-action-protection=no\n",
        "config update-db-cfg --extension=IAPI\n"
    ]

    for command in commands:
        print(await_exec(ff))
        ff.stdin.write(command)
        ff.stdin.flush()

    print(await_exec(ff))
    ff.kill()
