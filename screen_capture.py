import pyautogui
import time

# Define the search region (upper-left quadrant)
screen_width, screen_height = 1470, 956
# Wait to ensure the screen is ready
time.sleep(2)

equation = {"4.png","plus.png","6.png","equals.png"}
for character in equation:
    target_image = character
    location = pyautogui.locateOnScreen(target_image, confidence=0.95)
    x, y = pyautogui.center(location)
    x, y = x // 2, y // 2
    pyautogui.click(x, y)
    print(f"Clicked at ({x}, {y})")
    time.sleep(0.5)


