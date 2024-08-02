from Windows.InstallationIndicatorWindow import LoadingIndicator
from logic.command_line_and_permissions import sub_run
from logic.line_changer import insert_a_line
from design_core import InstallerWindow
import threading


class PublishOneC(InstallerWindow):
    draw_back_button = False
    draw_next_button = False
    header_text = None
    body_text = None

    @classmethod
    def can_draw(cls, global_config):
        keys_to_check = ['publish_1c', 'connect_database', 'check_functionality']
        all_false = not all(not global_config.get(key, True) for key in keys_to_check)
        return all_false

    def draw(self):
        super().draw()

        self.loading_indicator = LoadingIndicator(self.main_frame, size=100, speed=50,
                                                  label_text="Loading Publish...")
        self.loading_indicator.set_parent(self.main_frame)

        one_c_user = self.global_config['One_C_the_user']
        one_c = self.global_config['One_C']

        base_user = self.global_config['base_the_One_C']
        base = self.global_config['base']

        def loading_task():

            if "1cv8t" in one_c[one_c_user]:
                webinst_command = [
                    f"{one_c[one_c_user]}\\bin\\webinstt",
                    "-publish",
                    "-apache24",
                    "-wsdir", "Base",
                    "-dir", r"c:\apache\htdocs\Base",
                    f"-connstr", base[base_user],
                    "-confpath", r"C:\Apache24\conf\httpd.conf"
                ]
                print(sub_run(webinst_command))
            else:
                webinst_command = [
                    f"{one_c[one_c_user]}\\bin\\webinst",
                    "-publish",
                    "-apache24",
                    "-wsdir", "Base",
                    "-dir", r"c:\apache\htdocs\Base",
                    f"-connstr", base[base_user],
                    "-confpath", r"C:\Apache24\conf\httpd.conf"
                ]
                print(webinst_command)
                print(sub_run(webinst_command))

            insert_a_line()

            print(sub_run(r'net stop Apache2.4'))
            print(sub_run(r'net start Apache2.4'))

            self.open_next_window()

        loading_thread = threading.Thread(target=loading_task)
        loading_thread.start()
