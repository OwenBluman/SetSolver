import pyautogui
import time
import os

from game_logic import card_to_filename, filename_to_card, Table


def getFilenames(remaining_filenames):
    found_filenames = []
    for filename in remaining_filenames:
        filename = "/Users/owenbluman/PycharmProjects/setSolver/SetSolver/iconPics/" + filename
        try:
            location = pyautogui.locateOnScreen(filename, grayscale=False,confidence=0.97)
            if location:
                found_filenames.append(filename)
        except pyautogui.ImageNotFoundException:
            pass
    return found_filenames

def getSet(current_board):
    cards = []
    for filename in current_board:
        filename = filename[63:]
        cards.append(filename_to_card(filename))
    game_table = Table(cards)
    set_cards = game_table.findsets_gnt()
    filenames =[]
    for card in set_cards:
        new_filename = card_to_filename(card)
        new_filename = "/Users/owenbluman/PycharmProjects/setSolver/SetSolver/iconPics/" + new_filename
        filenames.append(new_filename)
    return filenames

# Function to check which images from the folder are on the screen
def getBoard(found_cards,remaining_cards):
    detected_images = found_cards
    # Loop through all images in the folder
    for card in remaining_cards:
        try:
            location = pyautogui.locateOnScreen(card_to_filename(card), grayscale=False,confidence=0.95)
            if location:
                detected_images.append(card)

        except pyautogui.ImageNotFoundException:
            pass  # If image is not found, do nothing and continue
        if (len(detected_images) == 12):
            break
    return detected_images

def clickTarget(target_image):
    location = pyautogui.locateOnScreen(target_image,grayscale=False,confidence=0.95)
    x, y = pyautogui.center(location)
    x, y = x // 2, y // 2
    pyautogui.click(x, y)

