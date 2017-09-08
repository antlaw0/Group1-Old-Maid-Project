class Hand(object):  #this class isn't necessary.  All the functions it needs to do can be done with ordinary built in functions of a list.
    # "A hand of playing cards"
    cards=[]
    def __init__(self):
        self.cards = []
    def __str__(self):
        #if self.cards:
            #playingCards = ""
            #for card in self.cards:
            #    playingCards += str(card) + " \t"
        if len(self.cards) >0:
            listInd=1
            for card in self.cards: #prints a numbered list of cards in hand
                print(listInd, " ",card)
                listInd=listInd+1
            #return "This string goes somewhere?"
        else:
            print("There are no cards left in your hand.  You win!")
            #return "Who uses this output?"

    def clear(self):
        # Im clearing all cards from hand #Why?
        self.cards = []

    def adding(self, card):
        #checked that we're trying to add a card (we are)
        self.cards.append(card)
        for ca in self:
            print(ca)

    def remove(self, card):
        self.cards.remove(card)

    def cardsLeft(self):
        return len(self.cards)

    def giving(self, card, otherHand):
        # A distributing method
        self.cards.remove(card)
        otherHand.add(card)