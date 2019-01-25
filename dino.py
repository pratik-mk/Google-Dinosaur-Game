# -*- coding: utf-8 -*-
from PIL import ImageGrab, Image
from PIL import ImageOps
import pyautogui
import time
from numpy import *
 
class Cordinates():
     replayBtn = (480,505)
     dinosaur = (194,509)
     #x coordinate 260 to check tree
     #y coordinate 530 to check tree
     
def restartGame():
    pyautogui.click(Cordinates.replayBtn)
    
def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("jump")
    pyautogui.keyUp('space')

def imageGrab():
    box = (Cordinates.dinosaur[0]+60,Cordinates.dinosaur[1],Cordinates.dinosaur[0]+220,Cordinates.dinosaur[1]+25)
    image = ImageGrab.grab(box)       
    grayImage = ImageOps.grayscale(image)
    a= array(grayImage.getcolors())
    return a.sum()

def main(): 
    restartGame()    
    while True:
        if(imageGrab()!=747):
            pressSpace()
            time.sleep(0.1)

main()    
     
