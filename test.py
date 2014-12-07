import crib


#this is a test method to make sure each card in deck is unique
def allUnique(deck):
    seen = set()
    return not any(i in seen or seen.add(i) for i in deck)

#create a deck of cards
deck = crib.deck
#shuffle the deck of cards
sDeck = crib.shuffleDeck(deck)

#print 'this is a complete deck of cards'
#print sDeck
print 'there are %s cards in the deck' % len(sDeck)
print 'are the cards in the deck unique? %s ' % allUnique(sDeck)

#print allUnique(sDeck)
#tests for number of cards in each hand
handA, handB, cDeck = crib.dealCards(sDeck, 6)
print 'handA has %s cards' % len(handA)
print 'handB has %s cards' % len(handB)
print 'remaining cards in the deck should be 40, and there are %s cards in the deck' % len(cDeck)

