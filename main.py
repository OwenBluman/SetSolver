import time
import pyautogui
import os
from game_logic import *
from screen_capture import *
from mss_detection import find_image
# Wait to ensure the screen is ready
import datetime

'''
print(datetime.datetime.now())
test_img = "iconPics/green_two_tilda_solid.png"
print("gonna call fucnaiton")
x,y = pyautogui.center(find_image(test_img))
pyautogui.click(x,y)
print(f"Here's the x {x}, and here's the y {y}")
print(datetime.datetime.now())
'''
time.sleep(1)
og_timer = datetime.datetime.now()
set_timer = datetime.datetime.now()
image_folder = "/Users/owenbluman/PycharmProjects/setSolver/SetSolver/iconPics"  # Replace with actual folder path
remaining_filenames = []
for filename in os.listdir(image_folder):
    remaining_filenames.append(filename)
for i in range(0,100):
    #print(remaining_filenames)
    current_filenames = getFilenames(remaining_filenames,False)
    try:
        try:
            set_filenames = getSet(current_filenames)
            print(f"Set found in {(datetime.datetime.now()-set_timer).total_seconds()} seconds, total time is {(datetime.datetime.now()-og_timer).total_seconds()}")
            set_timer = datetime.datetime.now()
            for filename in set_filenames:
                clickTarget(filename)
                remaining_filenames.remove(os.path.basename(filename))
        except:
            current_filenames = getFilenames(remaining_filenames, True)
            print(f"Caught exception and running bonus {datetime.datetime.now()}")
            set_filenames = getSet(current_filenames)
            print(f"Set found in {(datetime.datetime.now() - set_timer).total_seconds()} seconds, total time is {(datetime.datetime.now() - og_timer).total_seconds()}")
            set_timer = datetime.datetime.now()
            for filename in set_filenames:
                clickTarget(filename)
                remaining_filenames.remove(os.path.basename(filename))
            pass
    except:
        print('total fuck up')
        pass
    time.sleep(0.5)


