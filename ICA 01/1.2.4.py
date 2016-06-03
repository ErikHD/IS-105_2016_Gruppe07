#!/usr/bin/python3.4

from enum import Enum
from random import shuffle
from collections import defaultdict
import unittest

class Suit(Enum):
	Clubs = 1
	Diamonds = 2
	Hearts = 3
	Spaces = 4

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

def MakeDeck():
	deck = []
	for suit in Suit:
		for value in range(1, 14):
			deck.append(Card(suit, value))
	return deck

def Deal(deck, players):
	assert(players < 10)

	shuffle(deck)
	player_cards = defaultdict(list)
	for player in range(0, players):
		for card in range(0, 5):
			player_cards[player].append(deck.pop())
	return player_cards

class HandValue(Enum):
	High_Card = 1
	One_Pair = 2
	Two_Pair = 3
	Three_Of_A_Kind = 4
	Straight = 5
	Flush = 6
	Full_House = 7
	Four_Of_A_Kind = 8
	Straight_Flush = 9

	def _IsStraightFlush(hand):
		return HandValue._IsFlush(hand) and HandValue._IsStraight(hand)

	def _IsXOfAKind(x, hand):
		for value in range(1, 14):
			if sum(1 for x in hand if x.value == value) == x:
				return True
		return False

	def _IsFullHouse(hand):
		hand = [x for x in sorted(hand, key=lambda x: x.value)]
		val = [ sum(1 for x in hand if x.value == hand[0].value), sum(1 for x in hand if x.value == hand[4].value) ]
		if 2 in val and 3 in val:
			return True
		return False

	def _IsFlush(hand):
		return all(x.suit == hand[0].suit for x in hand)

	def _IsStraight(hand):
		hand = [x for x in sorted(hand, key=lambda x: x.value)]
		for i, v in zip(range(0, 5), range(hand[0].value, hand[0].value + 5)):
			if hand[i].value != v:
				return False
		return True

	def _IsXPair(x, hand):
		hand = [x for x in sorted(hand, key=lambda x: x.value)]
		pairs = 0
		while len(hand):
			if sum(1 for x in hand if x.value == hand[0].value) >= 2:
				pairs += 1
			hand = [x for x in hand if x.value != hand[0].value]
		return pairs >= x

	def CardRank(hand):
		return [x.value for x in sorted(hand, key=lambda x: x.value)]

	def Evaluate(hand):
		if HandValue._IsStraightFlush(hand): return HandValue.Straight_Flush
		if HandValue._IsXOfAKind(4, hand): return HandValue.Four_Of_A_Kind
		if HandValue._IsFullHouse(hand): return HandValue.Full_House
		if HandValue._IsFlush(hand): return HandValue._IsFlush
		if HandValue._IsXOfAKind(3, hand): return HandValue.Three_Of_A_Kind
		if HandValue._IsXPair(2, hand): return HandValue.Two_Pair
		if HandValue._IsXPair(1, hand): return HandValue.One_Pair
		return HandValue.High_Card



'''
dealt_cards = Deal(MakeDeck(), 4)

for player in dealt_cards:
	for card in dealt_cards[player]:
		print ('Player ' + str(player + 1) + ', Suit: ' + str(card.suit) + ', Value: ' + str(card.value))
'''
'''
class TestPoker(unittest.TestCase):
	def test_rightNumberPlayers(self):
		dealt_cards = Deal(MakeDeck(), 4)
		self.assertEqual(len(dealt_cards), 4)

	def test_rightNumberCards(self):
		dealt_cards = Deal(MakeDeck(), 4)
		for player in dealt_cards:
			self.assertEqual(len(dealt_cards[player]), 5)

if __name__ == '__main__':
	unittest.main()
'''
