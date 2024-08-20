from design_core import InstallerWindow


class HelloWindow(InstallerWindow):
    draw_back_button = False
    header_text = 'Мастер настройки ZeroFactor'
    body_text = ('Мастер настройки ZeroFactor поможет вам быстро настроить 1С и связать вашу \nинформационную базу с ZeroFactor'
                 'Подробнее о ZeroFactor, его компонентах \nи технических особенностях, можно узнать на сайте: zerofactor.ru'
                 '\n\nПри продолжении установки и/или использовании продукта \n(в т.ч. его компонентов) вы соглашаетесь с документами,'
                 ' размещёнными на \nсайте zerofactor.ru.')

    def draw(self):
        super().draw()
