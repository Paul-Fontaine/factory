import sys

from image_reader_factory import ImageReaderFactory
from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QTextEdit, QHBoxLayout, QVBoxLayout, QApplication


class ImageReaderWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Image Reader')
        self.setMinimumSize(300, 300)

        vlayout = QVBoxLayout(self)

        self.__line_edit: QLineEdit = QLineEdit(self)
        self.__line_edit.setText('Data/Image1.fm1')
        self.__button_load: QPushButton = QPushButton('load', self)
        self.__button_load.clicked.connect(self.__load)

        hlayout = QHBoxLayout(self)
        hlayout.addWidget(self.__line_edit)
        hlayout.addWidget(self.__button_load)

        self.__text_edit: QTextEdit = QTextEdit(self)
        self.__text_edit.setReadOnly(True)
        self.__text_edit.setFontFamily('Courier New')
        self.__text_edit.setLineWrapMode(QTextEdit.NoWrap)

        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.__text_edit)

    def __load(self):
        path: str = self.__line_edit.text()
        try:
            image_reader = ImageReaderFactory.create_image_reader(path)
        except FileNotFoundError:
            self.__text_edit.clear()
            self.__text_edit.setTextColor('red')
            self.__text_edit.append("file not found")
            return
        except ValueError:
            self.__text_edit.clear()
            self.__text_edit.setTextColor('red')
            self.__text_edit.append("unknown format")
            return

        data = image_reader.read_file()
        self.__text_edit.clear()
        self.__text_edit.setTextColor('black')
        for line in data:
            self.__text_edit.append(line)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ImageReaderWindow()
    window.show()

    sys.exit(app.exec())
