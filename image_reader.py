from abc import abstractmethod, ABC
from typing import List
from PySide6.QtCore import QFile, QTextStream


class ImageReader(ABC):
    def __init__(self, path: str):
        self._qfile: QFile = None
        self._text_stream: QTextStream = None
        self._path: str = path

        self.__open_file()

    def __open_file(self):
        self._qfile = QFile(self._path)
        if self._qfile.open(QFile.ReadOnly):
            self._text_stream = QTextStream(self._qfile)

    @abstractmethod
    def read_file(self) -> List[str]:
        pass
