# Import libraries
import cv2
import os
from PIL import Image

# Set name of folder
folder = "images/verbal_reasoning_"

# List all the files in the directory
files = os.listdir(folder)

# Create a folder to save cropped image
if not os.path.exists(folder + "/cropped"):
    os.mkdir(folder + "/cropped")

# Counter over files
k = 1

# Iterate through all the files
for file in files:
    
    if(file == '.DS_Store'):
        continue
    
    # Read the image
    im = cv2.imread(folder + '/' + file)
    
    # Search for index of view answer
    a = []
    
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
                m2 = abs(im[i][j][0] - 188)
                m3 = abs(im[i][j][1] - 147)
                m4 = abs(im[i][j][2] - 98)
                
                if((m2 == 0) and (m3 == 0) and (m4 == 0)):
                    a.append((i, j))
        
    # Trim the image  
    if(len(a) > 0):
        vim = im[:a[0][0], :800, :]
    else:
        vim = im[:, :600, :]
        
    # Save the cropped image
    vim = Image.fromarray(vim)
    vim.save(folder + '/cropped/' + file)
    
    print(k, "of", len(files), "done!")
    
    k += 1

import pygame
file = 'raja.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()

## Repair incorrectly cropped image    
#def single_file(file, folder, dim):
#    # Read the image
#    im = cv2.imread(folder + '/' + file)
#    
#    # Search for index of view answer
#    a = []
#    
#    for i in range(im.shape[0]):
#        for j in range(im.shape[1]):
#                m2 = abs(im[i][j][0] - 188)
#                m3 = abs(im[i][j][1] - 147)
#                m4 = abs(im[i][j][2] - 98)
#                
#                if((m2 == 0) and (m3 == 0) and (m4 == 0)):
#                    a.append((i, j))
#        
#    # Trim the image    
#    vim = im[:a[0][0], :dim, :]
#        
#    # Save the cropped image
#    vim = Image.fromarray(vim)
#    vim.save(folder + '/cropped/' + file)
#    
#single_file('image3.png', folder, 800)