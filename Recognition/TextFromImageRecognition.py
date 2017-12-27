from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract'


def textFromImageRecognition(file):
    return pytesseract.image_to_string(Image.open(file))
