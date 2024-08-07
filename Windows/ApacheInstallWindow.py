from Windows.InstallationIndicatorWindow import LoadingIndicator
from logic.apache_install import install_apache
from design_core import InstallerWindow


class ApacheInstall(InstallerWindow):
    draw_back_button = False
    draw_next_button = False
    header_text = None
    body_text = None
    technical_function = install_apache

    @classmethod
    def can_draw(cls, global_config):
        keys_to_check = ['install_apache']
        all_false = not all(not global_config.get(key, True) for key in keys_to_check)
        return all_false

    def draw(self):
        super().draw()
        self.loading_indicator = LoadingIndicator(self.main_frame, size=100, speed=50,
                                                  label_text="Loading Apache...")
        self.loading_indicator.set_parent(self.main_frame)
        self.run_tech_task(False)
        