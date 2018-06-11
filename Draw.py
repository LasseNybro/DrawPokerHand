class Draw:

    def __init__(self):
        import random # Imports the packages random and numpy
        import numpy
        Deck=numpy.loadtxt('Deck.txt',dtype=str) # Loads Deck.txt onto the Deck variable
        Card='n/a' # Starting value of Card in order for the while loop to run
        while Card == 'n/a': # The while loop runs until a unique card is drawn
            Suite=random.randint(0,3) # Randomly chooses a Suite for the card
            Value=random.randint(0,12) # Randomly chooses a Value for the card
            Card=Deck[Value,Suite] # Finds the randomly chosen card
        Deck[Value,Suite]='n/a' # Sets drawn cards' value to "n/a" in order to get unique cards and not multiples
        numpy.savetxt('Deck.txt',Deck,delimiter=" ",newline="\n",fmt="%s") # Writes the "n/a" into the Deck.txt file
        self.Card=Card # Makes it possible to return the Card outside the class
