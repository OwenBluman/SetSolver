import pyautogui
import time
import os


# Function to check which images from the folder are on the screen
def getBoard(image_folder):
    detected_images = []
    i = 0
    # Loop through all images in the folder
    for filename in os.listdir(image_folder):
        image_path = os.path.join(image_folder, filename)
        try:
            # Attempt to locate the image on screen
            location = pyautogui.locateOnScreen(image_path, grayscale=False,confidence=0.95)

            if location:
                detected_images.append(filename)
                i +=1

        except pyautogui.ImageNotFoundException:
            pass  # If image is not found, do nothing and continue
        if (i == 11):
            break
    return detected_images

def clickTarget(target_image):
    location = pyautogui.locateOnScreen(target_image,grayscale=False,confidence=0.95)
    x, y = pyautogui.center(location)
    x, y = x // 2, y // 2
    pyautogui.click(x, y)

