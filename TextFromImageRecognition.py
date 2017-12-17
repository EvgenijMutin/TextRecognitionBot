from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract'
print(pytesseract.image_to_string(Image.open('test.png')))
