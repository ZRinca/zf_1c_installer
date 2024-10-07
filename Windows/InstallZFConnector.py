from Windows.InstallationIndicatorWindow import LoadingIndicator
from logic.logic_function import install_zf
from design_core import InstallerWindow


class InstallZF(InstallerWindow):
    draw_back_button = False
    draw_next_button = False
    header_text = None
    body_text = None
    technical_function = install_zf

    @classmethod
    def can_draw(cls, global_config):
        keys_to_check = ['install_zf']
        all_false = not all(not global_config.get(key, True) for key in keys_to_check)
        return all_false

    def draw(self):
        super().draw()
        self.loading_indicator = LoadingIndicator(self.main_frame, size=100, speed=50,
                                                  label_text="Установка ZF...")
        self.loading_indicator.set_parent(self.main_frame)
        self.run_tech_task(False)
