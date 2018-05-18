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

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 1

    def add_card(self, card):
        '''
        Increases the value of the hand by the 
        rank of the card added. If the card is
        an Ace increment the value of aces by 1
        '''
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        '''
        If the hand contains an ace and the player
        goes over 21, the value of the player is reduced
        by 10 and the value of aces is also decremented by 1
        '''
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():
    '''
    A class representing chips in the game.
    '''

    def __init__(self):
        self.total = 100 # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
   
def take_bet(chips):
    '''
    This functions takes chip object as input 
    and takes bets from the player.
    '''
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet ? "))
        except ValueError:
            print("please enter integer")
        else:
            if chips.bet > chips.total:
                print("Sorry you don't have enough chips, you have {}".format(chips.total))
            else:
                break

def hit(deck, hand): 
    '''
    Takes Deck and Hand objects as arguments.
    Deals one card off the deck and adds it to
    the hand. Checks for aces in the even a player's
    hand exceeds 21
    '''
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    '''
    Prompts player to Hit or Stand
    Accepts deck and player's hand as argument.
    Assigns 'playing' as a Global variable.
    If the player hits, executes the hit() function
    If the player stands, set the 'playing variable to false
    '''
    global PLAYING
    player_input = (input("Would you like to Hit or Stand? Enter H or S ")).upper()
    if player_input == "H":
        hit(deck, hand)
        PLAYING = True
    else:
        PLAYING = False



my_deck = Deck()
player = Hand()
hit_or_stand(my_deck, player)