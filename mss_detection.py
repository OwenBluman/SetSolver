'''
This program handles template matching for Set cards
'''
import cv2
import numpy as np
import mss.tools
import mss
import pyautogui

'''
Finds the coordinates of the given Set card using MSS for screen capture and pyautogui for template matching
    image_path: file path to Set card (in iconPics)
    bonus_row: if true then increase the screen search region to account for extra row
    confidence: set to 0.97 to accurately locate based on color while accounting for any potential small errors
    return: the coordinates of the given Set card (have to divide by 2 and add the padding back in due to Mac display,
    see more info here: https://github.com/asweigart/pyautogui/issues/671)
'''
def find_image(image_path, bonus_row, confidence=0.97):
    height = 490
    if bonus_row:
        height = 610
    with mss.mss() as sct:
        image = cv2.imread(image_path)

        #Define board region accounting for presence/absense of fifth row
        board_region = {"top" : 215, "left" : 440, "width" : 595, "height" : height}
        sct_image = sct.grab(board_region)
        screen = np.array(sct_image)
        screen = cv2.cvtColor(screen, cv2.COLOR_RGBA2RGB)
        left,top,width,height = pyautogui.locate(image,screen,confidence=confidence,grayscale=False)
        return (left/2)+440,(top/2)+215,width/2,height/2,image_path




