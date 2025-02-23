import time
import pyautogui
from screen_capture import *
from game_logic import *
#Wait to ensure the screen is ready
time.sleep(2)


image_folder = "/Users/owenbluman/PycharmProjects/setSolver/SetSolver/iconPics"  # Replace with actual folder path


found_images = getBoard(image_folder)
set_up_cards = []
for image in found_images:
    set_up_cards.append(filename_to_card(image))
table = Table(set_up_cards)
set_found = table.findsets_gnt()
for card in set_found:
    print(card_to_filename(card))
    clickTarget(card_to_filename(card))
