#The Player class has three instance variables: 
# wins to keep track of the number of turns a player has won, 
# card to represent the card a player currently holds, 
# and name to keep track of a player’s name.

class Player:
   def __init__(self, name):
       self.wins = 0
       self.card = None
       self.name = name
