import cv2
import numpy as np
import mss.tools
import mss
import pyautogui

def find_image(image_path, bonus_row, confidence=0.97):
    #print("finding image")
    height = 490
    if bonus_row:
        height = 610
    with mss.mss() as sct:
        image = cv2.imread(image_path)
        monitor = {"top" : 215,"left" : 440, "width" : 595, "height" : height}

        sct_image = sct.grab(monitor)
        #mss.tools.to_png(sct_image.rgb, sct_image.size,output="test_board.png")
        screen = np.array(sct_image)
        screen = cv2.cvtColor(screen, cv2.COLOR_RGBA2RGB)
        #print(f"calling locate with confidence {confidence}")
        left,top,width,height = pyautogui.locate(image,screen,confidence=confidence,grayscale=False)
        #print(f"left {left}, top {top}, width {width}, height {height}")
        return (left/2)+440,(top/2)+215,width/2,height/2,image_path




