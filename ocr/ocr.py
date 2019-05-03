from PIL import Image,ImageEnhance
import pytesseract
import argparse
import cv2
import os,sys
import numpy as np
import csv
import time
dirs=os.listdir("./cropx")
for file in dirs:
	print(file)
	image = cv2.imread("./cropx/"+file)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 

	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)

	text = pytesseract.image_to_string(Image.open(filename))
	os.remove(filename)

	#print(text)
	im=Image.open("./cropx/"+file)
	enhancer=ImageEnhance.Contrast(im)
	enhanced_im=enhancer.enhance(3.0)
	enhanced_im.save("enhanced.png")
	img1 = cv2.imread('enhanced.png')

	img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
	a = np.double(img1)
	b = a + 15
	img2 = np.uint8(b)

	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, img2)
	text2 = pytesseract.image_to_string(Image.open(filename))
	#print(text)

	os.remove(filename)
	f=open('text.csv','a')
	f.write("\n")
	f.write("question")
	f.write("\n")
	f.write(text)
	f.write("\n")
	f.write("options")
	f.write("\n")
	f.write(text2)
	f.write(",")
	f.close()

cv2.waitKey(0)
cv2.destroyAllWindows()