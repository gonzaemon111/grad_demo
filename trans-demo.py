# -*- coding: utf-8 -*

# %matplotlib inline
import cv2
import matplotlib.pyplot as plt

MAX_CORNERS = 50
BLOCK_SIZE = 3
QUALITY_LEVEL = 0.01
MIN_DISTANCE = 20.0

img = cv2.imread('./data/lena.jpg')
plt.imshow(img)