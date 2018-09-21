# Import libraries
import cv2
import os
from PIL import Image

folders = os.listdir("images_q")

for f in folders:
    
    if f == ".DS_Store":
        continue

    # Set name of folder
    folder = "images_q/" + f
    
    # List all the files in the directory
    files = os.listdir(folder)
    
    if len(files) == 0:
        continue
    
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
                    m2 = abs(im[i][j][0] - 211)
                    m3 = abs(im[i][j][1] - 112)
                    m4 = abs(im[i][j][2] - 0)
                    
                    if((m2 == 0) and (m3 == 0) and (m4 == 0)):
                        a.append((i, j))
            
        # Trim the image  
        if(len(a) > 0):
            vim = im[:a[0][0]-10, 50:800, :]
        else:
            vim = im[:, :800, :]
            
        # Save the cropped image
        vim = Image.fromarray(vim)
        vim.save(folder + '/cropped/' + file)
        
        print(k, "of", len(files), "done!")
        
        k += 1
        
    print("__________________________________________________")
    print(f, "done!")
    
import pygame
file = 'raja.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()
        
#import webbrowser

## Define chrome path
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
#
## Iterate over cropped images
#files = os.listdir(folder + "/cropped/")
#
#for file in files:
#    webbrowser.get(chrome_path).open(folder + "/cropped/" + file)

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