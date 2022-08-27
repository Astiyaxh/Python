import random


def dealerTurn(start, playerTotal):
    total = start

    # Dealer will continue to hit until their total is > 21 OR they have beat the player
    while total <= playerTotal and total <= 21:
        card = getCard()
        total = total + card
        print("Dealer gets a " + str(card) + ". He now shows " + str(total))

    return total


def getBet(max):
    bet = int(input())

    # Ensure the player doesn't bet more than they have.
    while bet <= 0 or bet > max:
        print("Enter an amount between $1 and $" + str(max))
        bet = int(input())

    return bet


def getCard():
    deal = int(random.random() * 13) + 1
    if deal > 10:

        # If the card is above 10 (Jack, Queen, King), the function returns 10.
        value = 10
    else:
        value = deal

    return value


def introduction():
    print("Welcome to Flowgorithm Blackjack")
    print("The rules are quite simple - given this is simple demonstration program. Aces are always worth one. The dealer must hit until they have a higher hand (or they bust).")


def playerTurn(start):
    total = start

    # Loop until the player selects "s" to stand or they bust.
    while True:  # This simulates a Do Loop
        print("Hit or stand?  (h/s)")
        choice = input()
        if choice == "h":
            card = getCard()
            print("You are dealed a " + str(card))
            total = total + card
        print("You show: " + str(total))
        if not(total <= 21 and choice != "s"):
            break  # Exit loop

    return total


def playerWon(playerTotal, dealerTotal):
    # This logic can be simplied to a single Boolean expression. However, let's keep it readable.
    if playerTotal > dealerTotal:
        if playerTotal <= 21:
            won = True
        else:
            won = False
    else:
        if dealerTotal <= 21:
            won = False
        else:
            won = True

    return won


# Main
cash = 100
introduction()
while cash > 0:
    print("You now have $" + str(cash) + ". Enter your bet.")
    bet = getBet(cash)
    playerCards = getCard() + getCard()
    dealerCards = getCard()
    print("Dealer gives you two cards...")
    print("You show: " + str(playerCards))
    print("Dealer shows: " + str(dealerCards))
    playerCards = playerTurn(playerCards)
    if playerCards <= 21:
        dealerCards = dealerTurn(dealerCards, playerCards)
    if playerWon(playerCards, dealerCards):
        print("YOU WIN!")
        cash = cash + bet
    else:
        print("YOU LOSE!")
        cash = cash - bet
print("Game over!")
