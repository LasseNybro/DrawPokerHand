class ResetDeck:

    f=open("Deck.txt","w") # Opens the file Deck.txt
    Suite=['H','S','C','D'] # Creates an array with the suites of the cards
    Value=['1','2','3','4','5','6','7','8','9','10','J','Q','K'] # Creates an array of the possible values of the cards
    for i in range(0,13): # Cycles through all the values and creates an entrance for each
         for j in range(0,4): # Cycles through all of the suites for each value
            if j<3:
                f.write("{0}{1} \t".format(Suite[j],Value[i])) # Writes to the Deck.txt file
            else:
                f.write("{0}{1} \r\n".format(Suite[j],Value[i])) # Makes sure the next value starts on a new line
    f.close() # Closes the file Deck.txt
