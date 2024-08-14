import csv
from dataclasses import dataclass
from pygame_cards.abstract import AbstractCard
from pygame_cards.set import CardsSet
from pprint import pprint

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

loadedDecks = ['wild', 'unit']
enabledDecks: dict[str, CardsSet] = dict()
# Start making cards from relevant csvfiles
# Load card file
for deck in loadedDecks:
    filename = (deck + "Deck.csv") 
    enabledDecks[deck] = CardsSet()

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
        newestCard = siegeCard(*row)
        # Append to corresponding deck
        enabledDecks[deck].append(newestCard)


pprint(enabledDecks)
