import Card2
import random

class Deck(object):
    # """ A deck of playing cards. """
    RANKS = [1,2,3,4,5,6,7,8,9,10,11,12,13] #H
    SUITS = ["C", "D", "H", "S"]
    cardsLeft=53
    def __init__(self):
        self.deck = {}
        count=0
        for suit in Deck.SUITS:
            for rank in Deck.RANKS:
                count=count+1 #H added
                #print("suit is ",suit," rank is ",rank)
                card = Card2.Card(rank, suit) #make cards
                #print("I tried to make a card and I made a ", type(card))
                #print("the card is ",card)

                #self.deck[rank + ' ' + suit] = card ##this is not the right syntax for adding cards to dictionary
                self.deck[count]= card #count is unique number for key (1-53(not 52 because we need an extra card)), value is card
                #print(self.deck.keys())
                #c=self.deck.values()
                #print(c)
        oldMaid=Card2.Card(14,"Old Maid")
        self.deck[53]=oldMaid # add the old maid card
#        k=1
#        for i in self.deck:
#            print(str(k)+"\t"+str(self.deck[i]))
#            k=k+1

    def decreaseCardsLeft(self):
        self.cardsLeft=self.cardsLeft-1

    def getCardsLeft(self):
        return self.cardsLeft


    def deal(self): ##This is a bad way to deal a deck.  It does not really randomize the deck at all.
        # If you look at your hand, you have alternate cards with the other player.  Ie you always get the same hand.
        if self.cardsLeft >0:
            k=random.choice(list(self.deck.keys()))

            a=self.deck.pop(k)#this returns a tuple.  we only want the second item in the tuple,
            # which is the value from the key value pair we took out of the dictionary.
            #so...
            return a

        #this method works much better for actually randomizing the deck

#        print("cards left ", self.getCardsLeft())
#        while self.getCardsLeft() >0:
#            r=random.randint(0, self.getCardsLeft())
#            if r in self.deck:
#                print("cards left ", self.getCardsLeft())
#                card=self.deck[r]
#                del self.deck[r]
#                self.decreaseCardsLeft()
#                return card
#            elif r+1 in self.deck:
#                print("cards left ", self.getCardsLeft())
#                card=self.deck[r+1]
#                del self.deck[r+1]
#                self.decreaseCardsLeft()
#                return card
#            elif r-1 in self.deck:
#                print("cards left ", self.getCardsLeft())
#                card=self.deck[r-1]
#                del self.deck[r-1]
#                self.decreaseCardsLeft()
#                return card
