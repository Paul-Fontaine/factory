import sys
from PySide6.QtWidgets import QApplication
from image_reader_window import ImageReaderWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ImageReaderWindow()
    window.show()

    sys.exit(app.exec())
