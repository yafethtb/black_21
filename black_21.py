import random

# ---- INITIALIZATION ----
# Cards
the_card = {
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10": 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10,
    "A" : 11,
}

# Initial account
initial = int(input("How many dollars you bring to the table?  $"))

# ---- Functions ----
# ---- Betting function ----
def bet(acc):
    ''' Betting function '''
    while True:
        your_bet = int(input("How many you willing to bet?  $"))
        if your_bet > acc:
            print("Your bet is higher than your account. Please repeat all.")
            continue
        else:            
            return your_bet

# ---- Draw cards ----
def dealing(cards):
    ''' Dealing card function. Return card lists and their value. '''
    print("Game start.")
    your_card = [random.choice(list(cards.keys())) for i in range(0, 2)] 
    your_val =  sum(cards[i] for i in your_card)
    dealer_card = [random.choice(list(cards.keys())) for i in range(0, 2)]
    dealer_val = sum(cards[i] for i in dealer_card)
    return your_card, your_val, dealer_card, dealer_val

# ---- Adding card ----
def add_card(hand, cards):
    '''Draw another card '''    
    new_card = random.choice(list(cards.keys())) 
    hand.append(new_card)
    new_val = sum(cards[i] for i in hand)
    return hand, new_val

# ---- Compare hands ----
# !--- open_hand() returns None ---!
def open_hand(hand, hand_val, dealer_hand, dealer_val, acc, bet, cards):
    ''' Checking both hands' cards value. Return user money amount.'''
    if dealer_val <= 17:
        # Triggered when the dealer's hand is under 17.
        # !--- Open_hand() is not triggered ---!
        print("Dealer's hand value is under 17. Dealer will draw another card.")
        new_dealer_hand, new_dealer_val = add_card(dealer_hand, cards)
        open_hand(hand, hand_val, new_dealer_hand, new_dealer_val, acc, bet, cards)
    elif hand_val > 21 and dealer_val > 21:
        # Will be triggered when your hand is more than 21.
        print(f'Your hand is {hand} with value {hand_val}.\nDealer cards are{dealer_hand} with value {dealer_val}.')
        print("Both hands are over 21. It's draw.")        
    elif hand_val > 21 and dealer_val < 21:
        # Will be triggered if user hand is over 21 and dealer's hand is under 21.
        acc -= bet
        print(f'Your hand is {hand} with value {hand_val}.\nDealer cards are{dealer_hand} with value {dealer_val}.')
        print(f"You lose. Your money now is ${acc}.")        
    elif hand_val < 21 and dealer_val > 21:
        # Will be triggered if
        acc += bet
        print(f'Your hand is {hand} with value {hand_val}.\nDealer cards are{dealer_hand} with value {dealer_val}.')
        print(f"You win! Your money now is ${acc}.")        
    elif hand_val < 21 and dealer_val < 21:
        # Triggered when both hands are under 21.
        # Whoever have higher hand, wins.
        if hand_val < dealer_val:
            acc -= bet
            print(f'Your hand is {hand} with value {hand_val}.\nDealer cards are{dealer_hand} with value {dealer_val}.')
            print(f"You lose. Your money now is ${acc}.")            
        elif hand_val > dealer_val:
            acc += bet
            print(f'Your hand is {hand} with value {hand_val}.\nDealer cards are{dealer_hand} with value {dealer_val}.')
            print(f"You win! Your money now is ${acc}.")            
        elif hand_val == dealer_val:
            print(f'Your hand is {hand} with value {hand_val}.\nDealer cards are{dealer_hand} with value {dealer_val}.')
            print("Both hands are same. It's draw.")
        
    return acc

# --- Control if user will stop or continue.
def if_continue(money, cards):
    if money <= 0:
        print("You're bankrupt.")
        end_game(money)
    else:
        still_play = input("PLAY again? Press y to continue, or any keys if you want to stop:  > ").lower()
        if still_play == "y":
            game_21(money, cards)
        else:
            end_game(money)

# ---- End game ----
def end_game(money):
    print(f"Game over, your money is ${money}.") 
    
# ---- The body of program ----
# ---- Combining all other functions ----
# ---- Indirect recursion to game_21() from if_continue() ----
def game_21(money, cards):
    ''' Core game program.'''
    put_bet = bet(money)
    print("Let's begin the game.")
    hand, hand_val, dealer_hand, dealer_val = dealing(cards)
    print(f"Your hand is {hand} with value {hand_val}.\nDealer's first card is {dealer_hand[0]} with value {cards[dealer_hand[0]]}.")
    
    while True:
        if hand_val < 21:
            draw_more = input("DRAW again? Press y to continue, or any keys if you want to stand:  > ").lower()
            if draw_more =="y":
                hand, hand_val = add_card(hand, cards)
                print(f"Your hand is {hand} with value {hand_val}.\nDealer's first card is {dealer_hand[0]} with value {cards[dealer_hand[0]]}.")
                continue
            else:
                # !--- PROBLEM: open_hand() return None ---!
                # !--- open_hand() is not worked. Function continues to if_continue()
                money = open_hand(hand, hand_val, dealer_hand, dealer_val, money, put_bet, cards) 
                if_continue(money, cards)
                break
        elif hand_val == 21:
            money += put_bet
            print("Blackjack!")
            print(f"Your money now is ${money}.")
            if_continue(money, cards)
            break
        else:
            money -= put_bet
            print(f"Your hand value is over than 21. You lose ${put_bet}. Your money now is ${money}.")
            if_continue(money, cards)
            break
            

# ---- PROGRAM STARTS HERE ----

game_21(initial, the_card)
    
# !--- Too much stack  ---!
# !--- After some stacks, program will return initial bet as money ---!