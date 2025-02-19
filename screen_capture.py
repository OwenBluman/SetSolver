import pyautogui
import time

# Define the search region (upper-left quadrant)
screen_width, screen_height = 1470, 956
# Wait to ensure the screen is ready
time.sleep(2)

# Try locating the image
target_image = "target_image.png"

try:
    location = pyautogui.locateOnScreen(target_image, confidence=0.9)

    if location:
        x, y = pyautogui.center(location)
        pyautogui.click(x, y)
        print(f"Clicked at ({x}, {y})")
        time.sleep(0.5)

        # Type "Hello World"
        pyautogui.write("Hello World", interval=0.1)  # Simulates natural typing speed
        print("Typed 'Hello World'")
    else:
        print("Target image not found.")

except Exception as e:
    print(f"Error: {e}")
