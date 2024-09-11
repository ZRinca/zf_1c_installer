import sys

try:
    import pyi_splash
    pyi_splash.close()
except:
    pass

base_path = sys._MEIPASS

print('aaaaaaaaaaaaaa', base_path)

input()