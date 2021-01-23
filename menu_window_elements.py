from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout, QPushButton, QGraphicsDropShadowEffect
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon


class StatisticsWidget(QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # self.setFrameStyle(Qtw.QFrame.Panel | Qtw.QFrame.Raised)
        self.setFixedSize(1100, 750)


class OptionsWidget(QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.file_choosing_label = QLabel(self)
        self.file_choosing_label.setText('Choose text you want to write')
        self.file_choosing_button = QPushButton('Choose File')
        self.file_chosen_display_label = QLabel(self)
        self.file_chosen_display_label.setProperty("cssClass", "display")

        layout = QVBoxLayout()
        layout.addWidget(self.file_choosing_label)
        layout.addWidget(self.file_choosing_button)
        layout.addWidget(self.file_chosen_display_label)
        self.setLayout(layout)

        # self.setFrameStyle(Qtw.QFrame.Panel | Qtw.QFrame.Raised)
        self.setFixedSize(1100, 750)


class MenuWidget(QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.start_button = QPushButton('    Start')
        self.start_button.setIcon(QIcon('resources/icons8-play-96.png'))
        self.start_button.setIconSize(QSize(50, 50))
        self.statistics_button = QPushButton(' Statistics')
        self.statistics_button.setIcon(QIcon('resources/icons8-increase-96.png'))
        self.statistics_button.setIconSize(QSize(50, 50))
        self.options_button = QPushButton('  Options')
        self.options_button.setIcon(QIcon('resources/icons8-settings-96.png'))
        self.options_button.setIconSize(QSize(50, 50))
        self.exit_button = QPushButton('     Exit')
        self.exit_button.setIcon(QIcon('resources/icons8-delete-96.png'))
        self.exit_button.setIconSize(QSize(50, 50))

        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(15)
        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(15)
        shadow3 = QGraphicsDropShadowEffect()
        shadow3.setBlurRadius(15)
        shadow4 = QGraphicsDropShadowEffect()
        shadow4.setBlurRadius(15)
        self.start_button.setGraphicsEffect(shadow1)
        self.statistics_button.setGraphicsEffect(shadow2)
        self.options_button.setGraphicsEffect(shadow3)
        self.exit_button.setGraphicsEffect(shadow4)

        menu_layout = QVBoxLayout(self)
        menu_layout.addWidget(self.start_button)
        menu_layout.addWidget(self.statistics_button)
        menu_layout.addWidget(self.options_button)
        menu_layout.addWidget(self.exit_button)
        self.setLayout(menu_layout)

        # self.setFrameStyle(Qtw.QFrame.Panel | Qtw.QFrame.Raised)
        self.setFixedSize(250, 750)
