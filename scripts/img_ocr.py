"""
note: tesseract must be pre-installed and put on PATH
"""

import pytesseract
from PIL import Image
import fitz 


def pdf2imgs(src: str):
    pdf_file = fitz.open(src)
    for page in pdf_file:  # iterate through the pages
        
        mat = fitz.Matrix(2, 2)
        pix = page.get_pixmap(matrix=mat)  # render page to an image
        pix.save("page-%i.png" % page.number)  # store image as a PNG


def img2str(src: str):
    return pytesseract.image_to_string(Image.open(src))


if __name__ == '__main__':
    # print(img2str("testText/Screenshot1.png"))
    # pdf2imgs("testText/test_pdf.pdf")
    print(img2str("page-0.png"))
