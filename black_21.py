import random

# --- OPENING ---
print('''
    ========

    WELCOME TO PYTHON CASINO!
    THIS IS BLACKJACK TABLE.
    LET'S TRY YOUR LUCK!

    ========
''')

# --- Declare card deck ---
deck = {
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

# --- Declare Money ---
account = int(input("Please input your chip total values: > $ "))

# --- Draw hand ---

def deal_card(stack, qty):
    ''' Return 2 card first, then 1 more card when player asked. '''
    return [random.choice(list(stack.keys())) for i in range(0, qty)]

# --- Sum card value ---
def value_card(stack, hand):
    ''' Count value of all cards in hand '''
    val = sum([stack[i] for i in stack if i in hand])
    return val

# --- GAME OVER ---
def end_game(money):
    ''' Show message with amount of money when the game is over. '''
    print(f"Game over. Your money is $ {money}.")

# --- MAIN PROGRAM ---
def blackjack(stack, chip):
    ''' Main program. It checks bets and doing card dealing. '''
    # --- Betting ---
    while True:
        bet = int(input("Put how much chip you want to bet:  > $ "))
        if bet > chip:
            print("You can't bet chips you don't have. Please repeat.")            
        else:
            print("You can continue.")
            break
    
    # --- Dealing card ---
    print("Dealing card.")
    player_hand = deal_card(stack, 2)
    dealer_hand = deal_card(stack, 2)
    player_value = value_card(stack, player_hand)
    dealer_value = value_card(stack, dealer_hand)

    # --- Showing card ---
    print(f"Player's hand: {player_hand}; value: {player_value}")
    print(f"Dealer's first card: {dealer_hand[0]}; value: {stack[dealer_hand[0]]}")

    # --- Comparing hands ---
    while True:
        if player_value == 21:
            print("Blackjack! Player wins!")
            chip += bet
            break
        elif player_value > 21:
            print("Your hand is higher than 21. You lose.")
            chip -= bet
            break
        elif player_value < 21:
            add_card = input("Do you want to ADD card? Press y to continue, press any other keys to open card:  > ").lower()
            if add_card == "y":
                print("Adding a card.")              
                player_hand += deal_card(stack, 1)
                player_value = value_card(stack, player_hand)
                
                print(f"Player's hand: {player_hand}; value: {player_value}.")
                continue
            else:
                # --- Opening cards ---
                print("Open hand.")
                while True:    
                    if dealer_value < 17:
                        print("Dealer's hand is under 17. Dealer will add one more card.")
                        one_dealer = deal_card(stack, 1)
                        dealer_hand += one_dealer
                        dealer_value = value_card(stack, dealer_hand)
                        print(f"Dealer's hand: {dealer_hand}; value: {dealer_value}.")
                        continue
                    elif dealer_value == 21:
                        print("Dealer blackjack! Player lose.")
                        chip -= bet
                    elif dealer_value > 21:
                        print("Dealer's hand is higher than 21. Player wins.")
                        chip += bet
                    else:
                        if player_value == dealer_value:
                            print(f"Player value: {player_value}.\nDealer value: {dealer_value}.\nIt's a draw.")
                            break
                        elif player_value > dealer_value:
                            print(f"Player value: {player_value}.\nDealer value: {dealer_value}.\nYou win!")
                            chip += bet
                            break
                        elif player_value < dealer_value:
                            print(f"Player value: {player_value}.\nDealer value: {dealer_value}.\nYou lose.")
                            chip -= bet
                            break
            break                
    
    # --- Checking money. It will pass if money is zero ---
    if chip <= 0:
        print("You can't play anymore.")
        end_game(chip)
        
    else:
        print(f"You have $ {chip} to spend.")
        start_again = input("Do you want to CONTINUE the game? Press y to continue, press any other keys to stop:  > ").lower()
        if start_again == "y":
            blackjack(stack, chip)
        else:
            end_game(chip)
            


# --- GAME STARTS HERE ---
blackjack(deck, account)
