import cv2
import sys, os
import numpy as np
from matplotlib import pyplot as plt

one = sys.argv[1]
two = sys.argv[2]

#Read the image data from openCV
image_01 = cv2.imread(one)
image_02 = cv2.imread(two)

#print(image_01)
#print(image_02)

#Setup the matrices and set them all to zero to initialize
def diff(image, image2):
    row, col, garbage = image.shape
    bin_image = np.zeros(256)
    scale = np.arange(0, 256)
    gray_image_01 = np.zeros([row, col]) #First image greyscale
    gray_image_02 = np.zeros([row, col]) #Second image greyscale
    entity = np.zeros([row, col])
    for i in range(row):
        for j in range(col):
            res = int(image[i,j,1]*0.72 + image[i,j,0]*0.07 + image[i,j,2]*0.21)
            res2 = int(image2[i,j,1]*0.72 + image2[i,j,0]*0.07 + image2[i,j,2]*0.21)
            gray_image_01[i,j] = res
            gray_image_02[i,j] = res2
            #Find the image with the different object
            obj = abs(gray_image_01[i,j] - gray_image_02[i,j])
            entity[i,j] = obj
            dif = abs(res - res2)
            if(dif > 110):
                entity[i,j] = 255
            else:
                entity[i,j] = 0
            bin_image[int(entity[i,j])] = bin_image[int(entity[i,j])] + 1
    cv2.imwrite('Images/bin_image.png', entity)
    plt.bar(entity, bin_image, color='yellow')
    plt.title("Picture Difference Histogram")
    plt.show()

diff(image_01, image_02)
