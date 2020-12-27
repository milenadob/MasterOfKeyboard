from PyQt5 import QtWidgets as Qtw
from PyQt5 import QtGui as Qtg


class StatisticsWidget(Qtw.QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = Qtw.QVBoxLayout()
        self.setLayout(layout)


class OptionsWidget(Qtw.QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = Qtw.QVBoxLayout()
        self.setLayout(layout)


class MenuWidget(Qtw.QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.start_button = Qtw.QPushButton('Start')
        self.statistics_button = Qtw.QPushButton('Statistics')
        self.options_button = Qtw.QPushButton('Options')
        self.exit_button = Qtw.QPushButton('Exit')

        menu_layout = Qtw.QVBoxLayout(self)
        menu_layout.addWidget(self.start_button)
        menu_layout.addWidget(self.statistics_button)
        menu_layout.addWidget(self.options_button)
        menu_layout.addWidget(self.exit_button)
        menu_layout.addStretch(1)
        self.setLayout(menu_layout)
        self.setFixedSize(250, 700)


class StartDisplayWidget(Qtw.QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        logo_image = Qtg.QPixmap('resources/keyboard.png')
        self.logo_label = Qtw.QLabel(self)
        self.logo_label.setPixmap(logo_image)

        layout = Qtw.QVBoxLayout()
        layout.addWidget(self.logo_label)
        self.setLayout(layout)


stylesheet = """
QPushButton{
    border-image: url(resources/green_button00.png);
    height: 49px;
    width: 190px;
    margin-left: 15px;
    margin-right: 15px;
    margin-top: 15px;
    
}
QPushButton:pressed{
    border-image: url(resources/green_button01.png);
    height: 45px;
    width: 190px;
}

MenuWindow{
    border-image: url(resources/key.png) 0 0 0 0 stretch stretch ;
}
MenuWidget{
    background-color: rgba(255,255,255,180);
    padding-top: 30px;
}
"""