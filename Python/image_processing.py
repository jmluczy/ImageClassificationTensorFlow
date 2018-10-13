'''
Image Processing 
@author Jeff Blankenship, James Luczynski

<insert license and stuff here>

OpenCV-Python Tutorials at https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html
was used during this project.  Various individual lines of code are modified from their examples.

'''


import cv2
import numpy as np
import os
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory


directory = askdirectory()
print(directory)



#Globals
SIZE = 600            #set standard pixels for square image
BORDER = [255,255,0]  #BGR values for border padding color
THRESH_FRAC = 0.5   #Fraction of mean gray value to use for binary threshold (0.0-1.0) 

#load original image
filename = askopenfilename()
image_orig = cv2.imread(filename)
cv2.imshow('original', image_orig)


#convert image to grayscale
image_grayscale = cv2.cvtColor(image_orig, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale', image_grayscale)

#scale image to be <=SIZE width and height
height, width, depth = image_orig.shape
print("image_orig height:", height)
print("image_orig width: ", width)

scale = SIZE / max(height,width)
image_scaled = cv2.resize(image_grayscale,(int(width*scale),int(height*scale)))
cv2.imshow('scaled', image_scaled)

#add padding as needed to make it square
height, width = image_scaled.shape
print("image_scaled height:", height)
print("image_scaled width: ", width)
if (width>=height):
    print("padding the top and bottom")
    pad = int((SIZE - height)/2)
    image_padded = cv2.copyMakeBorder(image_scaled,pad,pad,0,0,cv2.BORDER_CONSTANT,value=BORDER) 
else: #(width<height)
    print("padding the sides")
    pad = int((SIZE - width)/2)
    image_padded = cv2.copyMakeBorder(image_scaled,0,0,pad,pad,cv2.BORDER_CONSTANT,value=BORDER) 
cv2.imshow('image_padded', image_padded)

#convert image to black and white
print("Average grayscale value: ", np.mean(image_padded))
threshold = int(np.mean(image_padded)* THRESH_FRAC )   
ret,image_final = cv2.threshold(image_padded,threshold,255,cv2.THRESH_BINARY_INV)
cv2.imshow("image_final", image_final)




# wait for escape to quit
print("Press <ESC> to quit.")
while True:
    k = cv2.waitKey(1) & 0xFF
    if k == 27:   
        break

cv2.destroyAllWindows()
