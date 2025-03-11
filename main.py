'''
This is the main driver for the program that will automatically win at Set with Friends
'''
import time
import os
from screen_capture import *
import datetime

#Wait for screen
time.sleep(1)

#Set up clocks
og_timer = datetime.datetime.now()
set_timer = datetime.datetime.now()

#Set up images
image_folder = "/Users/owenbluman/PycharmProjects/setSolver/SetSolver/iconPics"  # Replace with actual folder path
remaining_filenames = []
for filename in os.listdir(image_folder):
    remaining_filenames.append(filename)

#Loop over find/solve/click
for i in range(0,100):
    current_filenames = getFilenames(remaining_filenames,False)
    try:
        try:
            #Normal search
            set_filenames = getSet(current_filenames)
            print(f"Set found in {(datetime.datetime.now()-set_timer).total_seconds()} seconds, total time is {(datetime.datetime.now()-og_timer).total_seconds()}")
            set_timer = datetime.datetime.now()
            for filename in set_filenames:
                clickTarget(filename)
                remaining_filenames.remove(os.path.basename(filename))
        except:
            #Bonus row search
            current_filenames = getFilenames(remaining_filenames, True)
            print(f"Running bonus")
            set_filenames = getSet(current_filenames)
            print(f"Set found in {(datetime.datetime.now() - set_timer).total_seconds()} seconds, total time is {(datetime.datetime.now() - og_timer).total_seconds()}")
            set_timer = datetime.datetime.now()
            for filename in set_filenames:
                clickTarget(filename)
                remaining_filenames.remove(os.path.basename(filename))
            pass
    except:
        print('Bonus error')
        pass
    #Wait for cards to reset
    time.sleep(0.5)


