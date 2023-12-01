import os
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def convert():
    directory = r'C:\Users\vishn\OCR\Images'
    for filename in os.listdir(directory):  
        if filename.lower().endswith(('.png','.jpg',".jpeg",'.bmp')):
            image = cv2.imread(os.path.join(directory, filename))
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, threshold_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
            text = pytesseract.image_to_string(threshold_image)
    file=open('image.txt', 'w')
    file.write(text)
    file.close()
    


convert()
os.system("image.txt")