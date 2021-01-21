from PyQt5.QtWidgets import QPushButton, QFrame, QGridLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt


class KeyboardWidget(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.key_layout = QGridLayout()
        self.key_table = [['Esc', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Back'],
                     ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
                     ['CapsLk', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'', 'Enter'],
                     ['ShiftL', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'ShiftR'],
                     ['CtrlL', 'WinL', 'AltL', 'Space', 'AltR', 'WinR', 'Menu', 'CtrlR']]
        self.init_keyboard()
        self.setLayout(self.key_layout)

    def init_keyboard(self):
        row = 1
        for tab in self.key_table:
            i = 0
            col = 1
            while i < len(tab):
                button_length = 2
                if tab[i] == 'Back':
                    button_length = 4
                    self.key_layout.addWidget(QPushButton(), row, col, 1, button_length)
                    button = self.key_layout.itemAtPosition(row, col).widget()
                    button.setIcon(QIcon('resources/icons8-clear-symbol-96.png'))
                    button.setIconSize(QSize(24, 24))
                elif tab[i] == 'Tab' or tab[i] == '\\':
                    button_length = 3
                    self.key_layout.addWidget(QPushButton(tab[i]), row, col, 1, button_length)
                elif tab[i] == 'Enter' or tab[i] == 'CapsLk':
                    button_length = 4
                    self.key_layout.addWidget(QPushButton(tab[i]), row, col, 1, button_length)
                elif tab[i] == 'ShiftL' or tab[i] == 'ShiftR':
                    button_length = 5
                    self.key_layout.addWidget(QPushButton(tab[i][:-1]), row, col, 1, button_length)
                elif tab[i] == 'WinL' or tab[i] == 'WinR':
                    self.key_layout.addWidget(QPushButton(), row, col, 1, button_length)
                    button = self.key_layout.itemAtPosition(row, col).widget()
                    button.setIcon(QIcon('resources/icons8-windows-10-96.png'))
                    button.setIconSize(QSize(24, 24))
                elif tab[i] == 'Menu':
                    self.key_layout.addWidget(QPushButton(), row, col, 1, button_length)
                    button = self.key_layout.itemAtPosition(row, col).widget()
                    button.setIcon(QIcon('resources/icons8-menu-squared-96.png'))
                    button.setIconSize(QSize(24, 24))
                elif tab[i] == 'Space':
                    button_length = 16
                    self.key_layout.addWidget(QPushButton(), row, col, 1, button_length)
                elif tab[i] == 'CtrlL' or tab[i] == 'CtrlR' or tab[i] == 'AltL' or tab[i] == 'AltR':
                    self.key_layout.addWidget(QPushButton(tab[i][:-1]), row, col, 1, button_length)
                else:
                    self.key_layout.addWidget(QPushButton(tab[i]), row, col, 1, button_length)
                self.add_keys_shadow(row, col)
                button = self.key_layout.itemAtPosition(row, col).widget()
                button.setAccessibleName(tab[i])
                col += button_length
                i += 1
            row += 1

    def add_keys_shadow(self, row, col):
        button = self.key_layout.itemAtPosition(row, col).widget()
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(Qt.darkCyan)
        shadow.setOffset(4, 4)
        button.setGraphicsEffect(shadow)

    def check_key_pressed(self, key):
        items = [self.key_layout.itemAt(i).widget() for i in range(self.key_layout.count())]
        for button in items:
            if key == Qt.Key_Backspace:
                if button.text() == 'Back':
                    return button
            elif key == Qt.Key_Tab:
                if button.text() == 'Tab':
                    return button
            elif key == Qt.Key_Enter:
                return self.key_layout.findChild(QPushButton, "Enter")
            # elif key == Qt.Key_Shift:
            #    if button.text() == 'Shift':
            #        return button
            elif key == Qt.Key_CapsLock:
                if button.text() == 'CapsLk':
                    return button
            elif key == Qt.Key_Space:
                if button.text() == 'Space':
                    return button
            # elif key == Qt.Key_Alt:
            #     if button.text() == 'Alt':
            #         return button
            # elif key == Qt.Key_Control:
            #     if button.text() == 'Ctrl':
            #         return button
            elif len(button.text()) == 1 and ord(button.text()) == key:
                return button

    def change_to_button_pressed_style(self, button):
        if button is not None:
            button.setStyleSheet("background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 rgba(240,213,255,180), stop:1 rgba(181,238,255,180));")


    def change_to_button_normal_style(self, button):
        if button is not None:
            button.setStyleSheet("background-color: rgba(255,255,255,0));")
