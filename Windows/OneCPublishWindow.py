from Windows.InstallationIndicatorWindow import LoadingIndicator
from logic.logic_function import publish_one_c
from design_core import InstallerWindow


class PublishOneC(InstallerWindow):
    technical_function = publish_one_c
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
        self.run_tech_task(False)
