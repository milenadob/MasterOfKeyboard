from PyQt5.QtWidgets import QApplication, QFrame, QGridLayout, QProgressBar, QVBoxLayout, QLabel, QLineEdit
import sys
from keyboard import KeyboardWidget
from game_logic import GameLogic


class GameWindow(QFrame):

    def __init__(self, file_name, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.game_widget = GameWidget()
        self.game_menu = GameWindowMenu()
        self.game_logic = GameLogic()
        self.game_widget.text_input.textChanged.connect(self.check_text_input)

        window_layout = QGridLayout()
        window_layout.addWidget(self.game_widget, 0, 0)
        window_layout.addWidget(self.game_menu, 0, 1)
        self.setLayout(window_layout)

        self.line_index = 0
        self.progress = 0
        self.data = self.game_logic.load_data(file_name)
        self.lines = len(self.data)
        self.update_label()
        self.game_logic.start_game()

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


class GameWindowMenu(QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(10, 10, 100, 30)

        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)


class GameWidget(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.show_text_label = QLabel()
        self.time_label = QLabel()
        self.text_input = QLineEdit()
        self.keyboard_widget = KeyboardWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.show_text_label)
        layout.addWidget(self.time_label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.keyboard_widget)
        self.setLayout(layout)
        self.setFixedWidth(1100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GameWindow("resources/text.txt")
    window.setWindowTitle("Master of keyboard")
    window.setFixedSize(1500, 800)
    window.show()
    sys.exit(app.exec_())
