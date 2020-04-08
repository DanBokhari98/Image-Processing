import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys, os

def calcHist(image):
    row, col, garbage = image.shape
    gray_image = np.zeros([row,col])
    scale = np.arange(0,256)
    red = np.zeros(256)
    green = np.zeros(256)
    blue = np.zeros(256)
    gray = np.zeros(256)

# Grayscale conversion
    for i in range (row):
        for j in range(col):
            gray_image[i,j] = image[i,j,0]*0.07 + image[i,j,2]*0.21 + image[i,j,1]*0.72

    for i in range (row):
       for j in range(col):
           red[image[i,j,2]] = red[image[i,j,2]] + 1
           green[image[i,j,1]] = green[image[i,j,1]] + 1
           blue[image[i,j,0]] = blue[image[i,j,0]] + 1
           gray[int(gray_image[i,j])] = gray[int(gray_image[i,j])] + 1

    #Display all colors of the Histogram
    plt.bar(scale,red,color="red")
    plt.bar(scale,gray,color="gray")
    plt.bar(scale,green,color="green")
    plt.bar(scale,blue,color="blue")
    plt.title("Histogram")
    plt.figure(1)
    #Output results to a file and save
    plt.savefig('./Output/overexposed_color_histogram.png')
    plt.show()

arg = sys.argv[1]
image = cv2.imread(arg)
calcHist(image)

# Red = ( R + G + B ) - (G + B)
# Cyan =(R+G+B)-(R)
# Magenta=(R+G+B)-(G)
# Yellow =(R+G+B)-(B)
