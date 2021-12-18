# THE SIMPLE BLACKJACK PROJECT
## How it works

The blackjack rules are simple:

    1.  Whoever get the total value more than 21 is automatically lose and lose the bet.
    2. Whoever get the total value closed to 21 OR exactly 21 is the winner and get all the bet.

---
Blackjack algorithm then can be explained as these steps:

* State your account (how much money you brings to the table) and put your bet.
* Dealer gives you a pair of face-up cards. Total value of both cards should not exceed 21 or you'll automatically lose.
* Dealer draws two cards for themselves but only open one of them.
* You choose whether you want to draw another card or stand on what you have already.
* If you draw a card, as long as it's not exceed 21, you can either draw one more card or choose to stand with whatever you get already.
* If you choose to stand, the dealer will flip their face-down card. Then the value of your cards and theirs will be compared. 
* If you win, your account will be added with the amount of your bet. If you lose, your account will be subtracted with the amount of your bet.
* Keep playing until your account become zero or stop whenever you like.

--- 
An extra rule:
If dealer's initial cards have value under than 17, dealer draw a card until the value higher than your value OR it exceeded 21.

---
It's a simple set of rules and algorithm, but how to implement it will be quite challenging for my recent knowledge level of programming. 

### New added:
New version in folder (jack_with_class) consist of three files: card_stack.py(model), the_casino.py (controller), the_table.py(view). I refactoring my previous code to make it easier to understand.
    
