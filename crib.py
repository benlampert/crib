deck = [
	'As', '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', '11s', 'Js', 'Qs', 'Ks',
	'Ad', '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', '11d', 'Jd', 'Qd', 'Kd',
	'Ah', '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', '11h', 'Jh', 'Qh', 'Kh',
	'Ac', '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', '11c', 'Jc', 'Qc', 'Kc'
	]

from random import randrange	

def shuffleDeck(deck, sDeck=[]):

#take length of deck
#find a rand num in that range
#add that value to a new shuffled array
#delete that value from the old deck
	while len(sDeck)<52:
		value = randrange(len(deck))
		sDeck.append(deck[value])
		del deck[value]
	return sDeck
	
def dealCards(deck, numCards):
#numCards becomes the iterator
#create two hands that will be returned with the cards
#return the cards
	handA = []
	handB = []

	for i in range(numCards):
		handA.append( deck.pop())
		handB.append( deck.pop())	
	return (handA, handB, deck)

def pickCrib(handA, handB):
#interact to pick two cards and delete those from the hand list return the two hands
	thecrib = []
	print handA
	firstCard = input("A pick first card")
	thecrib.append(handA[firstCard])
	del handA[firstCard]
	print handA
	secondCard = input("A pick second card")
	thecrib.append(handA[secondCard])
	del handA[secondCard]
	thecrib.append(handB[firstCard])
	del handB[firstCard]
	thecrib.append(handB[secondCard])
	del handB[secondCard]
	
	return [handA, handB, thecrib]

