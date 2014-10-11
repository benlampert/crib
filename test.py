import crib

#this is a test method to make sure each card in deck is unique
def allUnique(deck):
    seen = set()
    return not any(i in seen or seen.add(i) for i in deck)

#create a deck of cards
deck = crib.deck

#shuffled_deck = crib.shuffleDeck(deck)


sDeck = crib.shuffleDeck(deck)
print 'this is a complete deck of cards'
print sDeck
<<<<<<< HEAD
print 'there are %s cards in the deck' % len(sDeck)
print 'are the cards in the deck unique? %s ' % allUnique(sDeck)

=======
print allUnique(sDeck)
>>>>>>> fabb80236744a745d9a2a4f3b774259fa78caaa2
