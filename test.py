import crib

def allUnique(deck):
    seen = set()
    return not any(i in seen or seen.add(i) for i in deck)

deck = crib.deck
print allUnique(deck)
#shuffled_deck = crib.shuffleDeck(deck)


sDeck = crib.shuffleDeck(deck)
print sDeck
print allUnique(sDeck)
print 'test'
