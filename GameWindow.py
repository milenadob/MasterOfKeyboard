from PyQt5 import QtWidgets as Qtw


class GameWindow(Qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.show_text_label = Qtw.QLabel()
        self.text_input = Qtw.QLineEdit()
        self.text_input.textChanged.connect(self.check_text_input)

        layout = Qtw.QVBoxLayout()
        layout.addWidget(self.show_text_label)
        layout.addWidget(self.text_input)
        self.setLayout(layout)
        self.line_index = 0
        self.data = []
        self.load_data()

    def load_data(self):
        with open("resources/text.txt", 'r') as f:
            self.data = f.readlines()
        self.data = [line.rstrip('\n') for line in self.data]

        self.update_label()

    def update_label(self):
        value = self.data[self.line_index]
        self.show_text_label.setText(value)

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


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     app.setStyleSheet(stylesheet)
#     window = GameWindow()
#     window.setWindowTitle("Master of keyboard")
#     window.setFixedSize(500, 500)
#     window.show()
#     sys.exit(app.exec_())
