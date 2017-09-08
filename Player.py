class Player(object):

	def __init__(self, name, hand):
		self.name = name
		self.hand = hand
		self.pairs = 0

#	def find_pairs(self):
#		a=0
#		b=0
#		for i in self.hand.cards:
#			a=0
#			b=0
#			a+=1
#			for ii in self.hand.cards:
#				b+=1
#				if a != b:
#					if i.rank == ii.rank:
#						self.pairs.append(i)
#						self.hand.cards.remove(i)
#						self.hand.cards.remove(ii)
	def pairsInc(self):
		self.pairs=self.pairs+1



	def find_pairs(self):#this method compares each card in the hand to every other card to look for matches and increments pairs when it finds one
#TODO This leaves behind the second and sixth card of each suit, even if they have a match in the hand.
		for i in self.hand:
			#print("i is a ",type(i), " and it's value is, ",i)
			#print("i's rank is:", i.getRank)
			for ii in self.hand:
				#print("ii is a ",type(ii), " and it's value is ",ii)
				if (i.getRank() == ii.getRank()) & (i.getSuit() !=ii.getSuit()) : #compare each card's rank with every other card in the hand's rank and make pair if rank matches and card doesn't (ie not the same card)
					#print("i's rank is ", i.getRank(), " and ii's rank is ", ii.getRank())
					#self.pairs =self.pairs+1
					self.pairsInc()
					#for o in self.hand:
						#print ("o is ",type(o)," ",o)
					#print(" i is ", i, " ii is ",ii)
					self.hand.pop(self.hand.index(i)) #remove first half of pair
					self.hand.pop(self.hand.index(ii)) #remove second half of pair
					return
				else:
					#print (i, ii)#, self.hand.index(i), self.hand.index(ii))
					print("cards in hand: ",len(self.hand))
		print(self.name, " has ", self.pairs)
		return
	def getPairs(self):
		return self.pairs

	def showHand(self):
		count=1
		for i in self.hand:
			print(str(count)+"\t"+str(i))
			count=count+1

	def passCard(self, player2, card):
		# A distributing method
		self.hand.remove(card)
		player2.hand.append(card)