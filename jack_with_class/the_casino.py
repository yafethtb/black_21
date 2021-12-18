import random
from card_stack import deck

class Player:
    def __init__(self, stack= deck):        
        self.stack = stack

    def account(self):
        '''Showing account'''
        self.account = int(input("Please input your chip total values: > $ "))
 
    def hand(self, card):
        '''Draw and keep cards in hand'''
        return [random.choice(list(self.stack.keys())) for i in range(0, card)]
    
    def value(self, hand):
        '''Counting value of the cards in hand.'''
        val = sum([self.stack[i] for i in hand])
        if 'A' in hand and val > 21:
            val -= 10
        return val
    
    def dealing(self,card):
        '''Drawing cards and counting their values. The number of card when first dealing must be 2.'''
        hand = self.hand(card)
        value = self.value(hand)
        return hand, value
    
    def add(self, hand):
        ''' Adding a card to hand if the hand's value is under 20.'''
        new_hand = self.hand(card = 1)
        hand += new_hand
        val = self.value(hand)
        if 'A' in hand and val > 21:
            val -= 10
        return hand, val
        # new_hand, new_val = self.dealing(1)        
        # hand += new_hand
        # val += new_val     
        # return hand, val
    
    def play(self, dealing, add, bid):
        '''Checking if the player automatically lose or win. If both terms are unsatisfied, execute add or stand.'''
        hand, value = dealing(2)
        while True:
            if value == 21:
                print(f"Your hand is {hand}. Blackjack!")
                self.account += bid
                print('-' * 20)
                break            
            elif value > 21:
                print(f"Your hand is {hand}. Your value is {value}.")
                self.account -= bid
                print('-' * 20)
                break
            else:
                print(f"Your hand is {hand}. It's under 21. Want to draw? press y to draw, other keys to not draw. ")
                answer = input('>  ').lower()
                if answer == 'y' or answer == 'yes':
                    print("You draw a card")                    
                    hand, value = add(hand)                                    
                    print('-' * 20)
                else:
                    print("Understood.")
                    print('-' * 20)
                    break
        return value

class Dealer(Player):
    def dealer_play(self, dealing, add):
        '''Checking if the dealer automatically lose or win. If value under 17, execute add.'''
        hand, value = dealing(2)
        while True:
            if value == 21:
                print(f"Dealer hand is {hand}. It's 21. Blackjack!")               
                return value                
            elif value > 21:
                print(f"Dealer hand is {hand}, with value {value}. Dealer lose.")
                return value
            elif value <= 17:
                print(f"Dealer hand is {hand}, with value {value}. Dealer will draw a card.")
                hand, value = add(hand)
                continue
            else:
                print(f"Dealer hand is {hand}, with value {value}.")
                return value
                
        
        
