"""
note: tesseract must be pre-installed and put on PATH
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
"""

import pytesseract
from PIL import Image
import fitz 


def pdf2imgs(filename: str):
    pdf_file = fitz.open(filename)
    for page in pdf_file:  # iterate through the pages
        
        mat = fitz.Matrix(2, 2)
        pix = page.get_pixmap(matrix=mat)  # render page to an image
        pix.save("var/page-%i.png" % page.number)  # store image as a PNG
    print("image converted...")


def img2str(filename: str):
    return pytesseract.image_to_string(Image.open(filename))


if __name__ == '__main__':
    # print(img2str("testText/Screenshot1.png"))
    # pdf2imgs("testText/test_pdf.pdf")
    print(img2str("page-0.png"))
