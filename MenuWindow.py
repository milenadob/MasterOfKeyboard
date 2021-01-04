from PyQt5 import QtWidgets as Qtw
from PyQt5 import QtGui as Qtg
import sys
from MenuWindowElements import StatisticsWidget, OptionsWidget, MenuWidget, stylesheet, StartDisplayWidget
from GameWindow import GameWindow


class MenuWindow(Qtw.QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.stack = Qtw.QStackedWidget(self)
        self.stack1_start = StartDisplayWidget()
        self.stack2_statistics = StatisticsWidget()
        self.stack3_options = OptionsWidget()
        self.stack.addWidget(self.stack1_start)
        self.stack.addWidget(self.stack2_statistics)
        self.stack.addWidget(self.stack3_options)
        self.stack3.file_choosing_button.clicked.connect(self.get_text_file)

        self.file_name = "resources/text.txt"        # default
        self.stack3_options.file_chosen_display_label.setText('Chosen file: ' + self.file_name)
        self.game_window = None

        self.leftMenu = MenuWidget()
        self.leftMenu.start_button.clicked.connect(self.open_game_window)
        self.leftMenu.statistics_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.stack2))
        self.leftMenu.options_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.stack3))
        self.leftMenu.exit_button.clicked.connect(self.close)

        window_layout = Qtw.QGridLayout()
        window_layout.addWidget(self.leftMenu, 0, 0)
        window_layout.addWidget(self.stack, 0, 1)
        self.setLayout(window_layout)
        self.show()

    def open_game_window(self):
        self.game_window = GameWindow(self.file_name)
        self.game_window.setFixedSize(500, 500)
        self.game_window.show()
        self.close()

    def get_text_file(self):
        self.file_name, _ = Qtw.QFileDialog.getOpenFileName(self, 'Open file', 'C:\\', "Text files (*.txt)")
        self.stack3_options.file_chosen_display_label.setText('Chosen file: ' + self.file_name)


if __name__ == '__main__':
    app = Qtw.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    window = MenuWindow()
    window.setWindowTitle("Master of keyboard")
    window.setFixedSize(1500, 800)
    window.setWindowIcon(Qtg.QIcon('resources/keyboard.png'))
    sys.exit(app.exec_())
