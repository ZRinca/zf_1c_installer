import sys


def screen_closer():
    try:
        import pyi_splash
        pyi_splash.close()
    except ImportError:
        pass


def base_path():
    path = sys._MEIPASS
    return path
