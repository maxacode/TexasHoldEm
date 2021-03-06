# Texas HOld Em game
#
import random

#Players  bank.
bank = 1000
#Rounds in the game
rounds = (1,2,3,4,5)
#Players who have not folded.
playersStillIn = []
#bots bank account:
allPlayersAccountValue = {}



all_cards = [('Club', '1'), ('Club', '2'), ('Club', '3'), ('Club', '4'), ('Club', '6'), ('Club', '7'), ('Club', '8'), ('Club', '9'), ('Club', '10'), ('Club', 'J'), ('Club', 'Q'), ('Club', 'K'), ('Club', 'A'), ('Spade', '1'), ('Spade', '2'), ('Spade', '3'), ('Spade', '4'), ('Spade', '6'), ('Spade', '7'), ('Spade', '8'), ('Spade', '9'), ('Spade', '10'), ('Spade', 'J'), ('Spade', 'Q'), ('Spade', 'K'), ('Spade', 'A'), ('Heart', '1'), ('Heart', '2'), ('Heart', '3'), ('Heart', '4'), ('Heart', '6'), ('Heart', '7'), ('Heart', '8'), ('Heart', '9'), ('Heart', '10'), ('Heart', 'J'), ('Heart', 'Q'), ('Heart', 'K'), ('Heart', 'A'), ('Diamond', '1'), ('Diamond', '2'), ('Diamond', '3'), ('Diamond', '4'), ('Diamond', '6'), ('Diamond', '7'), ('Diamond', '8'), ('Diamond', '9'), ('Diamond', '10'), ('Diamond', 'J'), ('Diamond', 'Q'), ('Diamond', 'K'), ('Diamond', 'A')]

def intro():
    global bank
    #bank = int(input("Welcome to Texas Hold Em Game - Offline Edition! \n Enter $ for all players to start with (Default $10,000): "))
    #players = int(input("Enter how many bots you would like to play against: "))
    players = 3

    #Adding all players to the ones still playing.
    for x in range(0,players+1):
        playersStillIn.append(x)
        allPlayersAccountValue[x] = bank
    #print(allPlayersAccountValue)
    #print(playersStillIn)
    giveCards(players)

# Vars:
# 1. All the types of cards - deck of cards,


# 2. How much money a player has and starts with.
# 3. Blinds
#
#
# Functions:
# 1. Give out cards to everyone.
def giveCards(players):
    global playerDecks
    playerDecks = {}
    for playerNum in range(0,players+1):

        first_card = random.randint(0,51)
        sec_card = random.randint(0,51)
        playerDecks[playerNum] = (all_cards[first_card]) + (all_cards[sec_card])

    print(f"These are your cards: \n {playerDecks[0]}")
    playerWage(playerDecks,players)

# 2. Have players make their choices - Bots have a strategy they follow.
def playerWage(playerDecks, players):
    pot = 0
    global allPlayersWages
    #This rounds wages and what player did it:
    allPlayersWages = {}
    #mainPlayerWage = int(input("Enter your wage: "))
    mainPlayerWage = 100
    allPlayersAccountValue[0] -= mainPlayerWage

    pot += mainPlayerWage
    print(f"Player 0 (You) is betting this much: {mainPlayerWage}")
    for playersWage in range(1,players + 1):
        botWage = random.randint(0,bank/10)
        print(f"Player {playersWage} is betting this much: {botWage}")
        allPlayersWages[playersWage] = botWage
        allPlayersAccountValue[playersWage] -= botWage

        #print(allPlayersWages)
        pot += botWage
    #print(allPlayersAccountValue)
    print(f"\nThe current pot is: {pot}\n")
    checkPotEqual()

def checkPotEqual():
    print(f" all player wages = {allPlayersWages}")
    for x in range(0,len(playersStillIn)):
        highestBet = max(allPlayersWages, key=allPlayersWages.get)
        if allPlayerWages[x]

# Ask mainPlayer what htey want to do: Call, Raise, Fold, etc.
def mainPlayerActions():
   # mainPlayerAction = input("Enter what action you would like to perform: 1:Fold, 2:Call, 3:Raise, 4:Stay:  " )
    mainPlayerAction = "4"


    if mainPlayerAction == "1":
        print("You are folding out! ")
       # playersStillIn.remove([0])
        exit()

    elif mainPlayerAction == "2":
        highestBet = max(allPlayersWages, key=allPlayersWages.get)
        print(f"You are calling this amount {allPlayersWages[highestBet]} from Player {highestBet}")
        allPlayersWages[0] = allPlayersWages[highestBet]
        callForBots(allPlayersWages, 0)

    elif mainPlayerAction == "3":
        raiseAction(0)
    elif mainPlayerAction == "4":
        print("Staying" )
        botActions()

    else:
        print("Some error in mainPlayerActions FUnc")


#Actions for bot:
def callForBots(player):
    highestBet = max(allPlayersWages, key=allPlayersWages.get)

    print(f"Player{player} has called this much {highestBet}")
    for x in range(1, len(playersStillIn)):
        print(f"Player{player} has called this much {highestBet}")
        allPlayersWages[x] = allPlayersWages[highestBet]
        print(allPlayersWages)

def botActions():
    print(len(playersStillIn))
    print(playerDecks)

    # If bot has a pair of cards or suits
    for x in range(1, len(playersStillIn)):
        if playerDecks[x][1] == playerDecks[x][3] or playerDecks[x][0] == playerDecks[x][2]:
            print(f"Player{x} has Pair of Cards or Suits")
            raiseAction(x)
    else:
        round2()

def raiseAction(player):
    if player == 0:
        raiseAmount = int(input("What would you like to raise by: "))
        allPlayersWages[player] = raiseAmount
        callForBots(player)

    else:
        print(allPlayersWages)
        raiseAmount = allPlayersWages[player] * 1.1
        allPlayersWages[player] = raiseAmount
        print(allPlayersWages)
        callForBots(player)

# 3. Deal cards then send to func 2tf
#
def round2():
    print("Starting Round 2")
# 4. compare all hands to determine winner.
#
# 5. Give out rewards to winner/winners.
#
# 6. Skip bots if main player folds.


intro()