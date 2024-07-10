import subprocess
from io import StringIO


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

    ff = subprocess.Popen(f'plink.exe -ssh -l {user} -pw "{password}" -P 1543 127.0.0.1', universal_newlines=True, encoding='utf-8',
                          shell=False,
                          stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    print(await_exec(ff))

    ff.stdin.write("common connect-ib\n")
    ff.stdin.flush()

    print(await_exec(ff))

    ff.stdin.write("config load-cfg --file=../InterfaceAPI.cfe --extension=IAPI\n")
    ff.stdin.flush()

    print(await_exec(ff))

    ff.stdin.write("config extensions properties set --extension=IAPI --safe-mode=no --unsafe-action-protection=no\n")
    ff.stdin.flush()

    print(await_exec(ff))

    ff.stdin.write("config update-db-cfg --extension=IAPI\n")
    ff.stdin.flush()

    print(await_exec(ff))

    ff.kill()
