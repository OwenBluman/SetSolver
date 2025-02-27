import time
import pyautogui
from screen_capture import *
from game_logic import *
# Wait to ensure the screen is ready

time.sleep(1)
image_folder = "/Users/owenbluman/PycharmProjects/setSolver/SetSolver/iconPics"  # Replace with actual folder path
remaining_filenames = []
for filename in os.listdir(image_folder):
    remaining_filenames.append(filename)
current_filenames = getFilenames(remaining_filenames)
set_filenames = getSet(current_filenames)
print(set_filenames)
