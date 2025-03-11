#https://sanderevers.github.io/2019/09/11/finding-sets.html

import random

class Table:

    def __init__(self, set_cards):
        self.cards = set_cards

    def findsets_gnt(self):  # generate and test
        for i, ci in enumerate(self.cards):
            for j, cj in enumerate(self.cards[i + 1:], i + 1):
                for k, ck in enumerate(self.cards[j + 1:], j + 1):
                    if ci.isset(cj, ck):
                        return ci, cj, ck

class Card:

    def __init__(self, *attrs):
        # a card is a simple 4-tuple of attributes
        # each attr is supposed to be either 0, 1 or 2
        self.attrs = attrs

    # most readable way to express what a SET is
    def isset(self, card1, card2):
        def allsame(v0, v1, v2):  # checks one attribute
            return v0 == v1 and v1 == v2

        def alldifferent(v0, v1, v2):  # checks one attribute
            return len({v0, v1, v2}) == 3

        return all(allsame(v0, v1, v2) or alldifferent(v0, v1, v2)
                   for (v0, v1, v2)
                   in zip(self.attrs, card1.attrs, card2.attrs))

    # all 81 possible cards
    @staticmethod
    def allcards():
        return [Card(att0, att1, att2, att3)
                for att0 in (0, 1, 2)
                for att1 in (0, 1, 2)
                for att2 in (0, 1, 2)
                for att3 in (0, 1, 2)
                ]

# Initialize a table with 12 random cards

'''
# Find and print all sets
sets_found = table.findsets_gnt()
print("\nSets found:")
for card in sets_found:
    print(card.attrs)
'''
def filename_to_card(filename):
    color_map = {"red": 0, "green": 1, "purple": 2}
    number_map = {"one": 0, "two": 1, "three": 2}
    shape_map = {"pill": 0, "tilda": 1, "diamond": 2}
    fill_map = {"empty": 0, "stripe": 1, "solid": 2}

    # Remove the file extension and split by underscore
    attributes = filename.rsplit(".", 1)[0].split("_")

    # Convert attributes to corresponding numerical values
    card_attrs = (
        color_map[attributes[0]],  # Color
        number_map[attributes[1]],  # Number
        shape_map[attributes[2]],  # Shape
        fill_map[attributes[3]]  # Fill
    )

    return Card(*card_attrs)

def card_to_filename(card):
    color_map = {0: "red", 1: "green", 2: "purple"}
    number_map = {0: "one", 1: "two", 2: "three"}
    shape_map = {0: "pill", 1: "tilda", 2: "diamond"}
    fill_map = {0: "empty", 1: "stripe", 2: "solid"}

    # Get the card's attributes
    color, number, shape, fill = card.attrs

    # Map the attributes back to their corresponding strings
    filename = f"{color_map[color]}_{number_map[number]}_{shape_map[shape]}_{fill_map[fill]}.png"

    return filename