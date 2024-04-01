from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QListWidget, QFileDialog
from PyQt6.QtCore import Qt, QMimeData, QTranslator as tr
from GUI import Ui_MyConverter 
import sys
import os
import cv2
import pytesseract
from pdf2image import convert_from_path


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
directory = r'C:\Users\vishn\Python\OCR\dir'
os.chdir(directory)
filenames = []

class MyMainWindow(QMainWindow, Ui_MyConverter):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.SelectFile.clicked.connect(self.Select_file)
        self.Convert.clicked.connect(self.convert)
    
    def Select_file(self):
        global filenames
        filenames, _ = QFileDialog.getOpenFileNames(
            self, "Select File", "", "PDF Files (*.pdf);;Image Files (*.png *.jpg *.jpeg *.bmp);; All Files (*.*)"
        )   

    def pdf_to_image(self):
        for filename in filenames:
            if filename.lower().endswith(('.pdf')):
                image=convert_from_path(filename,poppler_path=r'C:\Users\vishn\AppData\Local\Programs\Python\poppler-23.11.0\Library\bin')
    
            for i in range(len(image)):
                image[i].save('Page '+ str(i+1) +'.png', 'JPEG')

    def image_to_text(self):
        for filename in os.listdir(directory):  
            if filename.lower().endswith(('.png','.jpg','.jpeg','.bmp')):
                image = cv2.imread(os.path.join(directory, filename))
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                _, threshold_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
                text = pytesseract.image_to_string(threshold_image)
                with open('image.txt', 'a') as file:
                    file.write(text)
                    file.close()
                    os.remove(filename)
            

    def convert(self):
        choise = self.comboBox.currentText()

        if choise == "Image or PDF to text":
            for filename in filenames:
                if filename.lower().endswith(".pdf"):
                    self.pdf_to_image() 
            self.image_to_text()


        elif choise == "PDF to image":
            self.pdf_to_image()

        elif choise == "Image to PDF":
            for filename in filenames:
                print(filename)

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())  