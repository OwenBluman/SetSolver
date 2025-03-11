'''
This program handles interaction between the current screen region presented by the driver and the game logic
'''
import pyautogui
from game_logic import card_to_filename, filename_to_card, Table
from mss_detection import find_image

'''
Gets the filenames of all of the Set cards currently on the board, stopping once a set is found
    remaining_filenames: list of filenames to search for (will shrink when sets are found by program)
    bonus: if true then increase the screen search region to account for extra row
    return: the list of filenames that were found on the board
'''
def getFilenames(remaining_filenames,bonus):
    found_filenames = []
    for filename in remaining_filenames:
        filename = "/Users/owenbluman/PycharmProjects/setSolver/SetSolver/iconPics/" + filename
        #Try to find each image, add to list if found, pass otherwise
        try:
            location = find_image(filename,bonus)
            if location:
                found_filenames.append(filename)
                try:
                    #Once three cards are found, look for a set and if found then just return
                    #This saves time as program doesn't need to find all cards, just those that make up a set
                    if len(found_filenames) > 2 and getSet(found_filenames) != None:
                        return found_filenames
                except:
                    pass
        except pyautogui.ImageNotFoundException:
            pass
    return found_filenames

'''
Gets the filenames of the cards that make up a set from the current array of filenames
    current_board: list of filenames that will be searched through
    return: the list of filenames that form a set
'''
def getSet(current_board):
    cards = []
    for filename in current_board:
        #Slice image filename from full path
        filename = filename[63:]
        cards.append(filename_to_card(filename))
    #Find set
    game_table = Table(cards)
    set_cards = game_table.findsets_gnt()
    filenames = []
    #Return filenames in full path format
    for card in set_cards:
        new_filename = card_to_filename(card)
        new_filename = "/Users/owenbluman/PycharmProjects/setSolver/SetSolver/iconPics/" + new_filename
        filenames.append(new_filename)
    return filenames

'''
Clicks on a given Set card
    target_image: the card to be clicked on
'''
def clickTarget(target_image):
    #Find image in board (always including bonus row)
    location = find_image(target_image,True)
    x, y = pyautogui.center(location)
    pyautogui.click(x, y)

