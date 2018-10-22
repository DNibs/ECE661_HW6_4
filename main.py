# ECE661_HW6
# Author: David Niblick
# Date: 23OCT18
# main.py

# This application applies a binary mask that separates the foreground from the background using Otsu's algorithm.
#   This is accomplished with histograms of the RGB channels, and then histogram of texture for comparison.
#   After the binary mask is applied, the contours are found using a simple pixel-neighbor comparison.

# file for histogram
# file for creating texture

import cv2
import numpy as np
import otsu as ot
import matplotlib.pyplot as plt


# Load images from file
img1 = cv2.imread('baby.jpg', 1)
img2 = cv2.imread('lighthouse.jpg', 1)
img3 = cv2.imread('ski.jpg', 1)
img1_g = cv2.imread('baby.jpg', 0)
img2_g = cv2.imread('lighthouse.jpg', 0)
img3_g = cv2.imread('ski.jpg', 0)


# Apply mask using RGB
#   get channels
img1_ch_R = img1[:, :, 0]
img1_ch_G = img1[:, :, 1]
img1_ch_B = img1[:, :, 2]
#   RGB_channel_mask = otsu(img_channel)
img1_mask_R_hist = ot.histogram(img1_ch_R)
img1_mask_R_val = ot.apply_otsu(img1_mask_R_hist)
img1_mask_R = ot.create_mask(img1_ch_R, img1_mask_R_val)

plt.imshow(img1_mask_R)
plt.show()

#   AND channels for final mask
#   refine and display

# Apply mask using texture with three different scales of N
#   texture_channel = texture(img, N=?)
#   texture_channel_mask = otsu(texture_channel)
#   AND channels for final mask
#   refine and display

# Find Contours
#   iterate over every pixel
#   if p=1, iterate over neighbors
#       if all neighbors equal 1, not contour, if all neighbors equal 1, contour

