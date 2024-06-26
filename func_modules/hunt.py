import time
import common
import random
import stats
import itertools
import town
import sys

sys.setrecursionlimit(999)

def huntRewards(rank, experience, money):
    rewardExp = rank + random.randrange(0,rank + 1)
    rewardMun = random.randrange(int(rank / 4), (rank * 2) + 1)
    rewardExp = int(rewardExp)
    rewardMun = int(rewardMun)
    return rank, rewardExp, rewardMun

def percentCalc(rank, attack, defense, special):

    # Calculate powers
    playerBase = ((attack * 1.5) + defense) + int((special * 2))
    playerBase = int(playerBase)
    m = 1 / 5
    x = rank
    huntPower = m * (x ** 2) + 5

    # Create float for percentage
    winBase = playerBase / huntPower
    winChance = winBase * 100
    winChance = int(winChance)

    if winBase > 1:
        winChance = 99

    return winChance, winBase * 100

def silentHunt(rank, percent, attack, defense, special, experience, money, wins):
    winlose = 0

    # Set Pre-hunt Values
    preExp = experience
    preMun = money

    # Check the battle
    closer = random.randrange(1, 101)
    if closer <= percent:
        huntReturn = huntRewards(rank, 0, 0)
        experience += preExp + int(huntReturn[1] / 2)
        money += preMun + int(huntReturn[2] / 2)
        winlose += 1

    else:

        # Stat Tracking
        winlose -= 1
    return rank, percent, attack, defense, special, experience, money, winlose

def huntAction(rank, attack, defense, special, experience, money):

    # Set Pre-hunt Values
    preExp = experience
    preMun = money

    # Calculate win percent
    winChance = percentCalc(rank, attack, defense, special)

    # Check the battle
    closer = random.randrange(1,101)
    if closer <= winChance[0]:
        huntReturn = huntRewards(rank, 0, 0)
        postExp = preExp + int(huntReturn[1] / 2)
        postMun = preMun + int(huntReturn[2] / 2)

        # Stat Tracking
        stats.addHuntWinnings(postMun, postExp, 1)

        if winChance == 99:
            print('\n That was too easy!')

        print(' You gained [' + str(postExp) + '] exp and [' + str(postMun) + '] monies.')
        time.sleep(1)
        town.resourceCollection(1)

        return rank, attack, defense, special, postExp, postMun

    else:
        print("\n It's a tough fought battle!")
        time.sleep(1)
        print(' ...but you lost.')
        time.sleep(1)

        # Stat Tracking
        stats.addLose(1)

        return rank, attack, defense, special, 0, 0

def superHunt(rank, attack, defense, special, experience, money):

    # Ask for player info
    rankSuper = input('\n What rank do you want to hunt at? (Current Rank: ' + str(rank) + ')')
    huntSuper = input(' How many hunts do you want to do? (Max 10,000) ')
    test = True

    #try:
    if rankSuper == '':
        rankSuper = rank

    if huntSuper == '':
        huntSuper = 10000

    if int(rankSuper) > 0 and int(huntSuper) > 0:
        rankSuper = int(rankSuper)
        huntSuper = int(huntSuper)

    if huntSuper <= 10000:
        print(' Once started, these hunts will not stop.')
        confirm = input(' Continue at rank ' + str(rankSuper) + ' for ' + str(huntSuper) + ' hunts? (Y or N) ')

        # Begin Super Hunt
        if confirm.upper() == 'Y':
            huntNumber = 1
            totalMun = 0
            totalExp = 0
            totalWins = 0
            totalLosses = 0

            # Set Pre-hunt Values
            preExp = experience
            preMun = money

            # Calculate win percent
            winChance = percentCalc(rank, attack, defense, special)

            while int(huntNumber) < int(huntSuper) + 1:
                common.clear()
                barNum = int((int(huntNumber) / int(huntSuper)) * 50)
                print(' Super Hunting the deadliest of game... Hunt # ' + str(huntNumber))
                progress = (' 0% [{:<50}] 100%')
                print(progress.format('▓'*barNum))
                time.sleep(0.1)

                runBattle = silentHunt(rank, winChance[0], attack, defense, special, experience, money, totalWins)
                totalMun += runBattle[6]
                totalExp += runBattle[5]

                if runBattle[6] > 0:
                    totalWins += 1

                else:
                    totalLosses += 1

                huntNumber += 1

            # Stat Tracking
            stats.addHuntWinnings(totalMun, totalExp, totalWins)
            stats.addLose(totalLosses)

            # Format numbers
            numbersList = [totalWins, totalLosses, totalMun, totalExp]
            formattedNumbers = []
            for value in numbersList:
                formattedNumbers.append(common.numConversion(value))

            totalWinsFormat = formattedNumbers[0]
            totalLossesFormat = formattedNumbers[1]
            totalMunFormat = formattedNumbers[2]
            totalExpFormat = formattedNumbers[3]

            print(' The results are in!')
            time.sleep(1)
            resultLine = (' There were: {} wins! {} losses! {} Muns earned! {} Exp gained!')
            print(resultLine.format(totalWinsFormat, totalLossesFormat, totalMunFormat, totalExpFormat))

            print('\n Town is collecting resources. Please wait...')
            town.resourceCollection(totalWins)
            input('\n Press [ENTER] to continue...')
            return rank, attack, defense, special, totalExp, totalMun

        else:
            print(' Super Hunt Cancelled. Confirmation not received.')
            time.sleep(1)
            return rank, attack, defense, special, experience, money

    else:
        print(' Limit of 10,000 times. Please try again.')
        time.sleep(2)
        return rank, attack, defense, special, experience, money

    #except:
    #    print(' Invalid Input')
    #    time.sleep(1)
    #    return rank, attack, defense, special, experience, money


def runningHunt(attack, defense, special, experience, money, rank):
    common.clear()

    totalMun = 0
    totalExp = 0
    totalWins = 0

    rank = 1

    def runningRecursion(rank, percent, attack, defense, special, experience, money, wins):

        percent = percentCalc(rank, attack, defense, special)

        print(' Running rank ' + str(rank))
        time.sleep(0.1)
        runBattle = silentHunt(rank, percent[1], attack, defense, special, experience, money, wins)

        return runBattle

    print(' Welcome to Running Hunt!')
    print(' You will run though every rank from 1 to when you lose.')
    print(' This could take seconds. This could take minutes.\n')
    confirm = input(' Do you want to continue? (Y or N) ')
    if confirm.upper() == 'Y':
        percent = percentCalc(rank, attack, defense, special)

        for i in itertools.count(start=1):
            common.clear()

            runningList = runningRecursion(rank, percent[1], attack, defense, special, 0, 0, 0)
            if runningList[7] > 0:
                rank += 1
                totalExp += runningList[5]
                totalMun += runningList[6]
                totalWins += 1

            else:
                time.sleep(1)
                common.clear()
                break

    else:
        print(' Confirmation not received.')
        time.sleep(2)
        return attack, defense, special, experience, money, rank

    # Stat Tracking
    stats.addHuntWinnings(totalMun, totalExp, totalWins)
    stats.addLose(1)

    # Format numbers
    numbersList = [totalWins, 1, totalMun, totalExp]
    formattedNumbers = []
    for value in numbersList:
        formattedNumbers.append(common.numConversion(value))

    totalWinsFormat = common.numConversion(i - 1)
    totalExpFormat = common.numConversion(totalExp)
    totalMunFormat = common.numConversion((totalMun))

    print(' The run is over!')
    time.sleep(1)
    resultLine = (' There were: {} wins! {} Muns earned! {} Exp gained!')
    print(resultLine.format(totalWinsFormat, totalMunFormat, totalExpFormat))

    print('\n Town is collecting resources. Please wait...')
    town.resourceCollection(i -1)
    input('\n Press [ENTER] to continue...')


    return totalExp, totalMun


def huntFunction(importList):

    # Set hunt variables
    hunt = True
    name = importList[0]
    huntLvl = int(importList[1])
    huntExp = int(importList[2])
    huntMun = int(importList[3])
    huntAtk = int(importList[4])
    huntDef = int(importList[5])
    huntSpe = int(importList[6])

    # Set recommended rank
    rank = 1

    for i in itertools.count(start=1):

        # Calculate win percent
        winChance = percentCalc(rank, huntAtk, huntDef, huntSpe)

        if winChance[0] < 86:
            break

        rank += 1

    # Begin Hunt Menu and Functions
    while hunt:

        # Calculate win percent
        winChance = percentCalc(rank, huntAtk, huntDef, huntSpe)

        huntOverview = [name, huntLvl, huntExp, huntMun, huntAtk, huntDef, huntSpe]
        huntFormat = []
        point = 1

        # Run values through formatting function
        for value in huntOverview:
            huntFormat.append(common.numConversion(value))
            point += 1

        huntLvlFormat = huntFormat[1]
        huntExpFormat = huntFormat[2]
        huntMunFormat = huntFormat[3]
        huntAtkFormat = huntFormat[4]
        huntDefFormat = huntFormat[5]
        huntSpeFormat = huntFormat[6]

        common.clear()
        print(' Be safe on your hunt.')

        # Hunt list of options
        huntOptions = ['Hunt at R ' + str(rank) + '  ' + str(winChance[0]) + '%', 'Change Rank', 'Super Hunt',
                       'Running Hunt', 'Return']

        # GUI for Hunt Stats
        print(' ╔══════════════════════════╡')
        infoLine = ' ╟Lvl:{:>21} ╡\n ╟Exp:{:>21} ╡\n ╟Mun:{:>21} ╡'
        print(infoLine.format(huntLvlFormat, huntExpFormat, huntMunFormat))

        # GUI for Player Stats
        print(' ╠══════════════════════════╡')
        print(' ╠    ATK ╬    DEF ╬    SPE ╡')
        statLine = ' ╠{:>7} ╬{:>7} ╬{:>7} ╡'
        print(statLine.format(huntAtkFormat, huntDefFormat, huntSpeFormat))
        print(' ╠══════════════════════════╡')
        print(' ╠ Player Power:            ╡')
        powerLine = ' ╠{:>25} ╡'
        value = (((huntAtk * 5) + int(huntDef * 3) + (huntSpe * 10)) * 8) + huntLvl
        value = common.numConversion(value)
        print(powerLine.format(value))


        # GUI for Choices and Actions
        number = 1
        print(' ╠═══╦══════════════════════╡')
        for choice in huntOptions:
            choiceLine = ' ╟(' + str(number) + ")╟ " + '{:<21}' + "|"
            print(choiceLine.format(choice))
            number += 1
        print(' ╚═══╩══════════════════════╧')

        waitforhunt = input(' Choose Selection or [ENTER] for Hunt: ')
        time.sleep(0.2)

        if waitforhunt == '1' or waitforhunt == '':
            huntReaction = huntAction(rank, huntAtk, huntDef, huntSpe, 0, 0)
            huntExp += huntReaction[4]
            huntMun += huntReaction[5]

        elif waitforhunt == '2':
            newRank = input(' Set Rank: ')
            try:
                int(newRank)
                if int(newRank) > 0:
                    rank = int(newRank)
            except:
                newRank = rank
                print(' Invalid Choice')

            print(' Rank is now ' + str(rank))
            time.sleep(1)

        elif waitforhunt == '3':
            if huntLvl >= 200:
                huntReaction = superHunt(rank, huntAtk, huntDef, huntSpe, 0, 0)
                huntExp += huntReaction[4]
                huntMun += huntReaction[5]
            else:
                print(' Must be Level 200 to use Super Hunt!')
                time.sleep(1)

        elif waitforhunt == '4':
                huntReaction = runningHunt(huntAtk, huntDef, huntSpe, 0, 0, 1)
                huntExp += huntReaction[0]
                huntMun += huntReaction[1]

        elif waitforhunt == '5':
            hunt = False
            return huntOverview

        else:
            common.clear()
            print('Invalid Choice.')
