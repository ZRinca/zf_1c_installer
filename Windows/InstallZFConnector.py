from Windows.InstallationIndicatorWindow import LoadingIndicator
from logic.command_line_and_permissions import sub_run
from logic.installing_file import copy_file
from design_core import InstallerWindow
from settings import the_path_to_zf
import threading


class InstallZF(InstallerWindow):
    draw_back_button = False
    draw_next_button = False
    header_text = None
    body_text = None

    @classmethod
    def can_draw(cls, global_config):
        keys_to_check = ['install_zf']
        all_false = not all(not global_config.get(key, True) for key in keys_to_check)
        return all_false

    def draw(self):
        super().draw()

        self.loading_indicator = LoadingIndicator(self.main_frame, size=100, speed=50,
                                                  label_text="Loading ZF...")
        self.loading_indicator.set_parent(self.main_frame)

        def loading_task():
            copy_file('zf_1c_connect_client', the_path_to_zf)
            sub_run(r'SCHTASKS /Create /TN \ZeroFactor\ZFConnector /XML C:\Apache24\Api\ZFConnector_settings.xml')
            self.open_next_window()

        loading_thread = threading.Thread(target=loading_task)
        loading_thread.start()
