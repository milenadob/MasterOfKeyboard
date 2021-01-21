from PyQt5.QtWidgets import QApplication, QFrame, QGridLayout, QProgressBar, QVBoxLayout, QLabel, QLineEdit
from PyQt5 import QtGui, QtCore
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
        self.game_widget.text_input2.textChanged.connect(self.check_text_input)
        self.game_widget.text_input3.textChanged.connect(self.check_text_input)

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

        self.game_widget.keyboard_widget.change_to_button_pressed_style(
            self.game_widget.keyboard_widget.check_key_pressed(self.game_widget.keypressed))
        [self.game_widget.keyboard_widget.change_to_button_normal_style(
            self.game_widget.keyboard_widget.check_key_pressed(i)) for i in self.game_widget.lastkey
            if i != self.game_widget.keypressed]
        self.game_widget.lastkey.clear()

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
        self.text_input = CustomLineEdit()
        self.text_input.returnPressed.connect(self.change_text_input2)
        self.time_label2 = QLabel()
        self.text_input2 = CustomLineEdit()
        self.text_input2.returnPressed.connect(self.change_text_input3)
        self.time_label3 = QLabel()
        self.text_input3 = CustomLineEdit()
        self.text_input3.returnPressed.connect(self.change_text_input)
        self.keyboard_widget = KeyboardWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.show_text_label)
        layout.addWidget(self.time_label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.time_label2)
        layout.addWidget(self.text_input2)
        layout.addWidget(self.time_label3)
        layout.addWidget(self.text_input3)
        layout.addWidget(self.keyboard_widget)
        self.setLayout(layout)
        self.setFixedWidth(1100)

        self.keypressed = None
        self.lastkey = []

    def change_text_input2(self):
        self.text_input2.setFocus()

    def change_text_input3(self):
        self.text_input3.setFocus()

    def change_text_input(self):
        self.text_input.setFocus()


class CustomLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if not a0.isAutoRepeat():
            self.parent().keypressed = a0.key()
        super(CustomLineEdit, self).keyPressEvent(a0)

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        if not a0.isAutoRepeat():
            self.parent().lastkey.append(a0.key())
        super(CustomLineEdit, self).keyReleaseEvent(a0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GameWindow("resources/text.txt")
    window.setWindowTitle("Master of keyboard")
    window.setFixedSize(1500, 800)
    window.show()
    sys.exit(app.exec_())
