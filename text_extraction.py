import pytesseract
import easyocr
from glob import glob
import re
# from mtcnn.mtcnn import MTCNN
from mtcnn_cv2 import MTCNN
import sys
import shutil
import matplotlib.pyplot as plt
import os
import cv2

imgs = glob('/home/aja/Documents/ML/dataset/text_extraction/test/*')
image = imgs[0]


class TextExtract:
    """
    Class reponsible for extraction and handling of information from an image
    """

    def __init__(self, image):
        self.img = image  # image to be processed
        self.num = {}  # numeric values extracted
        self.info = {}  # non-numeric values extracted
        self.extract()  # method for extraction

    def numeric_handler(self):
        """ 
        method responsible for handling numeric values found on the image.

        Uses easyocr library to extract values and find every numeric value on the image.

        output:
            - returns a list of numeric values that was found on the image
        """
        numeric = []
        # dealing with numbers
        num_reader = easyocr.Reader(['en', 'fr'])
        nums = num_reader.readtext(self.img)
        spec = [',', '.']  # list of special characters identified
        # nums output is represented as [(bbox, text, prob),...]
        nums = [value[1] for value in nums]
        for text in nums:
            if text.isnumeric():
                numeric.append(text)
            else:
                try:
                    # for every special character identified in our list of special letters
                    for spc in spec:
                        # if special character in text then append the string
                        if spc in text:
                            numeric.append(text)
                except:
                    # handling extraction error
                    raise Exception('An error occured while extracting numeric values')
        return numeric

    def info_handler(self):
        char = pytesseract.image_to_string(image)

    def face_extractor(self):
        detector = MTCNN()
        img = cv2.imread(self.img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # for mtcnn
        face = detector.detect_faces(img)
        if len(face) > 1 or len(face) < 1:
            print(image)
            return []
        face_coords = face[0]['box']
        x1, y1, width, height = face_coords[0], face_coords[1], face_coords[2], face_coords[3]
        x2, y2 = x1 + width, y1 + height
        extracted_face = img[y1:y2, x1:x2]
        return extracted_face

    def extract(self):
        nums = self.numeric_handler()
        face = self.face_extractor()
        face = plt.imshow(face)
        print(nums)
        print(face)


text = TextExtract(image)
