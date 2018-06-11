class ResetDeck:

    f=open("Deck.txt","w") # Opens the file
    Suite=['H','S','C','D'] # Creates an array with the suites of the cards
    Value=['1','2','3','4','5','6','7','8','9','10','J','Q','K'] # Creates an array of the possible values of the cards
    for i in range(0,13): # Runs through all the suites and creates an entrance for each
         for j in range(0,4): # Runs through all the values of the cards inside each of the suites to create a card with all values for each suite
            if j<3:
                f.write("{0}{1} \t".format(Suite[j],Value[i])) # Writes to the Deck.txt file
            else:
                print("newline")
                f.write("{0}{1} \r\n".format(Suite[j],Value[i])) # Makes sure the next suite starts on a new line
    f.close() # Closes the file

