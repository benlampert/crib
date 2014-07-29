import crib

def allUnique(deck):
    seen = set()
    return not any(i in seen or seen.add(i) for i in deck)

deck = crib.deck
print allUnique(deck)
sDeck = crib.shuffleDeck(deck)
#shuffled_deck = crib.shuffleDeck(deck)
#print shuffled_deck

print allUnique(sDeck)

#print allUnique(shuffled_deck)
=======
deck = crib.createDeck()
print crib.shuffleDeck(deck)



