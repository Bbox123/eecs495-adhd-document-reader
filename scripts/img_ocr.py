"""
note: tesseract must be pre-installed and put on PATH
"""

import pytesseract
from PIL import Image

def img2str(src: str):
    return pytesseract.image_to_string(Image.open('testText/Screenshot1.png'))


if __name__ == '__main__':
    print(img2str("testText/Screenshot1.png"))
