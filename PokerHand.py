from ResetDeck import * # Imports the Reset function for Deck.txt
from Draw import * # Imports the Draw class which allows us to draw cards from Deck.txt

ResetDeck() # Resets Deck.txt to default

Card=Draw() # Draws a card using the class Draw
Card1=Card.Card # Turns the card drawn over to Card1
Card=Draw()
Card2=Card.Card
Card=Draw()
Card3=Card.Card
Card=Draw()
Card4=Card.Card
Card=Draw()
Card5=Card.Card

print([Card1,Card2,Card3,Card4,Card5]) # Prints the 5 cards drawn
