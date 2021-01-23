# icons used in application comes from site icon8.com
from PyQt5.QtWidgets import QFrame, QWidget, QStackedWidget, QGridLayout, QDesktopWidget, QApplication, QFileDialog
from PyQt5.QtGui import QIcon
import sys
from menu_window_elements import StatisticsWidget, OptionsWidget, MenuWidget
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
