from random import shuffle
class Card(object):
 def _init_(self,suit,rank):
  self.suit = suit
  self.rank = rank
 suit_name = ['Clubs','Diamond','Hearts','Spades']
 rank_name = [None,'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
 def _str_(self):
  return '%s of %s' % (Card.rank_names[self.rank].Card.suit_names[self.suit])
 def _repr_(self):
  return (self.rank_names[self.rank],self.suit_names[self.suit])
 def _lt_(self,other):
  return self.rank<other.rank
 def _gt_(self,other):
  return self.rank>other.rank
 def _eq_(self,other):
  return self.rank == self.other
class Deck(object):
 def _init_(self):
  self.Cards = [Card(suit,rank) for suit in range(4) for rank in range(0,13)]
 def _str_(self):
  return '\n'.join([str(Card) for Card in self.Cards])  
 def _len_(self):
  return len(self.Cards)
 def sort(self):
  self.cards.sort()
deck = Deck()
deck.sort()
print(deck)
