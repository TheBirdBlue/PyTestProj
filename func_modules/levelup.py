import common
import time
import stats
import sys

sys.setrecursionlimit(1100)

def maxStatRecursion(level, experience, experienceDown, stat):
    if experience >= int(stat * 1.5) and level <= 999:

        # Increment Level, Attack, and queue Exp used
        experienceDown -= int(stat * 1.5)
        level += 1
        stat += 1

        # Decrement old values before checking again
        experience += int(experienceDown)
        recursionReturn = maxStatRecursion(level, experience, 0, stat)
        return recursionReturn

    else:
        return level, experience, experienceDown, stat

def maxStat(level, experience, stat):
    recursionReturn = []
    tempExp = int(experience)
    tempStat = int(stat)
    levelUp = 0
    tempStatCost = int(tempStat * 1.5)
    if tempExp >= tempStatCost:

        recursionReturn = maxStatRecursion(levelUp, tempExp, 0, tempStat)

        print(' Stat will increase by ' + common.numConversion(recursionReturn[3] - stat) + '.')
        print(' It will cost ' + common.numConversion(experience + (recursionReturn[1] * -1)) + '.')
        print(' Level will increase by ' + common.numConversion(recursionReturn[0]) + '.')
        confirm = input(' Would you like to make these changes? (Y or N)')

        if confirm.upper() == 'Y':

            # Stat Tracking
            stats.addExpOut((experience + (recursionReturn[1] * -1)))
            return recursionReturn[0], recursionReturn[1], recursionReturn[3] - stat

        else:
            return 0, tempExp, 0

    else:
        amount = int(stat * 1.5 - experience)
        print('You need ' + str(amount) + ' more EXP')
        time.sleep(1)
        return 0, tempExp, 0

def levelup(importList):

    # Set Level Up Values
    levelup = True
    name = importList[0]
    level = int(importList[1])
    experience = int(importList[2])
    money = int(importList[3])
    attack = int(importList[4])
    defense = int(importList[5])
    special = int(importList[6])
    list = ['Raise Attack', 'Raise Defense', 'Max Attack', 'Max Defense', 'Return']

    # Begin main menu and functions
    while levelup:
        common.clear()

        levelOverview = [name, level, experience, money, attack, defense, special]
        levelFormat = []

        # Run values through formatting function
        for value in levelOverview:
            levelFormat.append(common.numConversion(value))

        charLevelFormat = levelFormat[1]
        experienceFormat = levelFormat[2]
        attackFormat = levelFormat[4]
        defenseFormat = levelFormat[5]

        # GUI for Over Stats
        number = 1
        print(' Getting more powerful ' + name)
        print(' ╔════════════════════╡')
        infoLine = ' ╟Lvl:{:>15} ╡\n ╟Exp:{:>15} ╡'
        print(infoLine.format(charLevelFormat, experienceFormat))

        # GUI for Player Stats
        print(' ╠════════════════════╡')
        statHeader = ' ╠      ATK ╬     DEF ╡'
        print(statHeader)
        statLine = ' ╠{:>9} ╬{:>8} ╡'
        print(statLine.format(attackFormat, defenseFormat))

        # GUI for Choices and Actions
        print(' ╠═══╦════════════════╡╞══════════════════════╡')
        for choice in list:
            choiceLine = ' ╟(' + str(number) + ")╟ " + '{:<15}' + "|"
            costLine = '╞ Cost: {:>10} exp |'
            if number < 5:

                # Shows cost to level up per stat
                if number == 1:
                    print(choiceLine.format(choice) + costLine.format(str(common.numConversion(int(attack * 1.5)))))
                if number == 2:
                    print(choiceLine.format(choice) + costLine.format(str(common.numConversion(int(defense * 1.5)))))
                if number == 3:
                    costStat = maxStatRecursion(0, experience, 0, attack)
                    expCost = experience + (costStat[1] * -1)
                    expCostFormat = common.numConversion(expCost)
                    if costStat[0] <= 0:
                        print(choiceLine.format(choice) + costLine.format('NA'))
                    else:
                        print(choiceLine.format(choice) + costLine.format(expCostFormat))
                if number == 4:
                    costStat = maxStatRecursion(0, experience, 0, defense)
                    expCost = experience + (costStat[1] * -1)
                    expCostFormat = common.numConversion(expCost)
                    if costStat[0] <= 0:
                        print(choiceLine.format(choice) + costLine.format('NA'))
                    else:
                        print(choiceLine.format(choice) + costLine.format(expCostFormat))

            # Exit Line
            else:
                print(choiceLine.format(choice) + '╞══════════════════════╡')
            number += 1
        print(' ╚═══╩════════════════╧═══════════════════════╡')

        levelupChoice = input(' Choose Selection: ')
        time.sleep(0.2)

        if levelupChoice == '1':
            if experience >= int(attack * 1.5):
                experience -= int(attack * 1.5)

                # Stat Tracking
                stats.addExpOut(int(attack * 1.5))

                level += 1
                attack += 1

            else:
                amount = int(attack * 1.5) - experience
                print(' You need ' + str(amount) + ' more EXP')
                time.sleep(1)

        elif levelupChoice == '2':
            if experience >= int(defense * 1.5):
                experience -= int(defense * 1.5)

                # Stat Tracking
                stats.addExpOut(int(defense * 1.5))

                level += 1
                defense += 1
            else:
                amount = int(defense * 1.5) - experience
                print(' You need ' + str(amount) + ' more EXP')
                time.sleep(1)

        elif levelupChoice == '3':
            changeStats = maxStat(level, experience, attack)
            level += changeStats[0]
            experience = changeStats[1]
            attack += changeStats[2]

        elif levelupChoice == '4':
            changeStats = maxStat(level, experience, defense)
            level += changeStats[0]
            experience = changeStats[1]
            defense += changeStats[2]

        elif levelupChoice == '5':
            levelup = False
            return levelOverview

        else:
            common.clear()
            print(' Invalid Choice.')
