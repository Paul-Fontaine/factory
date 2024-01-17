from typing import List

from image_reader import ImageReader


class Format1ImageReader(ImageReader):
    def __init__(self, path: str):
        ImageReader.__init__(self, path)

    def read_file(self) -> List[str]:
        data: list[str] = []
        # Read the file. (the 2 first lines contains the width and the height
        width: int = int(self._text_stream.readLine())
        height: int = int(self._text_stream.readLine())
        for i in range(height):
            line: str = ""
            for j in range(width):
                line += self.text_stream.readLine()
            data.append(line)
        return data
