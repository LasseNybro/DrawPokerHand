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

#The Code below is supposed to figure out which hand you have from the 5 cards above, although it is a lot of if statements...

#if Flush==1 and Straight==1
#	print("You got a Royal Straight Flush, amazing!")
#if FoaK==1
#	print("You've got four %d's", SameValue)
#if House==1
#	print("You've got 3 %d's and 2 %d's, that's a House",SameValue,SecondValue)
#if Flush==1
#	print("You've got a Flush, congrats")
#if Straight==1
#	print("You've got a Straight")
#if ToaK==1
#	print("You've got 3 %d's!", SameValue)
#if TwoPairs==1
#	print("You've got 2 pairs, one is %d's and the other is %d's",Pair1,Pair2)
#if Pair==1
#	print("You've got a pair of %d's, lucky you",SameValue)
#else
#	print("You've got the high card %d, too bad",HighCard)
