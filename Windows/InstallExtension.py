from Windows.InstallationIndicatorWindow import LoadingIndicator
from logic.agent_mode import enter_commands_agent_mod
from logic.command_line_and_permissions import sub_run
from design_core import InstallerWindow
import threading

from logic.techical_functions import install_extension


class Extension(InstallerWindow):
    draw_back_button = False
    draw_next_button = False
    header_text = None
    body_text = None
    technical_function = install_extension

    @classmethod
    def can_draw(cls, global_config):
        keys_to_check = ['install_1c_extension', 'connect_database', 'check_functionality']
        all_false = not all(not global_config.get(key, True) for key in keys_to_check)
        return all_false

    def draw(self):
        super().draw()
        self.loading_indicator = LoadingIndicator(self.main_frame, size=100, speed=50,
                                                  label_text="Loading Extension...")
        self.loading_indicator.set_parent(self.main_frame)
        self.run_tech_task(False)
