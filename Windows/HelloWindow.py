from design_core import InstallerWindow


class HelloWindow(InstallerWindow):
    draw_back_button = False
    installer_version = True

    header_text = 'Мастер настройки ZeroFactor'
    body_text = ('Мастер настройки ZeroFactor поможет вам быстро настроить 1С и связать \nвашу '
                 'информационную базу с ZeroFactor. Подробнее о ZeroFactor, \nего компонентах '
                 'и технических особенностях можно узнать на нашем \nсайте.\n\n'
                 'При продолжении установки и/или использовании продукта '
                 '(в т.ч. его \nкомпонентов) вы соглашаетесь с документами, '
                 'размещёнными \nна сайте.')
    site_link = ['Наш сайт: ', 'zerofactor.ru']

    def draw(self):
        super().draw()
