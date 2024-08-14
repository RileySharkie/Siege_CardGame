import csv
from dataclasses import dataclass
from itertools import chain
from pygame_cards.abstract import AbstractCard

@dataclass
class siegeCard(AbstractCard):
    defense: int
    effect: str 
    goldValue: int
    leatherValue: int
    woodValue: int
    stoneValue: int
    ironValue: int
    prestiegeValue: int
    canFight: bool
    might: int
    morale: int
    count: int
    deck: int

loadedDecks = ['wild']
enabledDecks = dict()

# Start making cards from relevant csvfiles
# Load card file
for deck in loadedDecks:
    filename = (deck + "Deck.csv") 

# open and read the file
# place the first row as a list of field headings in 'fields'
# then add the remaining rows to list 'rows' (a list of lists!)
    fields = []
    rows = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
#Begin assembling all cards into enabledDecks
    for row in rows:
        newestCard = siegeCard(*row, deck)
        if newestCard.deck in enabledDecks:
            enabledDecks[newestCard.deck] += newestCard
        else:
            enabledDecks[newestCard.deck] = [newestCard]


print(enabledDecks)