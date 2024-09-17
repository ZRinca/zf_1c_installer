"""Do not delete the import Window"""
import Windows
from design_core import run_design
from logic.app_starter import screen_closer

screen_closer()
GLOBAL_CONFIG = {}

if __name__ == "__main__":
    run_design(GLOBAL_CONFIG)
