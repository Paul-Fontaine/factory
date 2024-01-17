from typing import List

from image_reader import ImageReader


class Format2ImageReader(ImageReader):
    def __init__(self, path: str):
        ImageReader.__init__(self, path)

    def read_file(self) -> List[str]:
        data: list[str] = []
        # Read the file. the first line contains the width
        line: str = ""
        width: int = int(self._text_stream.readLine())
        temp: list[str] = self._text_stream.readLine()
        for i in range(len(temp)):
            if i % width == 0:
                data.append(line)
                line = ""
            line += temp[i]
        data.append(line)
        return data
