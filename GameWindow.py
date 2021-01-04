from PyQt5 import QtWidgets as Qtw
import sys


class GameWindow(Qtw.QFrame):

    def __init__(self, file_name, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.progress_bar = Qtw.QProgressBar(self)
        self.progress_bar.setGeometry(10, 10, 200, 30)
        self.show_text_label = Qtw.QLabel()
        self.text_input = Qtw.QLineEdit()
        self.text_input.textChanged.connect(self.check_text_input)

        layout = Qtw.QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.show_text_label)
        layout.addWidget(self.text_input)
        self.setLayout(layout)

        self.line_index = 0
        self.data = []
        self.file_name = file_name
        self.lines = 0
        self.progress = 0
        self.load_data()

    def load_data(self):
        with open(self.file_name, 'r') as f:
            self.data = f.readlines()
        self.data = [line.rstrip('\n') for line in self.data]
        self.lines = len(self.data)
        self.update_label()

    def update_label(self):
        value = self.data[self.line_index]
        self.show_text_label.setText(value)

        if self.line_index + 1 == self.lines:
            self.progress_bar.setValue(100)
        elif self.line_index == 0:
            self.progress_bar.setValue(0)
        else:
            self.progress += int(100 / self.lines)
            self.progress_bar.setValue(self.progress)

    def check_text_input(self, text):
        self.text_input.setStyleSheet('color:black')
        if text != "":
            if text in self.data[self.line_index]:
                if len(text) == len(self.data[self.line_index]):
                    self.line_index = self.line_index + 1
                    self.update_label()
                    self.text_input.clear()
            else:
                self.text_input.setStyleSheet('color:red')


if __name__ == '__main__':
    app = Qtw.QApplication(sys.argv)
    window = GameWindow("resources/text.txt")
    window.setWindowTitle("Master of keyboard")
    window.setFixedSize(1500, 800)
    window.show()
    sys.exit(app.exec_())
