import threading

from Windows.InstallationIndicatorWindow import LoadingIndicator
from command_line_and_permissions import sub_run
from design_core import InstallerWindow


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
            # Выполнение команд в отдельном потоке
            print(sub_run(r'C:\Apache24\bin\httpd.exe -k install'))
            print(sub_run(r'net stop Apache2.4'))
            print(sub_run(r'net start Apache2.4'))

            # После выполнения команд вызов метода для открытия следующего окна
            self.main_frame.after(0, self.open_next_window)

        # Создание и запуск потока
        loading_thread = threading.Thread(target=loading_task)
        loading_thread.start()
