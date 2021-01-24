from PyQt5.QtWidgets import QFrame, QGridLayout, QProgressBar, QVBoxLayout, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt, QTimer, QTime, QThread
from keyboard import KeyboardWidget
from game_logic import GameLogic


class GameWindow(QFrame):

    def __init__(self, file_name, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.game_logic = GameLogic()
        self.data = self.game_logic.load_data(file_name)
        self.prepared_data = []
        self.prepare_data()
        self.game_menu = GameWindowMenu(self.data)
        self.game_widget = GameWidget(self.prepared_data, self.game_menu)

        window_layout = QGridLayout()
        window_layout.addWidget(self.game_widget, 0, 0)
        window_layout.addWidget(self.game_menu, 0, 1)
        self.setLayout(window_layout)

        self.game_logic.start_game()

    def prepare_data(self):
        if len(self.data) % 3 == 2:
            self.data.append("")
        elif len(self.data) % 3 == 1:
            self.data.append("")
            self.data.append("")
        self.prepared_data = ([(self.data[i], self.data[i+1], self.data[i+2]) for i in range(0, len(self.data), 3)])


class GameWindowMenu(QFrame):

    def __init__(self, data, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(10, 10, 100, 30)

        self.data = data
        self.progress_total = 0
        self.progress_step = 1
        self.characters_to_progress = 1
        self.progress = 0
        self.error_label = QLabel()
        self.clock = QLCDNumber()

        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.error_label)
        layout.addWidget(self.clock)
        self.setLayout(layout)
        self.calculate_progress_step()

        self.timer = TimerThread(self)
        self.timer.start()

    def calculate_progress_step(self):
        self.progress_total = sum(len(i) for i in self.data)
        characters_per_step = round(self.progress_total / 100)
        progress_per_character = round(100 / self.progress_total)
        if characters_per_step > progress_per_character:
            self.characters_to_progress = characters_per_step
        else:
            self.progress_step = progress_per_character

    def set_progress_bar(self, forward):
        if forward:
            self.progress_bar.setValue(self.progress + self.progress_step)
            self.progress += self.progress_step
        else:
            self.progress_bar.setValue(self.progress - self.progress_step)
            self.progress -= self.progress_step


class TimerThread(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.game_time_miliseconds = 0

    def run(self):
        timer = QTimer()
        timer.timeout.connect(self.update_time_label)
        timer.start(100)
        self.exec_()

    def update_time_label(self):
        self.game_time_miliseconds += 1
        time_show = f"{int(self.game_time_miliseconds/10)}:{self.game_time_miliseconds % 10}"
        self.parent().clock.display(time_show)


class GameWidget(QFrame):
    def __init__(self, data, menu, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data = data
        self.game_menu = menu
        self.data1, self.data2, self.data3 = zip(*self.data)

        self.show_text_label = QLabel()
        self.show_text_label2 = QLabel()
        self.show_text_label3 = QLabel()

        self.text_input = CustomLineEdit()
        self.text_input.returnPressed.connect(self.change_text_input2)
        self.text_input.textChanged.connect(self.check_text_input)
        self.text_input2 = CustomLineEdit()
        self.text_input2.returnPressed.connect(self.change_text_input3)
        self.text_input2.textChanged.connect(self.check_text_input)
        self.text_input3 = CustomLineEdit()
        self.text_input3.returnPressed.connect(self.change_text_input)
        self.text_input3.textChanged.connect(self.check_text_input)

        container = QFrame()
        container.setObjectName("text_input_frame")
        entry_layout = QVBoxLayout()
        entry_layout.addWidget(self.show_text_label)
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

        self.line_index = 0
        self.good_characters = 0
        self.bad_characters = 0
        self.deleted_characters = 0
        self.inputs_text_len = 0
        self.all_inputs_text_len = 0
        self.previous_progress = 0
        self.errors = 0

        self.update_label()

    def change_text_input(self):
        self.inputs_text_len = 0
        self.previous_progress = self.game_menu.progress

        if (len(self.text_input.text()) == len(self.data1[self.line_index]) and
                self.text_input.text() in self.data1[self.line_index] and
                len(self.text_input2.text()) == len(self.data2[self.line_index]) and
                self.text_input2.text() in self.data2[self.line_index] and
                len(self.text_input3.text()) == len(self.data3[self.line_index]) and
                self.text_input3.text() in self.data3[self.line_index]):

            self.line_index += 1
            self.update_label()
            self.text_input.setFocus()
            self.text_input.clear()
            self.text_input2.clear()
            self.text_input3.clear()
        if self.data1[self.line_index] == "":
            self.game_menu.progress_bar.setValue(100)
            self.game_menu.error_label.setText("Errors: " + str(self.errors))

    def change_text_input2(self):
        if (len(self.text_input.text()) == len(self.data1[self.line_index]) and
                self.text_input.text() in self.data1[self.line_index]):
            self.inputs_text_len = 0
            self.previous_progress = self.game_menu.progress
            self.text_input2.setFocus()

    def change_text_input3(self):
        if (len(self.text_input2.text()) == len(self.data2[self.line_index]) and
                self.text_input2.text() in self.data2[self.line_index]):
            self.inputs_text_len = 0
            self.previous_progress = self.game_menu.progress
            self.text_input3.setFocus()

    def update_label(self):
        value1 = self.data1[self.line_index]
        self.show_text_label.setText(value1)

        value2 = self.data2[self.line_index]
        self.show_text_label2.setText(value2)

        value3 = self.data3[self.line_index]
        self.show_text_label3.setText(value3)

    def check_text_input(self, text):
        self.text_input.setStyleSheet('color:rgba(112,112,165,180);')
        self.text_input2.setStyleSheet('color:rgba(112,112,165,180);')
        self.text_input3.setStyleSheet('color:rgba(112,112,165,180);')

        if text != "":
            if self.sender() is self.text_input:
                if text not in self.data1[self.line_index]:
                    self.text_input.setStyleSheet('color:red')
                    self.bad_characters += 1
                    self.errors += 1
                else:
                    self.good_characters += 1
            if self.sender() is self.text_input2:
                if text not in self.data2[self.line_index]:
                    self.text_input2.setStyleSheet('color:red')
                    self.bad_characters += 1
                    self.errors += 1
                else:
                    self.good_characters += 1
            if self.sender() is self.text_input3:
                if text not in self.data3[self.line_index]:
                    self.text_input3.setStyleSheet('color:red')
                    self.bad_characters += 1
                    self.errors += 1
                else:
                    self.good_characters += 1
            self.inputs_text_len += 1

            if len(text) < self.inputs_text_len:
                self.inputs_text_len -= 2
                self.deleted_characters += 1
                if self.bad_characters > 1:
                    self.deleted_characters = 0
                    self.errors -= 1
                    self.bad_characters -= 2
                elif self.bad_characters == 1:
                    self.bad_characters = 0
                    self.deleted_characters = 0
                    self.good_characters -= 1
                if self.deleted_characters == self.game_menu.characters_to_progress:
                    self.game_menu.set_progress_bar(False)
                    self.deleted_characters = 0
                    self.good_characters = 0
                if len(text) == 1:
                    self.inputs_text_len = 0
                    self.deleted_characters = 0
                    self.good_characters = 0
                    self.game_menu.progress_bar.setValue(self.previous_progress)
                    self.game_menu.progress = self.previous_progress

            elif self.good_characters == self.game_menu.characters_to_progress:
                self.game_menu.set_progress_bar(True)
                self.good_characters = 0


class CustomLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_key = []

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if int(a0.modifiers()) & Qt.ShiftModifier:
            shift_pressed = True
        else:
            shift_pressed = False
        button = self.parent().parent().keyboard_widget.check_key_pressed(a0.key(), a0.nativeScanCode(), shift_pressed)
        self.parent().parent().keyboard_widget.change_to_button_pressed_style(button)
        [self.parent().parent().keyboard_widget.change_to_button_normal_style(
            self.parent().parent().keyboard_widget.check_key_pressed(i[0], i[1], i[2]))
            for i in self.last_key if i[1] != a0.nativeScanCode()]
        self.last_key.clear()
        super(CustomLineEdit, self).keyPressEvent(a0)

    def keyReleaseEvent(self, a0: QKeyEvent) -> None:
        if int(a0.modifiers()) & Qt.ShiftModifier:
            last_shift = True
        else:
            last_shift = False
        self.last_key.append((a0.key(), a0.nativeScanCode(), last_shift))
        super(CustomLineEdit, self).keyReleaseEvent(a0)

