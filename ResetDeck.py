file=open("Deck.txt","w") # Opens the file
Suite=['H','S','C','D'] # Creates an array with the suites of the cards
Value=['1','2','3','4','5','6','7','8','9','10','J','Q','K'] # Creates an array of the possible values of the cards
for j=0:3: # Runs through all the suites and creates an entrance for each
  for i=0:12: # Runs through all the values of the cards inside each of the suites to create a card with all values for each suite
    if i<12:
      write('\t',Suite(j),Value(i)) # Writes to the Deck.txt file
    else
      write('\n',Suite(j),Value(i)) # Makes sure the next suite starts on a new line
file.close() # Closes the file
