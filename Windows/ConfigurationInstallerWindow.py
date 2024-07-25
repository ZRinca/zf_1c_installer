from design_core import InstallerWindow


class ConfigurationInstallerWindow(InstallerWindow):
    header_text = 'Установка расширения'
    body_text = 'Установка расширения'

    @classmethod
    def can_draw(cls, global_config):
        return global_config.get('install_1c_extension', True)