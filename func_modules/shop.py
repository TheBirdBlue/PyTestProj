import time
import common
import random
import town

import stats

def maxStatRecursion(level, money, moneyDown, stat):
    level = int(level)
    money = int(money)
    moneyDown = int(moneyDown)
    stat = int(stat)

    if money >= stat * 25 and level <= 999:

        # Increment Level, Attack, and queue Exp used
        moneyDown -= stat * 25
        level += 1
        stat += 1

        # Decrement old values before checking again
        money += moneyDown

        recursionReturn = maxStatRecursion(level, money, 0, stat)
        return recursionReturn

    else:
        return level, money, moneyDown, stat

def maxSpecial(level, money, stat):
    recursionReturn = []
    tempMun = int(money)
    tempStat = int(stat)
    levelUp = 0
    tempStatCost = int(tempStat * 1.5)
    if tempMun >= tempStatCost:

        recursionReturn = maxStatRecursion(levelUp, tempMun, 0, tempStat)
        recursionLevel = int(recursionReturn[0])
        recursionMun = int(recursionReturn[1])
        recursionSpend = int(recursionReturn[2])
        recursionStat = int(recursionReturn[3] - int(stat))

        recursionList = [recursionLevel, recursionMun, recursionSpend, recursionStat]
        recursionFormat = []

        for value in recursionList:
            recursionFormat.append(common.numConversion(value))

        print(' Stat will increase by ' + recursionFormat[3] + '.')
        print(' It will cost ' + common.numConversion(int(money) + (recursionMun * -1)) + '.')
        print(' Level will increase by ' + common.numConversion(recursionReturn[0]) + '.')
        confirm = input(' Would you like to make these changes? (Y or N)')

        if confirm.upper() == 'Y':

            # Stat Tracking
            stats.addMoneyTransaction(-(money + (recursionMun * -1)))
            return recursionLevel, recursionMun, recursionStat

        else:
            return 0, tempMun, 0

    else:
        amount = stat * 25 - money
        print(' You need ' + str(amount) + ' more Muns')
        time.sleep(1)
        return 0, money, 0

def specialShop(importList):

    # Set Level Up Values
    shop = True
    name = importList[0]
    level = int(importList[1])
    experience = int(importList[2])
    money = int(importList[3])
    attack = int(importList[4])
    defense = int(importList[5])
    special = int(importList[6])


    list = ['Raise Special', 'Max Special', 'Sell Resource', 'Dice', 'Coin', 'Return']
    resourceList = ['Wood', 'Ore', 'Metal']

    # Set price variables for selling resources
    woodVariable = random.randrange(-5, 6)
    oreVariable = random.randrange(-50, 51)
    metalVariable = random.randrange(-125, 126)

    # Set growth symbols
    infoVariable = [woodVariable, oreVariable, metalVariable]
    infoPrice = [10, 100, 250]
    symbol = []

    # Set symbols for lists for selling resources
    for base, variable in zip(infoPrice, infoVariable):
        if variable == 0:
            symbol.append('-')

        elif variable > 0:
            percent = int((variable / base) * 100)
            if percent == 50:
                symbol.append('↑↑↑')
            elif percent in range(25, 50):
                symbol.append('↑↑')
            elif percent in range(1, 25):
                symbol.append('↑')

        elif variable < 0:
            newVariable = -variable
            percent = int((newVariable/base) * 100)
            if percent == 50:
                symbol.append('↓↓↓')
            elif percent in range(25, 50):
                symbol.append('↓↓')
            elif percent in range (1, 25):
                symbol.append('↓')

    while shop:
        common.clear()

        shopOverview = [name, level, experience, money, attack, defense, special]
        shopFormat = []
        point = 1

        # Run values through formatting function
        for value in shopOverview:
            shopFormat.append(common.numConversion(value))
            point += 1

        levelFormat = shopFormat[1]
        moneyFormat = shopFormat[3]
        specialFormat = shopFormat[6]

        # GUI for Over Stats
        number = 1
        print(' Welcome to the "Special" shop,  ' + name)
        print(' ╔════════════════════╡')
        infoLine = ' ╟Lvl:{:>15} ╡\n ╟Mun:{:>15} ╡'
        print(infoLine.format(levelFormat, moneyFormat))

        # GUI for Player Stats
        print(' ╠════════════════════╡')
        statHeader = ' ╠                SPE ╡'
        print(statHeader)
        statLine = ' ╠{:>19} ╡'
        print(statLine.format(specialFormat))

        # GUI for Choices and Actions
        print(' ╠═══╦════════════════╡')
        for choice in list:
            choiceLine = ' ╟(' + str(number) + ")╟ " + '{:<15}' + "|"
            print(choiceLine.format(choice))

            # Sub-menu for sell resources
            if number == 3:
                subchoice = 1
                for resource, arrow in zip(resourceList, symbol):
                    choiceLine = ' ╟   ╟ -' + str(subchoice) + ' {:<6} {:<5}' + "|"
                    print(choiceLine.format(resource, arrow))
                    subchoice += 1
            number += 1
        print(' ╚═══╩════════════════╧')

        shopChoice = input(' Choose Selection: ')
        time.sleep(0.2)

        if shopChoice == '1':
            if money >= special * 25:
                money -= special * 25

                # Stat Tracking
                stats.addMoneyTransaction(-(special * 25))

                level += 1
                special += 1

            else:
                amount = (special * 25) - money
                print(' You need ' + common.numConversion(amount) + ' more Muns.')
                time.sleep(1)

        elif shopChoice == '2':
            changeStats = maxSpecial(level, money, special)
            level += changeStats[0]
            money = changeStats[1]
            special += changeStats[2]

        elif shopChoice.startswith('3'):
            if '-' in shopChoice:
                check = shopChoice.split('-')
                try:
                    newCheck = int(check[1])
                    if newCheck in range(1,4):
                        town.sellResources(newCheck - 1, woodVariable, oreVariable, metalVariable)

                except:
                    print('Invalid input.')
                    time.sleep(1)

            else:
                print(' Missing resource option. Please include "-#" after the 3.')
                time.sleep(2)

        elif shopChoice == '4':

            # Gamble Option against a six-sided die
            bet = input(" What's your wager? ")

            # Try to run bet input as integer
            try:
                int(bet)
                bet = int(bet)

                # Check that player has the money to bet
                if bet <= money:
                    guess = input(" What's your guess (1-6)? ")
                    roll = random.randrange(1, 7)
                    roll = int(roll)
                    print(' The dice rolls... on a ' + str(roll))
                    time.sleep(1)

                    # Checks if guess is correct

                    if guess == '':
                        print(' No number selected.')
                        time.sleep(1)

                    elif int(guess) == int(roll):
                        print(" Well done, winner. Here's your " + str(bet * 5) +" Mun.")
                        money += int(bet) * 5
                        time.sleep(1)

                        # Stat Tracking
                        stats.addMoneyTransaction(bet * 5)

                    else:
                        print(" Better luck next roll.")
                        money -= bet
                        time.sleep(1)

                        # Stat Tracking
                        stats.addMoneyTransaction(- bet)

                else:
                    print(" You don't have that much to spare...")
                    time.sleep(1)

            except:
                bet = 0
                print(' Invalid Amount')

        elif shopChoice == '5':

            # Gamble Option against a coin flip
            print(' Heads you win. Tails you lose.')
            bet = input(" What's your wager? ")

            # Try to run bet input as integer
            try:
                int(bet)
                bet = int(bet)

                # Check that player has the money to bet
                if bet <= money:
                    coin = random.randrange(1, 3)


                    if int(coin) == 1:
                        print(" The coin is flipped... and it's heads.")
                        time.sleep(1)
                        print(" Well done, winner. Here's your " + str(bet) + " Mun.")
                        money += int(bet)
                        time.sleep(1)

                        # Stat Tracking
                        stats.addMoneyTransaction(bet)

                    else:
                        print(" The coin is flipped... and it's tails.")
                        time.sleep(1)
                        print(" Better luck next flip.")
                        money -= bet
                        time.sleep(1)

                        # Stat Tracking
                        stats.addMoneyTransaction(- bet)

                else:
                    print(" You don't have that much to spare...")
                    time.sleep(1)

            except:
                bet = 0
                print(' Invalid Amount')

        elif shopChoice == '6':
            shop = False
            return shopOverview

        else:
            common.clear()
            print(' Invalid Choice.')
