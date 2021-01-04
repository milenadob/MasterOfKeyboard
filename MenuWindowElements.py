from PyQt5 import QtWidgets as Qtw
from PyQt5 import QtGui as Qtg


class StatisticsWidget(Qtw.QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = Qtw.QVBoxLayout()
        self.setLayout(layout)

        self.setFrameStyle(Qtw.QFrame.Panel | Qtw.QFrame.Raised)
        self.setFixedSize(1100, 750)


class OptionsWidget(Qtw.QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.file_choosing_label = Qtw.QLabel(self)
        self.file_choosing_label.setText('Choose text you want to write')
        self.file_choosing_button = Qtw.QPushButton('Choose File')
        self.file_chosen_display_label = Qtw.QLabel(self)
        self.file_chosen_display_label.setProperty("cssClass", "display")

        layout = Qtw.QVBoxLayout()
        layout.addWidget(self.file_choosing_label)
        layout.addWidget(self.file_choosing_button)
        layout.addWidget(self.file_chosen_display_label)
        self.setLayout(layout)

        self.setFrameStyle(Qtw.QFrame.Panel | Qtw.QFrame.Raised)
        self.setFixedSize(1100, 750)


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

        self.setFrameStyle(Qtw.QFrame.Panel | Qtw.QFrame.Raised)
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
    border-image: url(resources/blue_button00.png);
    height: 49px;
    width: 190px;
    max-height: 49px;
    max-width: 190px;
    margin-left: 15px;
    margin-right: 15px;
    margin-top: 15px;
    color: white;  
    font-size: 18px;
}
QPushButton:pressed{
    border-image: url(resources/blue_button01.png);
    height: 45px;
    width: 190px;
}
OptionsWidget QLabel{
    font-size: 20px;
    max-height: 60px;
    margin-left: 15px;
    margin-right: 15px;
    
}
QLabel[cssClass = 'display']{
    border-image: url(resources/blue_button13.png);
    max-width: 400px;
    
    padding-left: 10px;
}
MenuWindow{
    border-image: url(resources/key.png) 0 0 0 0 stretch stretch ;
}
MenuWidget{
    background-color: rgba(255,255,255,180);
    padding-top: 30px;
}
OptionsWidget, StatisticsWidget{
    background-color: rgba(255,255,255,180);
    margin-top: 35px;
    margin-left: 100px;
}
"""