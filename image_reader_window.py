import sys

from image_reader_factory import ImageReaderFactory
from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QTextEdit, QHBoxLayout, QVBoxLayout, QApplication


class ImageReaderWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Image Reader')
        self.__vlayout = QVBoxLayout(self)

        self.__line_edit: QLineEdit = QLineEdit(self)
        self.__button_load: QPushButton = QPushButton('load', self)
        self.__button_load.clicked.connect(self.__load)

        self.__hlayout = QHBoxLayout(self)
        self.__hlayout.addWidget(self.__line_edit)
        self.__hlayout.addWidget(self.__button_load)

        self.__text_edit: QTextEdit = QTextEdit(self)
        self.__text_edit.setReadOnly(True)

        self.__vlayout.addLayout(self.__hlayout)
        self.__vlayout.addWidget(self.__text_edit)

    def __load(self):
        path: str = self.__line_edit.text()
        image_reader = ImageReaderFactory.create_image_reader(path)
        data = image_reader.read_file()
        for line in data:
            print(line)
            self.__text_edit.append(line)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ImageReaderWindow()
    window.show()

    sys.exit(app.exec())
