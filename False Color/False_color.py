import cv2
import numpy as np
from spectral import *
from matplotlib import pyplot as plt

img = open_image('TIPJUL1.LAN')
img.__class__
print(img)

rows = img.shape[0]
cols = img.shape[1]

nir = img[:,:,3]
red = img[:,:,2]
green = img[:,:,1]

view = imshow(img, (3, 2, 1))

maxR = np.max(red)
minR = np.min(red)
maxN = np.max(nir)
minN = np.min(nir)

for i in range(rows):
    for j in range(cols):
        red[i,j] = ((red[i,j] - minR) / (maxR - minR))
        nir[i,j] = ((nir[i,j] - minN) / (maxN - minN))
        
bImg = np.zeros([rows,cols])
for i in range(rows):
    for j in range(cols):
        if ((nir[i,j]-red[i,j])/(nir[i,j]+red[i,j]) > 0:)
            bImg[i,j] = 1

plt.imshow(bImg, cmap = 'Greys', interpolation = 'nearest')