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

'''
dealt_cards = Deal(MakeDeck(), 4)

for player in dealt_cards:
	for card in dealt_cards[player]:
		print ('Player ' + str(player + 1) + ', Suit: ' + str(card.suit) + ', Value: ' + str(card.value))
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
