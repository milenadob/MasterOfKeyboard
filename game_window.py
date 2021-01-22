from PyQt5.QtWidgets import QApplication, QFrame, QGridLayout, QProgressBar, QVBoxLayout, QLabel, QLineEdit
from PyQt5 import QtGui, QtCore
import sys
from keyboard import KeyboardWidget
from game_logic import GameLogic
from threading import Timer


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
        self.game_widget.text_input.setStyleSheet('color:rgba(112,112,165,180);')

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
        self.show_text_label2 = QLabel()
        self.text_input2 = CustomLineEdit()
        self.text_input2.returnPressed.connect(self.change_text_input3)
        self.show_text_label3 = QLabel()
        self.text_input3 = CustomLineEdit()
        self.text_input3.returnPressed.connect(self.change_text_input)

        container = QFrame()
        container.setObjectName("text_input_frame")
        entry_layout = QVBoxLayout()
        entry_layout.addWidget(self.show_text_label)
        entry_layout.addWidget(self.time_label)
        entry_layout.addWidget(self.text_input)
        entry_layout.addWidget(self.show_text_label2)
        entry_layout.addWidget(self.text_input2)
        entry_layout.addWidget(self.show_text_label3)
        entry_layout.addWidget(self.text_input3)
        container.setLayout(entry_layout)

        self.keyboard_widget = KeyboardWidget()

        layout = QVBoxLayout()
        layout.addWidget(container)
        layout.addWidget(self.keyboard_widget)
        self.setLayout(layout)
        self.setFixedWidth(1100)

    def change_text_input2(self):
        self.text_input2.setFocus()

    def change_text_input3(self):
        self.text_input3.setFocus()

    def change_text_input(self):
        self.text_input.setFocus()


class CustomLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_key = []

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if not a0.isAutoRepeat():
            print(a0.key())
            button = self.parent().parent().keyboard_widget.check_key_pressed(a0.key())
            self.parent().parent().keyboard_widget.change_to_button_pressed_style(button)
            [self.parent().parent().keyboard_widget.change_to_button_normal_style(
                self.parent().parent().keyboard_widget.check_key_pressed(i)) for i in self.last_key
                if i != a0.key()]
            self.last_key.clear()
        super(CustomLineEdit, self).keyPressEvent(a0)

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        if not a0.isAutoRepeat():
            self.last_key.append(a0.key())
        super(CustomLineEdit, self).keyReleaseEvent(a0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GameWindow("resources/text.txt")
    window.setWindowTitle("Master of keyboard")
    window.setFixedSize(1500, 800)
    window.show()
    sys.exit(app.exec_())
