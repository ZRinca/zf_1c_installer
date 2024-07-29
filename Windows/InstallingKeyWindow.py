from installing_apache_and_file import move_and_rename_deskey_file
from Windows.InstallationIndicatorWindow import LoadingIndicator
from design_core import InstallerWindow
import threading


class InstallingKey(InstallerWindow):
    draw_back_button = False
    draw_next_button = False
    header_text = None
    body_text = None

    @classmethod
    def can_draw(cls, global_config):
        keys_to_check = ['install_zf', 'check_functionality']
        all_false = not all(not global_config.get(key, True) for key in keys_to_check)
        return all_false

    def draw(self):
        super().draw()

        self.loading_indicator = LoadingIndicator(self.main_frame, size=100, speed=50, label_text='Loading Key...')
        self.loading_indicator.set_parent(self.main_frame)

        def loading_task():
            move_and_rename_deskey_file(self.global_config['link_key'], 'source_key.dskey', 'C:\\zf_connector')
            self.open_next_window()

        loading_thread = threading.Thread(target=loading_task)
        loading_thread.start()
