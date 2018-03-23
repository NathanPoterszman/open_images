#!/usr/bin/env python

import numpy as np 
import matplotlib.pyplot as plt 
import os
import skimage
from skimage import io

# open a list of images in a given folder 

folder = input("folder to reach:")
os.chdir(folder) #change the working directory
i = 0
L = os.listdir(os.getcwd()) #get the list of files
for file in L:
	print ('file number', i)
	ext = os.path.splitext(file)[1] #separate the file name in file + ext and keep ext
	if ext == '.tif': 
		img =  io.imread(file) #open image with a numpy array
		img = np.rollaxis(img, 3) #put channels first
		print(L[i], 'is an image')
		print (img.shape) #give the shape of the array (channels, z, x, y)
	else:
		print (L[i], 'is NOT an image')
	i += 1