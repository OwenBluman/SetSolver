import pyautogui
import time
import cv2
from numpy import inf
import numpy
from colorthief import ColorThief
from torch.distributed.tensor import empty

colorT = ColorThief('red_two_pill_solid.png')
red_base = colorT.get_color(quality=1)
print(red_base)
screen_width, screen_height = 1470, 956
# Wait to ensure the screen is ready
time.sleep(2)

def color_match(regions):
    best_diff = 777
    i = 0
    for region in regions:
        x, y = pyautogui.center(region)
        x, y = x // 2, y // 2
        ss = pyautogui.screenshot(region=(x, y, 50, 50))
        filename = "/Users/owenbluman/PycharmProjects/setSolver/SetSolver/test" + str(i) + ".png"
        ss.save(filename)
        colorT = ColorThief(filename)
        dominant_color = colorT.get_color(quality=1)
        print(dominant_color)
        total_diff = (sum(abs(x - y) for x, y in zip(dominant_color, red_base)))/ len(red_base)
        print(total_diff)
        if total_diff < best_diff:
            best_diff = total_diff
        i += 1
        print(i)
    return regions[i-1]


target_image = "purple_one_tilda_stripe.png"
location = pyautogui.locateOnScreen(target_image, confidence=0.90)
x, y = pyautogui.center(location)
x, y = x // 2, y // 2
PIXEL = pyautogui.screenshot(region=(x, y, 1, 1))
print(PIXEL.getcolors())
pyautogui.click(x, y)
print(f"Clicked at ({x}, {y})")
time.sleep(0.5)

target_image = "red_two_pill_solid.png"
locations = pyautogui.locateAllOnScreen(target_image)
locations = list(locations)
x, y = pyautogui.center(color_match(locations))
x, y = x // 2, y // 2
PIXEL = pyautogui.screenshot(region=(x, y, 1, 1))
print(PIXEL.getcolors())
pyautogui.click(x, y)
print(f"Clicked at ({x}, {y})")
time.sleep(0.5)

target_image = "green_three_diamond_empty.png"
location = pyautogui.locateOnScreen(target_image, confidence=0.90)
x, y = pyautogui.center(location)
x, y = x // 2, y // 2
PIXEL = pyautogui.screenshot(region=(x, y, 1, 1))
print(PIXEL.getcolors())
pyautogui.click(x, y)
print(f"Clicked at ({x}, {y})")
time.sleep(0.5)


