from Windows.InstallationIndicatorWindow import LoadingIndicator
from added_to_the_task_scheduler import added_task
from installing_apache_and_file import copy_file
from design_core import InstallerWindow
import threading


class InstallZF(InstallerWindow):
    draw_back_button = False
    draw_next_button = False
    header_text = None
    body_text = None

    @classmethod
    def can_draw(cls, global_config):
        keys_to_check = ['install_apache', 'install_zf']
        all_false = not all(not global_config.get(key, True) for key in keys_to_check)
        return all_false

    def draw(self):
        super().draw()

        self.loading_indicator = LoadingIndicator(self.main_frame, size=100, speed=50,
                                                  label_text="Loading ZF...")
        self.loading_indicator.set_parent(self.main_frame)

        def loading_task():
            copy_file('zf_1c_connect_client', 'C:\\zf_connector')
            added_task()
            self.open_next_window()

        loading_thread = threading.Thread(target=loading_task)
        loading_thread.start()
