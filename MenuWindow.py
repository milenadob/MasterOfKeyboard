from PyQt5 import QtWidgets as Qtw
from PyQt5 import QtGui as Qtg
import sys
from MenuWindowElements import StatisticsWidget, OptionsWidget, MenuWidget, stylesheet, StartDisplayWidget
from GameWindow import GameWindow


class MenuWindow(Qtw.QFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.stack = Qtw.QStackedWidget(self)
        self.stack1 = StartDisplayWidget()
        self.stack2 = StatisticsWidget()
        self.stack3 = OptionsWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        self.game_window = None
        self.leftMenu = MenuWidget()
        self.leftMenu.setFrameStyle(Qtw.QFrame.Panel | Qtw.QFrame.Raised)
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
        self.game_window = GameWindow()
        self.game_window.setFixedSize(500, 500)
        self.game_window.show()
        self.close()


if __name__ == '__main__':
    app = Qtw.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    window = MenuWindow()
    window.setWindowTitle("Master of keyboard")
    window.setFixedSize(1500, 800)
    window.setWindowIcon(Qtg.QIcon('resources/keyboard.png'))
    sys.exit(app.exec_())
