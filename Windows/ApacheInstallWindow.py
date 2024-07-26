from Windows.InstallationIndicatorWindow import LoadingIndicator
from installing_apache_and_file import copy_apache_and_exp
from command_line_and_permissions import sub_run
from design_core import InstallerWindow
from exe_bit_extractor import exe_bit
import threading


class ApacheInstall(InstallerWindow):
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
                                                  label_text="Loading Apache...")
        self.loading_indicator.set_parent(self.main_frame)

        def loading_task():

            one_c_user = self.global_config['One_C_the_user']
            one_c = self.global_config['One_C']

            if "1cv8t" in one_c[one_c_user]:
                bit = exe_bit(f'{one_c[one_c_user]}\\bin\\1cv8t.exe')
            else:
                bit = exe_bit(f'{one_c[one_c_user]}\\bin\\1cv8.exe')
            copy_apache_and_exp(bit)

            print(sub_run(r'C:\Apache24\bin\httpd.exe -k install'))
            print(sub_run(r'net stop Apache2.4'))
            print(sub_run(r'net start Apache2.4'))

            self.open_next_window()

        loading_thread = threading.Thread(target=loading_task)
        loading_thread.start()

