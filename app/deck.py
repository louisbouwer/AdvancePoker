from random import shuffle
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def deck_count(self):
        deck_total_count = len(self.cards)
        print(f"\nDeck: There are {deck_total_count} in the deck of cards\n")
        return deck_total_count

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()   # pop() ==> Remove and return item at index (default last).

