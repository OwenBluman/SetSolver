import time
import pyautogui
from screen_capture import *
from game_logic import *
# Wait to ensure the screen is ready
time.sleep(1)


image_folder = "/Users/owenbluman/PycharmProjects/setSolver/SetSolver/iconPics"  # Replace with actual folder path
remaining_cards = []
for filename in os.listdir(image_folder):
    remaining_cards.append(filename_to_card(filename))

found_images = getBoard(image_folder)
current_cards = []
for image in found_images:
    current_cards.append(filename_to_card(image))
    remaining_cards.remove(filename_to_card(image))
table = Table(current_cards)
set_found = table.findsets_gnt()
for card in set_found:
    print(card_to_filename(card))
    clickTarget(card_to_filename(card))
    current_cards.remove(card)
