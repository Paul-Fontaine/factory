from image_reader import ImageReader
from format1_image_reader import Format1ImageReader
from format2_image_reader import Format2ImageReader


class ImageReaderFactory:
    @staticmethod
    def create_image_reader(path: str) -> ImageReader:
        if path.endswith('.fm1'):
            return Format1ImageReader(path)
        elif path.endswith('.fm2'):
            return Format2ImageReader(path)
