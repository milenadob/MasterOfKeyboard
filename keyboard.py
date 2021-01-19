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
                     ['Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Shift'],
                     ['Ctrl', 'Win', 'Alt', 'Space', 'Alt', 'Win', 'Menu', 'Ctrl']]
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
                elif tab[i] == 'Shift':
                    button_length = 5
                    self.key_layout.addWidget(QPushButton(tab[i]), row, col, 1, button_length)
                elif tab[i] == 'Win':
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
                else:
                    self.key_layout.addWidget(QPushButton(tab[i]), row, col, 1, button_length)
                self.add_keys_shadow(row, col)
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



