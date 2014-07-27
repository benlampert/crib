suits = ['s','h','d','c']
values =['A', 1, 2,3,4,5,6,7,8,9,10,'J','Q','K']

def createDeck():
	deck = []
	card = ''
	for suit in suits:
		for value in values:
			card = str(value)+suit
			deck.append(card)
	return deck

from random import randrange	

def shuffleDeck(deck):
	sDeck = []
	for card in deck:
		sDeck.append(deck[randrange(len(deck))])
	return sDeck