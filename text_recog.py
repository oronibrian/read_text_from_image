import cv2
import sys
from PIL import Image
import pytesseract

def ocr_file_in(filename):
    text = pytesseract.image_to_string(Image.open(filename)) 
    return text



print('-------------------------------------------')
result=ocr_file_in('images/computervision.jpg')
print(result)

