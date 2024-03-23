# to-do list:
# enable deposit and bet amounts
# allow lower case "H" or "S" inputs as well   

import random

cards = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
}

player_cards = []
dealer_cards = []


# deal cards
def deal_cards():
    # draw 2 new cards 
    dealer_card_1 = random.choice(list(cards.keys()))
    dealer_card_2 = random.choice(list(cards.keys()))
    # append those 2 new cards to the empty list "dealer_cards"
    dealer_cards.extend([dealer_card_1, dealer_card_2])
    
    # print the dealer's 1st card while hiding the 2nd card
    print(f"Dealer has drawn a {dealer_card_1} and a hidden card")
    # checks if dealer hit blackjack. If so, exit the program
    dealer_score = cards[dealer_card_1] + cards[dealer_card_2]
    if dealer_score == 21: 
        print("Dealer has Blackjack! Dealer wins!")
        exit()

    player_card_1 = random.choice(list(cards.keys()))
    player_card_2 = random.choice(list(cards.keys()))
    player_cards.extend([player_card_1, player_card_2])
    
    player_score = cards[player_card_1] + cards[player_card_2]
    print(f"You drew a {player_card_1} and a {player_card_2}. You have a score of {player_score}")
    if player_score == 21:
        print("You have Blackjack! Congratulations. You win!")
        exit()

    return player_score, dealer_score, player_cards, dealer_cards

# draw 1 new card, regardless for player or for dealer
def draw_card(): 
    new_card = random.choice(list(cards.keys()))
    new_score = cards[new_card]
    print(f"New card drawn is a {new_card}")
    return new_score, new_card

# Action for the player 
def player_action(player_score):
    # Keep asking the player whether to Hit or Stay, until they bust or they choose to stay
    while True:
        choice = input("It's your turn. Hit or stay? Enter 'H' for hit, 'S' for stay ")
        if choice == "H":
            new_score, new_card = draw_card()
            player_score += new_score
            print(f"You now have a score of {player_score}")

            if player_score > 21:
                break
        
        elif choice == "S":
            print(f"You chose to stay with your current score of {player_score}. Now it's the dealer's turn")
            break
        
        else:
            print("Error. That's not a valid input")
        
    return player_score

# Action for the dealer
def dealer_action(dealer_score):
        # dealer now reveals his cards
        print(f"Dealer flips his cards. You now see that he has a {' and '.join(dealer_cards)} for a score of {dealer_score}")
        # keep drawing new cards until dealer busts, or is over 16
        while dealer_score <= 16:
            new_score, new_card = draw_card()
            dealer_cards.append(new_card_)
            dealer_score += new_score
            print(f"Dealer drew a {new_card}. Dealer now has a total score of {dealer_score}")
            
            if dealer_score > 21: 
                break

        return dealer_score


def main():
    print("Welcome to Michael's casino!")

    player_score, dealer_score, player_cards, dealer_cards = deal_cards()   

    player_score_final = player_action(player_score)
    dealer_score_final = dealer_action(dealer_score)
    if player_score_final > 21: 
        print("You busted and lost. Thanks for playing!")
    elif dealer_score_final > 21: 
        print("Dealer busted. You win!")
    else: 
        if player_score_final > dealer_score_final:
            print("Your cards are higher than the dealer's. You win! Thanks for playing!")
        elif player_score_final == dealer_score_final:
            print("A rare tie! Neither player wins. Thanks for playing!")
        else:
            print("Your cards are lower than the dealer's. You lose. Thanks for playing!")
    
main()