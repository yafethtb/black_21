from the_cassino import Player, Dealer

player = Player()
dealer = Dealer()

player.account()

table_on = True
while table_on:

    if player.account > 0:
        ask = input("Do you want to bet now? Press 'y' to bet, press other keys to stop: >  ").lower()
    else:
        print("You don't have enough money. Game over!")
        table_on = False
        break

    if ask == 'y' or ask == 'yes':
        while True:
            bid = int(input("How much your bid? >  $ "))
            if bid > player.account:
                print("Please enter lower value.")
            elif bid <= player.account:
                print("Let's continue.")
                break
        
        player_value = player.play(player.dealing,player.add, bid)
        
        if player_value == 21:
            print(f"You win $ {bid}. Your account is $ {player.account}")
        elif player_value > 21:
            print(f"You lose. Your account is $ {player.account}.")
        elif player_value < 21:
            dealer_value = dealer.dealer_play(dealer.dealing, dealer.add)            
            if player_value == dealer_value:
                print("It's draw.")
            elif player_value < dealer_value and dealer_value <= 21:
                print("You lose.")
                player.account -= bid
            else:
                print("You win!")
                player.account += bid
        
    else:
        print(f"Your account is $ {player.account}.")
        table_on = False


