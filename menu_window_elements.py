from PyQt5 import QtWidgets as Qtw
from PyQt5 import QtGui as Qtg
from PyQt5 import QtCore as Qtc


class StatisticsWidget(Qtw.QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = Qtw.QVBoxLayout()
        self.setLayout(layout)

        # self.setFrameStyle(Qtw.QFrame.Panel | Qtw.QFrame.Raised)
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

        # self.setFrameStyle(Qtw.QFrame.Panel | Qtw.QFrame.Raised)
        self.setFixedSize(1100, 750)


class MenuWidget(Qtw.QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.start_button = Qtw.QPushButton('    Start')
        self.start_button.setIcon(Qtg.QIcon('resources/icons8-play-96.png'))
        self.start_button.setIconSize(Qtc.QSize(50, 50))
        self.statistics_button = Qtw.QPushButton(' Statistics')
        self.statistics_button.setIcon(Qtg.QIcon('resources/icons8-increase-96.png'))
        self.statistics_button.setIconSize(Qtc.QSize(50, 50))
        self.options_button = Qtw.QPushButton('  Options')
        self.options_button.setIcon(Qtg.QIcon('resources/icons8-settings-96.png'))
        self.options_button.setIconSize(Qtc.QSize(50, 50))
        self.exit_button = Qtw.QPushButton('     Exit')
        self.exit_button.setIcon(Qtg.QIcon('resources/icons8-delete-96.png'))
        self.exit_button.setIconSize(Qtc.QSize(50, 50))

        shadow1 = Qtw.QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(15)
        shadow2 = Qtw.QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(15)
        shadow3 = Qtw.QGraphicsDropShadowEffect()
        shadow3.setBlurRadius(15)
        shadow4 = Qtw.QGraphicsDropShadowEffect()
        shadow4.setBlurRadius(15)
        self.start_button.setGraphicsEffect(shadow1)
        self.statistics_button.setGraphicsEffect(shadow2)
        self.options_button.setGraphicsEffect(shadow3)
        self.exit_button.setGraphicsEffect(shadow4)

        menu_layout = Qtw.QVBoxLayout(self)
        menu_layout.addWidget(self.start_button)
        menu_layout.addWidget(self.statistics_button)
        menu_layout.addWidget(self.options_button)
        menu_layout.addWidget(self.exit_button)
        self.setLayout(menu_layout)

        # self.setFrameStyle(Qtw.QFrame.Panel | Qtw.QFrame.Raised)
        self.setFixedSize(250, 750)
