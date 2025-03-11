'''
This program contains the logic for encoding Set cards and finding sets, as well as file conversion
The Table and Card classes are from https://sanderevers.github.io/2019/09/11/finding-sets.html
'''

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

'''
Converts a given filename to a Card object
    filename: the filename to be converted
    return: the Card object with associated attributes
'''
def filename_to_card(filename):
    color_map = {"red": 0, "green": 1, "purple": 2}
    number_map = {"one": 0, "two": 1, "three": 2}
    shape_map = {"pill": 0, "tilda": 1, "diamond": 2}
    fill_map = {"empty": 0, "stripe": 1, "solid": 2}

    #Trims the file path and splits by underscore, then encodes attributes
    attributes = filename.rsplit(".", 1)[0].split("_")
    card_attrs = (
        color_map[attributes[0]],
        number_map[attributes[1]],
        shape_map[attributes[2]],
        fill_map[attributes[3]]
    )

    return Card(*card_attrs)

'''
Converts a given Card object to a filename
    filename: the filename to be converted
    return: the filename associated with the Card object
'''
def card_to_filename(card):
    color_map = {0: "red", 1: "green", 2: "purple"}
    number_map = {0: "one", 1: "two", 2: "three"}
    shape_map = {0: "pill", 1: "tilda", 2: "diamond"}
    fill_map = {0: "empty", 1: "stripe", 2: "solid"}
    color, number, shape, fill = card.attrs

    #Converts attributes to strings to create filename
    filename = f"{color_map[color]}_{number_map[number]}_{shape_map[shape]}_{fill_map[fill]}.png"
    return filename