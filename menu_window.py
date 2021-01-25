# icons used in application comes from site icon8.com
from PyQt5.QtWidgets import (QFrame, QWidget, QStackedWidget, QGridLayout, QDesktopWidget, QApplication, QFileDialog,
                             QVBoxLayout, QPushButton, QLabel, QGraphicsDropShadowEffect)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import sys
from stylesheet import stylesheet
from game_window import GameWindow


class MenuWindow(QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.setWindowFlag(Qtc.Qt.FramelessWindowHint)
        # self.setAttribute(Qtc.Qt.WA_TranslucentBackground, True)
        self.stack = QStackedWidget(self)
        self.stack1_start = QWidget()
        self.stack2_statistics = StatisticsWidget()
        self.stack3_options = OptionsWidget()
        self.stack.addWidget(self.stack1_start)
        self.stack.addWidget(self.stack2_statistics)
        self.stack.addWidget(self.stack3_options)
        self.stack3_options.file_choosing_button.clicked.connect(self.get_text_file)

        self.file_name = ""
        self.game_window = None

        self.left_menu = MenuWidget()
        self.left_menu.start_button.clicked.connect(self.open_game_window)
        self.left_menu.statistics_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.stack2_statistics))
        self.left_menu.options_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.stack3_options))
        self.left_menu.exit_button.clicked.connect(self.close)

        window_layout = QGridLayout()
        window_layout.addWidget(self.left_menu, 0, 0)
        window_layout.addWidget(self.stack, 0, 1)
        self.setLayout(window_layout)
        self.show()

    def open_game_window(self):
        if self.file_name == "":
            self.file_name = "resources/text.txt"        # default
        self.game_window = GameWindow(self.file_name)
        sizeObject = QDesktopWidget().screenGeometry(0)
        self.game_window.setGeometry(sizeObject.width() // 2 - 800, sizeObject.height() // 2 - 400, 1500, 800)
        self.game_window.setFixedSize(1500, 800)
        self.game_window.setWindowIcon(QIcon('resources/icons8-keyboard-96.png'))
        self.game_window.setWindowTitle("Master of keyboard")
        self.game_window.show()
        self.close()

    def get_text_file(self):
        self.file_name, _ = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\', "Text files (*.txt)")
        self.stack3_options.file_chosen_display_label.setText('Chosen file: ' + self.file_name)


class StatisticsWidget(QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.setLayout(layout)
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
        self.setFixedSize(250, 750)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sizeObject = QDesktopWidget().screenGeometry(0)
    app.setStyleSheet(stylesheet)
    window = MenuWindow()
    window.setWindowTitle("Master of keyboard")
    window.setFixedSize(1500, 800)
    window.setGeometry(sizeObject.width()//2 - 800, sizeObject.height()//2 - 400, 1500, 800)
    window.setWindowIcon(QIcon('resources/icons8-keyboard-96.png'))
    sys.exit(app.exec_())
