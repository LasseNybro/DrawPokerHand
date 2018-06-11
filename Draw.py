class Draw:
    import random
    import numpy

    def Draw():
        Deck=numpy.loadtxt('Deck.txt',dtype=str)
        Card='n/a'
        while Card == 'n/a':
            Suite=random.randint(0,3)
            Value=random.randint(0,12)
            Card=Deck[Value,Suite]
        Deck[Value,Suite]='n/a'
        numpy.savetxt('Deck.txt',Deck,delimiter=" ",newline="\n",fmt="%s")
        print(Card)
        return Card
