# ECE661_HW6
# Author: David Niblick
# Date: 23OCT18
# otsu.py


import cv2
import numpy as np


# Create Histogram
def histogram(img):
    h = np.size(img, 0)
    w = np.size(img, 1)
    L = w*h

    hist_n = np.zeros(L)
    hist_p = np.zeros(L)

    for i in range(0, h):
        for j in range(0, w):
            lum = int(img[i, j])
            hist_n[lum] = hist_n[lum] + 1

    hist_p = hist_n / np.sum(hist_n)

    return hist_n


def apply_otsu(hist_n):
    # Create distribution
    L = np.size(hist_n)
    hist_p = hist_n / np.sum(hist_n)
    print('L = {}'.format(L))
    w0 = np.zeros(L)
    w1 = np.zeros(L)
    mu0 = np.zeros(L)
    mu1 = np.zeros(L)

    # Iterate each illum - calculate class prob, mean, between-class variance
    for k in range(0, L):
        w0[k] = np.sum(hist_p[0:k])
        w1[k] = 1 - w0[k]


    # Choose k that corresponds to max between-class variance

# Create mask
#   iterate over image; if pixel > k, set mask to 1

# return mask
