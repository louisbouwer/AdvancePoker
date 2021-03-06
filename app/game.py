# Created a new Deck object, store it in the instance variable deck. 
# Create a Player objects using the names in name1, and in future name2, etc. 
# The play_game method of the Game class manages the poker game. 
# There is a loop in the method that maintains the game as long 
# as the variable m response is not equal to q.
# Five cards are drawn each time in the loop within the play_game function. 

from deck import Deck
from player import Player
from treys import Card, Evaluator


class Game:
    def __init__(self):
        print("---- Start Poker Game ----")
        name1 = input("   Please type in Player's Name: ")
        # name2 = input("p2 name ")

        # Instantiate a deck object
        self.deck = Deck()
        self.deck.deck_count()
        print(f"\nGame: There are {len(self.deck.cards)} in the deck of cards\n")
        # Instantiate a player object with a name
        self.p1 = Player(name1)
        # self.p2 = Player(name2)

    # Main Function for the Game being called from main.py
    def play_game(self):
        print(" ---- Dealing 5 Cards per Player ---- \n")
        m = "   Press q to quit. Any key to play: \n"
        while m != "q":
            response = input(m)            
            if response == 'q' or int(self.deck.deck_count()) < 5:
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
            # print(f"Hand second card suite initial is: {hand[1].value[0]}")
            print(f"Hand second card suit is: {hand[1].suit}")
            print(f"Top card on deck is: {self.deck.cards[0]}")
            print("---- End of Print Testing ----\n")
            
            # Analyze hand
            print("---- Start Poker Hand Analyzer Testing ----")
        
            # The parent class Evaluator requires two values for evaluate
            # the values all_cards and board
            # for this purpose board will be set as empty
            # Can rewrite the class Evaluator in future

            evaluator = Evaluator()
            
            # Must translate existing hand to all_card codes

            evalsuits = ["s", "h", "d", "c"]

            evalvalues = ["None0", "None1", "2", "3",
              "4", "5", "6", "7",
              "8", "9", "T",
              "J", "Q", "K", "A"]

            print(" -----  Testing Card Translator for Card Evaluator ---- ")
            handcard = []
            for i in range(0,5):
                print(f"value of i is: {i}")
                print(f"Code for {i} evalcard is: {evalvalues[hand[i].value]}{evalsuits[hand[i].suit]}")
                handcardvalue = evalvalues[hand[i].value]
                handcardsuit = evalsuits[hand[i].suit]
                handcard.append(handcardvalue + handcardsuit)
                print(f"handcardvalue: {handcardvalue} and handcardsuit: {handcardsuit}")
                print(f"handcard {i} is: {handcard[i]}")
                print(f"complete list of handcard is: {handcard}")

            # Poker hand requires 5 cards
            ahand = [
                Card.new(handcard[0]),
                Card.new(handcard[1]),
                Card.new(handcard[2]),
                Card.new(handcard[3]),
                Card.new(handcard[4])
                ]

            # For this poker version there is no cards on the table
            aboard = []

            print("\n---- Poker Hand Analyzer Final Results ----")
            print(f"   Evaluator score: {evaluator.evaluate(ahand, aboard)}")
            print(f"   Evaluator rank class: {evaluator.get_rank_class(evaluator.evaluate(ahand, aboard))}")
            rank_class = evaluator.get_rank_class(evaluator.evaluate(ahand, aboard))
            print(f"   Evaluator rank_class input value: {rank_class}")
            print(f"   Poker hand class: *** {evaluator.class_to_string(rank_class)} ***")
            print("---- End Analyzer Testing ----\n")

            print("---- Remaining Cards in the Deck ----\n")
            self.deck.deck_count()

