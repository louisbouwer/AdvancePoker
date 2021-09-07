# Create a new Deck object, store it in the instance variable deck, 
# and create two Player objects using the names in name1 and name2. 
# The play_game method of the Game class starts the game. 
# There is a loop in the method that maintains the game as long 
# as there are two or more cards left in the deck, and 
# as long as the variable response is not equal to q .
# Two cards are drawn each time in the loop and the play_game method 
# assigns the first card to p1 and the second card to p2.

from deck import Deck
from player import Player
from treys import Card, Evaluator


class Game:
    def __init__(self):
        name1 = input("p1 name ")
        # name2 = input("p2 name ")

        # Instantiate a deck object
        self.deck = Deck()

        # Instantiate a player object with a name
        self.p1 = Player(name1)
        # self.p2 = Player(name2)

    # Main Function for the Game being called from main.py
    def play_game(self):
        print(" ---- Dealing 5 Cards per Player ---- \n")
        m = "Press q to quit. Any key to play: \n"
        while m != "q":
            response = input(m)            
            if response == 'q':
                break

            # Create a Poker Hand with 5 Cards
            hand = []
            for i in range(0,5):
                print(f"value of i is: {i}")
                # Ensure we remove cards from the deck
                hand.append(self.deck.rm_card())
                print(f"The {i+1} card drawn from the deck: {hand[i]}")

            print(f"The full hand: {hand} \n")
            
            # Test printing of cards to create a hand
            print("---- Testing Card Values ----")
            print(f"Hand second card is: {hand[1]}")
            print(f"Hand second card value is: {hand[1].value}")
            print(f"Hand second card suit is: {hand[1].suit}")
            print(f"Top card on deck is: {self.deck.cards[0]}")
            print("---- End of Print Testing ----\n")
            
            # Analyze hand
            print("---- Start Hand Analyzer Testing ----")
        
            # The parent class Evaluator requires two values for evaluate
            # the values all_cards and board
            # for this purpose board will be set as empty
            # Can rewrite the class Evaluator in future

            evaluator = Evaluator()
            board = []

            # Must translate existing hand to all_card codes

            

            all_cards = [ 
                Card.new('Qs'),
                Card.new('Th'),
                Card.new('Th'),
                Card.new('Th'),
                Card.new('Th')
            ]
            print(evaluator.evaluate(all_cards, board))
            print(evaluator.get_rank_class(evaluator.evaluate(all_cards, board)))
            print(evaluator.class_to_string(2))
            print("---- End Analyzer Testing ----\n")

            p1n = self.p1.name


