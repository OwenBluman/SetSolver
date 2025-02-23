import mss
import cv2
import numpy as np
import os
import pyautogui


# Function to capture the screen using MSS
def capture_screen(region=None):
    with mss.mss() as sct:
        screenshot = sct.grab(region if region else sct.monitors[1])  # Capture full screen or region
        img = np.array(screenshot)
        return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)  # Convert BGRA to BGR for OpenCV


# Function to detect board images
def getBoard(image_folder, screen_img):
    detected_images = []

    for filename in os.listdir(image_folder):
        image_path = os.path.join(image_folder, filename)
        template = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

        if template is None:
            continue  # Skip if file is not an image

        # Convert template to grayscale if necessary
        if template.shape[-1] == 4:
            template = cv2.cvtColor(template, cv2.COLOR_BGRA2BGR)

        result = cv2.matchTemplate(screen_img, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= 0.95)  # Confidence threshold

        if len(loc[0]) > 0:
            detected_images.append(filename)

    return detected_images


# Function to click on target image
def clickTarget(target_image, screen_img):
    template = cv2.imread(target_image, cv2.IMREAD_UNCHANGED)

    if template is None:
        return

    if template.shape[-1] == 4:
        template = cv2.cvtColor(template, cv2.COLOR_BGRA2BGR)

    result = cv2.matchTemplate(screen_img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= 0.95:  # Confidence threshold
        x, y = max_loc
        w, h = template.shape[1], template.shape[0]
        center_x, center_y = x + w // 2, y + h // 2

        pyautogui.click(center_x, center_y)


# Example Usage
if __name__ == "__main__":
    image_folder = "path/to/your/images"

    screen_img = capture_screen()
    detected_images = getBoard(image_folder, screen_img)

    print("Detected images:", detected_images)

    if detected_images:
        clickTarget(os.path.join(image_folder, detected_images[0]), screen_img)
