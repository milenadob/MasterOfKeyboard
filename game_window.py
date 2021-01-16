from PyQt5 import QtWidgets as Qtw
from PyQt5 import QtCore as Qtc
import sys
from game_logic import GameLogic


class GameWindow(Qtw.QFrame):

    def __init__(self, file_name, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowFlag(Qtc.Qt.FramelessWindowHint)
        self.setAttribute(Qtc.Qt.WA_TranslucentBackground, True)

        self.game_widget = GameWidget()
        self.game_widget.text_input.textChanged.connect(self.check_text_input)
        self.game_menu = GameWindowMenu()

        window_layout = Qtw.QGridLayout()
        window_layout.addWidget(self.game_widget, 0, 0)
        window_layout.addWidget(self.game_menu, 0, 1)
        self.setLayout(window_layout)

        self.line_index = 0
        self.data = []
        self.file_name = file_name
        self.lines = 0
        self.progress = 0
        self.load_data()
        self.game_logic = GameLogic()
        self.game_logic.start_game()

    def load_data(self):
        with open(self.file_name, 'r') as f:
            self.data = f.readlines()
        self.data = [line.rstrip('\n') for line in self.data]
        self.lines = len(self.data)
        self.update_label()

    def update_label(self):
        value = self.data[self.line_index]
        self.game_widget.show_text_label.setText(value)

        if self.line_index + 1 == self.lines:
            self.game_menu.progress_bar.setValue(100)
            self.game_logic.end_game()
            self.game_widget.time_label.setText(str(self.game_logic.total_time))
        elif self.line_index == 0:
            self.game_menu.progress_bar.setValue(0)
        else:
            self.progress += int(100 / self.lines)
            self.game_menu.progress_bar.setValue(self.progress)

    def check_text_input(self, text):
        self.game_widget.text_input.setStyleSheet('color:black')
        if text != "":
            if text in self.data[self.line_index]:
                if len(text) == len(self.data[self.line_index]):
                    self.line_index = self.line_index + 1
                    self.update_label()
                    self.game_widget.text_input.clear()
            else:
                self.game_widget.text_input.setStyleSheet('color:red')


class GameWindowMenu(Qtw.QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.progress_bar = Qtw.QProgressBar(self)
        self.progress_bar.setGeometry(10, 10, 100, 30)

        layout = Qtw.QVBoxLayout()
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)


class GameWidget(Qtw.QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.show_text_label = Qtw.QLabel()
        self.time_label = Qtw.QLabel()
        self.text_input = Qtw.QLineEdit()
        layout = Qtw.QVBoxLayout()
        layout.addWidget(self.show_text_label)
        layout.addWidget(self.time_label)
        layout.addWidget(self.text_input)
        self.setLayout(layout)
        self.setFixedSize(1200, 800)


if __name__ == '__main__':
    app = Qtw.QApplication(sys.argv)
    window = GameWindow("resources/text.txt")
    window.setWindowTitle("Master of keyboard")
    window.setFixedSize(1500, 800)
    window.show()
    sys.exit(app.exec_())
