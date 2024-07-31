from Windows.InstallationIndicatorWindow import LoadingIndicator
from logic.agent_mode import enter_commands_agent_mod
from logic.command_line_and_permissions import sub_run
from design_core import InstallerWindow
import threading


class Extension(InstallerWindow):
    draw_back_button = False
    draw_next_button = False
    header_text = None
    body_text = None

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


        def loading_task():

            one_c_user = self.global_config['One_C_the_user']
            one_c = self.global_config['One_C']

            if "1cv8t" in one_c[one_c_user]:
                designer_command = [
                    r"C:\Program Files\1cv8\common\1cestartt.exe",
                    "DESIGNER",
                    "/AgentMode",
                    "/AgentBaseDir", r"C:\Apache24\Api",
                    "/IBName", self.global_config['base_the_One_C'],
                    "/AgentSSHHostKeyAuto",
                    "/Visible"
                ]

                print(sub_run(designer_command))
            else:
                designer_command = [
                    r"C:\Program Files\1cv8\common\1cestart.exe",
                    "DESIGNER",
                    "/AgentMode",
                    "/AgentBaseDir", r"C:\Apache24\Api",
                    "/IBName", self.global_config['base_the_One_C'],
                    "/AgentSSHHostKeyAuto",
                    "/Visible"
                ]

                print(sub_run(designer_command))
            enter_commands_agent_mod(self.global_config['LOGIN'], self.global_config['PASSWORD'])

            self.open_next_window()

        loading_thread = threading.Thread(target=loading_task)
        loading_thread.start()

