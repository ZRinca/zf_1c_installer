from design_core import InstallerWindow


def any_function(global_config):
    global_config['test2'] = 'shpek'


class HelloWindow(InstallerWindow):
    draw_back_button = False
    header_text = 'Приветствую!'
    body_text = ('При нажатии на кнопку «Далее» вы принимаете условия лицензионного соглашения.'
                 'Это \n значает, что вы соглашаетесь с правилами использования программного '
                 'обеспечения или'
                 '\nдругого продукта, предоставляемого вам.')

    def draw(self):
        super().draw()
