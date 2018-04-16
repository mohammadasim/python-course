import random
'''
Declared variables to be used in this project
'''
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'king': 10, 'Ace':11}
playing = True

class Card():
    '''
    This class represents a card in the game.
    Each instance of the class has attributes
    suit and rank
    '''

    def __init__(self, suit, rank):
        '''
        init method to instantiate
        instance of Card class

        '''
        self.suit = suit
        self.rank = rank

    def __str__(self):
        '''
        Method to print suit and rank 
        of the insance of the class
        '''
        return self.rank + " of " + self.suit

class Deck():
    '''
    This class represents the deck
    in the game with variable cards
    the represents the 52 cards in 
    this game.
    '''

    def __init__(self):
        '''
        This method initialises a deck of cards
        For each suit of cards the correct set of
        ranks will be initialised.
        '''
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        '''
        This method returns the suit and rank of
        52 cards in the deck
        '''
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return deck_comp

    def shuffle(self):
        '''
        Method to shuffle the cards in the deck
        '''
        random.shuffle(self.deck)

    


    

