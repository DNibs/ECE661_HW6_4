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


# Load images from file


# Apply mask using RGB
#   RGB_channel_mask = otsu(img_channel)
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

