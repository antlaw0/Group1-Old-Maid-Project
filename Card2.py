class Card(object):
    #A playing card
    def __init__(self, rank, suits):
        self.rank = rank
        self.suit = suits
        self.isFaceUp = False

    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit

    def flip(self): ##why do we need this method?
        self.isFaceUp = not self.isFaceUp

    def cardString(self): ##if you do this, you can use numbers for the rank of the cards which is much easier to match.
                          ##whenever the card needs to be displayed, simply call this method


        if self.suit == "C": suit = '\u2663'
        elif self.suit == "D": suit = '\u2662'
        elif self.suit == "H": suit = '\u2661'
        elif self.suit == "S": suit = '\u2660'
        else: suit="Old Maid"

        if self.rank ==1:
            s= "Ace of "+ suit
        elif self.rank ==11:
            s= "Jack of "+ suit
        elif self.rank == 12:
            s= "Queen of "+ suit
        elif self.rank == 13:
            s = "King of "+ suit
        elif self.rank == 14:
            s = suit #The old maid card
        else:
            s = str(self.rank)+ " of " + suit
        #print(s)
        #print("type of s is ",type(s))
        return s

    def __str__(self):
#        if self.isFaceUp :
#            display_card = self.rank + ' of ' + self.suit
#        else:
#            display_card = "Card face down"
#        return display_card
        return self.cardString() #use function to identify proper string for display
        #print("n is type ",type(n))
        #return n
