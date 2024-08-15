import csv
import sys
from dataclasses import dataclass
from functools import cached_property
from pprint import pprint
from time import sleep

import pygame
from pygame_cards.abstract import AbstractCard, AbstractCardGraphics
from pygame_cards.set import CardsSet
from pygame_cards.utils import position_for_centering
# from pygame_cards.deck import Deck
from pygame_cards.hands import HorizontalPileGraphic

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
    

@dataclass
class siegeCardGraphics(AbstractCardGraphics):
    @cached_property
    def surface(self) -> pygame.Surface:
        surf = pygame.Surface(self.size)
        surf.fill(pygame.Color(20, 20, 20, 20))
        surf.fill(pygame.Color(30, 30, 30), pygame.Rect(2, 2, surf.get_width() - 4, surf.get_height() - 4))
        font = pygame.font.SysFont("urwgothic", 20)
        name = font.render(self.card.name, True, pygame.Color(163, 146, 139))
        # Make sure the name is centered in the x direction.
        surf.blit(name, (position_for_centering(name, surf)[0], 10))
        return surf

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
        newestCard.graphics = siegeCardGraphics(newestCard)
        # Append to corresponding deck
        enabledDecks[deck].append(newestCard)

player_hand = CardsSet()



if __name__ == "__main__":
    # A very simple game loop to show the cards
    pygame.init()

    size = width, height = 800, 600

    screen = pygame.display.set_mode(size)
    screen.fill("black") 
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if(event.unicode == 'w'):
                    if(len(enabledDecks['wild']) > 0):
                        player_hand.append(enabledDecks['wild'].pop())
                elif(event.unicode == 's'):
                    enabledDecks['wild'].shuffle()
                
        pygame.display.flip()
        
        # player_hand.append(enabledDecks['wild'].draw(0))
        # print(len(player_hand))
        
        
        draw_pile_display = HorizontalPileGraphic(enabledDecks['wild'])
        hand_display = HorizontalPileGraphic(player_hand, size=(1200, 200), card_size=(100, 200))
        screen.fill("black") 
        screen.blit(draw_pile_display.surface, (50, 100))
        screen.blit(hand_display.surface, (50, 325))
        
        # Make sure you don't burn your cpu
        sleep(0.1)
