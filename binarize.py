import os
import cv2 as cv

images = os.listdir('./rgb_images/')
output_path = './binary_images/'

for img in images:
    image1 = cv.imread(img)
    image2 = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)
