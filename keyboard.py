from PyQt5.QtWidgets import QPushButton, QFrame, QGridLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon, QColor
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
        self.shift_pressed = [('1', '!'), ('2', '@'), ('3', '#'), ('4', '$'), ('5', '%'), ('6', '^'), ('7', '&'),
                              ('8', '*'), ('9', '('), ('0', ')'), ('-', '_'), ('=', '+'), ('[', '{'), (']', '}'),
                              ('\\', '|'), (';', ':'), ('\'', '\"'), (',', '<'), ('.', '>'), ('/', '?')]
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
                button.setObjectName(tab[i])
                col += button_length
                i += 1
            row += 1

    def add_keys_shadow(self, row, col):
        button = self.key_layout.itemAtPosition(row, col).widget()
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(3)
        shadow.setColor(QColor.fromRgb(112, 122, 170))
        shadow.setOffset(2, 3)
        button.setGraphicsEffect(shadow)

    def check_key_pressed(self, key, sc, shift_pressed):
        if key == Qt.Key_Backspace:
            return self.findChild(QPushButton, 'Back')
        elif key == Qt.Key_Escape:
            return self.findChild(QPushButton, 'Esc')
        elif key == 16777220:
            return self.findChild(QPushButton, 'Enter')
        elif sc == 42:
            return self.findChild(QPushButton, 'ShiftL')
        elif sc == 54:
            return self.findChild(QPushButton, 'ShiftR')
        elif key == Qt.Key_CapsLock:
            return self.findChild(QPushButton, 'CapsLk')
        elif key == Qt.Key_Space:
            return self.findChild(QPushButton, 'Space')
        elif sc == 56:
            return self.findChild(QPushButton, 'AltL')
        elif sc == 312:
            return self.findChild(QPushButton, 'AltR')
        elif sc == 29:
            return self.findChild(QPushButton, 'CtrlL')
        elif sc == 285:
            return self.findChild(QPushButton, 'CtrlR')
        elif key == Qt.Key_Menu:
            return self.findChild(QPushButton, 'Menu')
        elif key == Qt.Key_Meta:
            return self.findChild(QPushButton, 'WinL')
        elif shift_pressed and (key in range(33, 65) or key in range(91, 97) or key in range(123, 126)):
            key_without_shift = [i[0] for i in self.shift_pressed if i[1] == chr(key)]
            return self.findChild(QPushButton, key_without_shift[0])
        else:
            return self.findChild(QPushButton, chr(key))

    def change_to_button_pressed_style(self, button):
        if button is not None:
            button.setStyleSheet("""background-color: 
            qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 rgba(240,213,255,180), stop:1 rgba(181,238,255,180));""")

    def change_to_button_normal_style(self, button):
        if button is not None:
            button.setStyleSheet("background-color: rgba(255,255,255,255);")
