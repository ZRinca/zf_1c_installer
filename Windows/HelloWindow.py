from design_core import InstallerWindow


def any_function(global_config):
    global_config['test2'] = 'shpek'


class HelloWindow(InstallerWindow):
    draw_back_button = False
    header_text = 'Мастер настройки ZeroFactor'
    body_text = ('Мастер настройки ZeroFactor поможет вам быстро настроить 1С и связать вашу информационную\nбазу с ZeroFactor'
                 'Подробнее о ZeroFactor, его компонентах и технических особенностях, можно \nузнать на сайте: zerofactor.ru'
                 '\n\nПри продолжении установки и/или использовании продукта (в т.ч. его компонентов) вы \nсоглашаетесь с документами,'
                 ' размещёнными на сайте zerofactor.ru.')

    def draw(self):
        super().draw()
