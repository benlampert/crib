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
	
