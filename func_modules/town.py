import random
import time
import common
import stats
import alchemistLab
import forge
import guild

fileLocation = 'save/saveResources.txt'
lMenu = ['Deposit', 'Lumber Mill', 'Blacksmith', 'Alchemist', 'Guild']
rMenu = ['Withdraw', 'Mines', 'Population', 'Forge', 'Return']

def writeResources(resourceList):
    workList = resourceList
    with open(fileLocation, 'w') as file:
        for item in resourceList:
            file.write(str(item))
            file.write('\n')

def deposit(money, coffer):
    money = int(money)
    coffer = int(coffer)
    munChange = input(' How much would you like to deposit? ')
    try:
        munChange = int(munChange)
        if munChange <= money:
            money -= munChange
            coffer += munChange

            print(' Deposited ' + common.numConversion(munChange) + ' into the coffers.')
            time.sleep(1)
            return money, coffer

        else:
            print(' Not enough Muns')
            return money, coffer

    except:
        print(' Invalid input.')

def withdraw(money, coffer):
    money = int(money)
    coffer = int(coffer)
    munChange = input(' How much would you like to withdraw? ')
    try:
        munChange = int(munChange)
        if munChange <= coffer:
            money += munChange
            coffer -= munChange

            print(' Withdrew ' + common.numConversion(munChange) + ' from the coffers.')
            time.sleep(1)
            return money, coffer

        else:
            print(' Not enough Muns')
            return money, coffer

    except:
        print(' Invalid input.')

def upLumber(coffer, wood, lumber):
    if lumber == 0:
        confirm = input(' Would you like to build the Lumber Yard for 1000 Muns? (Y or N) ')
        if confirm.upper() == 'Y':
            if coffer >= 1000:
                cofferFinal = coffer - 1000
                stats.addMoneyTransaction(- 1000)
                lumberFinal = lumber + 1
                return cofferFinal, wood, lumberFinal

            else:
                print(' Not enough money in the coffers.')
                time.sleep(1)
                return coffer, wood, lumber

        else:
            print(' Confirmation not received.')
            time.sleep(1)
            return coffer, wood, lumber

    else:
        levelUpMun = lumber * 1000
        levelUpResource = lumber * 155
        print(' It will cost the following resources to upgrade the Lumber Yard:')
        print('  - ' + common.numConversion(levelUpResource) + ' Wood')
        print('  - ' + common.numConversion(levelUpMun) + ' Muns')
        confirm = input(' Do you want to continue? (Y or N) ')
        if confirm.upper() == 'Y':
            if wood >= levelUpResource and coffer >= levelUpMun:
                wood -= levelUpResource
                coffer -= levelUpMun
                stats.addMoneyTransaction(- levelUpMun)
                lumber += 1
                return coffer, wood, lumber

            else:
                print(' Not enough resources.')
                time.sleep(1)
                return coffer, wood, lumber

        else:
            print(' Confirmation not received')
            time.sleep(1)
            return coffer, wood, lumber

def upMine(coffer, wood, ore, mine):
    if mine == 0:
        confirm = input(' Would you like to build the Mine for 1000 wood? (Y or N) ')
        if confirm.upper() == 'Y':
            if wood >= 1000:
                wood -= 1000
                mine += 1
                return coffer, wood, ore, mine

            else:
                print(' Not enough wood available.')
                time.sleep(1)
                return coffer, wood, ore, mine

        else:
            print(' Confirmation not received.')
            time.sleep(1)
            return coffer, wood, ore, mine

    else:
        levelUpMun = mine * 1000
        levelUpResource = mine * 155
        print(' It will cost the following resources to upgrade the Mines:')
        print('  - ' + common.numConversion(levelUpResource) + ' ore')
        print('  - ' + common.numConversion(levelUpMun) + ' Muns')
        confirm = input(' Do you want to continue? (Y or N) ')
        if confirm.upper() == 'Y':
            if ore >= levelUpResource and coffer >= levelUpMun:
                ore -= levelUpResource
                coffer -= levelUpMun
                stats.addMoneyTransaction(- levelUpMun)
                mine += 1
                return coffer, wood, ore, mine

            else:
                print(' Not enough resources.')
                time.sleep(1)
                return coffer, wood, ore, mine

        else:
            print(' Confirmation not received.')
            time.sleep(1)
            return coffer, wood, ore, mine

def upSmith(coffer, ore, metal, smith):
    if smith == 0:
        confirm = input(' Would you like to build the Blacksmith for 1000 ore? (Y or N) ')
        if confirm.upper() == 'Y':
            if ore >= 1000:
                ore -= 1000
                smith += 1
                return coffer, ore, metal, smith

            else:
                print(' Not enough ore available.')
                time.sleep(1)
                return coffer, ore, metal, smith

        else:
            print(' Confirmation not received.')
            time.sleep(1)
            return coffer, ore, metal, smith

    else:
        levelUpMun = smith * 1000
        levelUpResource = smith * 155
        print(' It will cost the following resources to upgrade the Blacksmith:')
        print('  - ' + common.numConversion(levelUpResource) + ' metal')
        print('  - ' + common.numConversion(levelUpMun) + ' Muns')
        confirm = input(' Do you want to continue? (Y or N) ')
        if confirm.upper() == 'Y':
            if metal >= levelUpResource and coffer >= levelUpMun:
                metal -= levelUpResource
                coffer -= levelUpMun
                stats.addMoneyTransaction(- levelUpMun)
                smith += 1
                return coffer, ore, metal, smith

            else:
                print(' Not enough resources.')
                time.sleep(1)
                return coffer, ore, metal, smith

        else:
            print(' Confirmation not received.')
            time.sleep(1)
            return coffer, ore, metal, smith

def populationControl(coffer, population):
    print(' Would you like to bring in or remove people?')
    hireorfire = input(" '+' to add or '-' to remove: (Eg. +3 or -2)")

    # Check if +
    if hireorfire.startswith('+'):
        useOne = hireorfire.replace('+', '')
        useTwo = useOne.replace(' ', '')

        try:
            useThree = int(useTwo)

            if coffer >= useThree * 10000:
                useThreeFormat = common.numConversion(useThree * 10000)
                print(' It will cost ' + useThreeFormat + ' Muns from the coffer')
                confirm = input(' Continue with hiring? (Y or N)')

                if confirm.upper() == 'Y':
                    coffer -= useThree * 10000
                    population += useThree

                    # Stat Tracking
                    stats.addMoneyTransaction(- (useThree * 10000))

                    return coffer, population

                else:
                    return coffer, population

            else:
                print(' Not enough in the coffers.')
                time.sleep(1)
                return coffer, population

        except:
            print('Invalid input.')
            time.sleep(1)
            return coffer, population

    # Check if -
    elif hireorfire.startswith('-'):
        useOne = hireorfire.replace('-', '')
        useTwo = useOne.replace(' ', '')

        try:
            useThree = int(useTwo)

            if useThree <= population:
                print(' ' + common.numConversion(useThree * 100) + ' will be returned to the coffer.')
                confirm = input(' Continue with firing? (Y or N)')

                if confirm.upper() == 'Y':
                    coffer += useThree * 100
                    population -= useThree

                    # Stat Tracking
                    stats.addMoneyTransaction(useThree * 100)

                    return coffer, population

                else:
                    return coffer, population

            else:
                print(' Not enough in the population.')
                time.sleep(1)
                return coffer, population

        except:
            print(' Invalid input.')
            time.sleep(1)
            return coffer, population

    else:
        print(' Invalid input.')
        time.sleep(1)
        return coffer, population

def resourceCollection(repeat):
    checkList = False
    resourceList = []
    with open(fileLocation, 'r') as file:
        for line in file:
            resourceList.append(int(line))

    # Set names to list on load
    itemWood = resourceList[0]
    itemOre = resourceList[1]
    itemMetal = resourceList[2]
    levelLumber = resourceList[3]
    levelMine = resourceList[4]
    levelSmith = resourceList[5]
    levelAlchemist = resourceList[6]
    levelForge = resourceList[7]
    levelGuild = resourceList[8]
    coffer = resourceList[9]
    population = resourceList[10]
    search = 1

    # Set list for loop and resources
    building = ['Lumber', 'Mine', 'Blacksmith']
    buildingLoop = [levelLumber, levelMine, levelSmith]
    resourceGains = [0, 0, 0]
    buildingLoopLocation = 0

    # Begin resource gathering
    if levelLumber > 0 or levelMine > 0 or levelSmith > 0:
        for stock, name in zip(buildingLoop, building):
            moneySpent = 0
            stockBase = stock
            resource = 0

            # Check if building has been built and population to work
            if stock > 0 and population > 0 and resourceList[9] >= 100:
                for run in range(1, repeat + 1):

                    # Run chance per population
                    if population > 0 and resourceList[9] >= 100:
                        checkList = True
                        for count in range(1, population + 1):
                            if resourceList[9] >= 100:

                                # Gain guaranteed resources
                                stock = stockBase
                                while stock > 100:
                                    resource += 1
                                    stock -= 100

                                chanceGrab = random.randrange(0, 100)
                                if chanceGrab <= stock:
                                    resourceList[9] -= 100
                                    resource += 1
                                    moneySpent -= 100
                                else:
                                    resourceList[9] -= 10
                                    moneySpent -= 10

                            else:
                                pass

                resourceGains[buildingLoopLocation] += resource

            else:
                resourceGains[buildingLoopLocation] += 0
            buildingLoopLocation += 1

            stats.addMoneyTransaction(moneySpent)

    formatted = []
    for value in resourceGains:
        formatted.append(common.numConversion(value))

    resultLineOne = ' The town has gained ' + formatted[0] + ' wood.'
    resultLineTwo = ' The town has gained ' + formatted[1] + ' ore.'
    resultLineThree = ' The town has gained ' + formatted[2] + ' metal.'

    # Print finds
    if resourceGains[0] > 0 or resourceGains[1] > 0 or resourceGains[2] > 0:
        print('\n')
    if resourceGains[0] > 0:
        print(resultLineOne)
        resourceList[0] += resourceGains[0]
        time.sleep(1)
    if resourceGains[1] > 0:
        print(resultLineTwo)
        resourceList[1] += resourceGains[1]
        time.sleep(1)
    if resourceGains[2] > 0:
        print(resultLineThree)
        resourceList[2] += resourceGains[2]
        time.sleep(1)
    if resourceList[9] < 100 and checkList == True:
        time.sleep(1)
        print('\n The coffers are empty! No one will work until paid.')
        time.sleep(1)

    if levelAlchemist > 0:
        alchemistLab.alchemistCollection(repeat)

    if levelForge > 0:
        forge.forgeSmithing(repeat)

    if levelGuild > 0:
        guild.guildProcess(repeat, levelGuild)

    writeResources(resourceList)

def sellResources(choice, woodVariable, oreVariable, metalVariable):
    resourceList = []
    with open(fileLocation, 'r') as file:
        for line in file:
            resourceList.append(int(line))

    # Set names to list on load
    itemWood = resourceList[0]
    itemOre = resourceList[1]
    itemMetal = resourceList[2]
    levelLumber = resourceList[3]
    levelMine = resourceList[4]
    levelSmith = resourceList[5]
    levelAlchemist = resourceList[6]
    levelForge = resourceList[7]
    levelGuild = resourceList[8]
    coffer = resourceList[9]
    population = resourceList[10]

    # Set series of variables
    infoPull = ['wood', 'ore', 'metal']
    infoPrice = [10 + woodVariable, 500 + oreVariable, 1000 + metalVariable]
    print(' You have ' + common.numConversion(resourceList[choice]) + ' ' + infoPull[choice] + ' that sells for '\
        + common.numConversion(infoPrice[choice]) + ' each.')
    sellNumber = input(' How many would you like to sell? ')

    try:
        sellNumber = int(sellNumber)
        if sellNumber <= resourceList[choice]:
            totalPrice = infoPrice[choice] * sellNumber
            print(' That will be ' + common.numConversion(totalPrice) + ' Muns for ' + common.numConversion(sellNumber)
                  + ' ' + infoPull[choice] + '.')
            confirm = input(' Confirm the sale? (Y or N)')
            if confirm.upper() == 'Y':
                resourceList[9] += totalPrice
                resourceList[choice] -= sellNumber

                print(' ' + common.numConversion(sellNumber) + ' ' + infoPull[choice] + ' sold for '
                      + common.numConversion(totalPrice) + '.')
                print(' The money was sent to the town coffer.')
                time.sleep(2)

                stats.addMoneyTransaction(totalPrice)
                writeResources(resourceList)

            else:
                pass

        else:
            print(' Not enough resources.')
            time.sleep(1)

    except:
        print(' Invalid input.')
        time.sleep(1)

def townFunction(money):
    resourceList = []
    town = True

    # Open File and load to variable
    # Wood, Ore, Metal, Lumber, Mine, Smith, Coffer, Population
    with open(fileLocation, 'r') as file:
        for line in file:
            resourceList.append(int(line))

    # Set names to list on load
    itemWood = resourceList[0]
    itemOre = resourceList[1]
    itemMetal = resourceList[2]
    levelLumber = resourceList[3]
    levelMine = resourceList[4]
    levelSmith = resourceList[5]
    levelAlchemist = resourceList[6]
    levelForge = resourceList[7]
    levelGuild = resourceList[8]
    coffer = resourceList[9]
    population = resourceList[10]

    workingList = [itemWood, itemOre, itemMetal, levelLumber, levelMine, levelSmith, levelAlchemist, levelForge,
                   levelGuild, coffer, population]

    while town == True:
        common.clear()

        workingFormat = []

        # Run values through formatting function
        for value in workingList:
            workingFormat.append(common.numConversion(value))

        itemWoodFormat = workingFormat[0]
        itemOreFormat = workingFormat[1]
        itemMetalFormat = workingFormat[2]
        cofferFormat = workingFormat[9]
        populationFormat = workingFormat[10]
        moneyFormat = common.numConversion(money)

        # Set Building Names if built
        if levelLumber > 0:
            buildingOne = 'Lumber Mill'
            buildingOneLevel = levelLumber
        else:
            buildingOne = '[EMPTY LOT]'
            buildingOneLevel = levelLumber

        if levelMine > 0:
            buildingTwo = 'Mines'
            buildingTwoLevel = levelMine
        else:
            buildingTwo = '[EMPTY LOT]'
            buildingTwoLevel = levelMine

        if levelSmith > 0:
            buildingThree = 'Blacksmith'
            buildingThreeLevel = levelSmith
        else:
            buildingThree = '[EMPTY LOT]'
            buildingThreeLevel = levelSmith

        if levelAlchemist > 0:
            buildingFour = 'Alchemist'
            buildingFourLevel = levelAlchemist
        else:
            buildingFour = '[EMPTY LOT]'
            buildingFourLevel = levelAlchemist

        if levelForge > 0:
            buildingFive = 'Forge'
            buildingFiveLevel = levelForge
        else:
            buildingFive = '[EMPTY LOT]'
            buildingFiveLevel = levelForge

        if levelGuild > 0:
            buildingSix = 'Guild'
            buildingSixLevel = levelGuild
        else:
            buildingSix = '[EMPTY LOT]'
            buildingSixLevel = levelGuild

        # Line set up for printing
        infoLineOne = ' ╟ Wood:{:8} ╬ Ore:{:9} ╬ Metal:{:7} ╡'
        infoLineTwo = ' ╟{:>14} ╬{:>14} ╬{:>14} ╡'
        infoLineThree = ' ╟{:^15}╬{:^15}╬{:^15}╡'
        centered = ' Lv:' + '{}'

        # Set up lists for spacing set up

        spacing = [16, 16, 16, 16, 16, 16]
        buildingCheck = [buildingOneLevel, buildingTwoLevel, buildingThreeLevel, buildingFourLevel, buildingFiveLevel,
                         buildingSixLevel]
        spaceCount = 0

        for building, space in zip(buildingCheck, spacing):
            if building >= 10:
                spacing[spaceCount] = 15
            if building >= 100:
                spacing[spaceCount] = 14
            if building >= 1000:
                spacing[spaceCount] = 13
            if building >= 10000:
                spacing[spaceCount] = 12

            spaceCount += 1

        infoLineFour = ' ╟' + centered.center(spacing[0], ' ') + '╬' + centered.center(spacing[1], ' ') + '╬'\
                       + centered.center(spacing[2], ' ') + '╡'
        infoLineFive = ' ╟               ╬               ╬' + centered.center(spacing[5], ' ') + '╡'
        infoLineSix = ' ╟ Money: {:>6} ╬ Coffer: {:>5} ╬ Population: {:>1} ╡'

        # Line printing
        number = 1
        print(' ╔═══════════════╦═══════════════╦═══════════════╡')
        print(infoLineOne.format(' ', ' ', ' '))
        print(infoLineTwo.format(itemWoodFormat, itemOreFormat, itemMetalFormat))

        # First set of buildings
        print(' ╠═══════════════╬═══════════════╬═══════════════╡')
        print(' ╠               ╬               ╬               ╡')
        print(infoLineThree.format(buildingOne, buildingTwo, buildingThree))
        print(infoLineFour.format(buildingOneLevel, buildingTwoLevel, buildingThreeLevel))
        print(' ╠               ╬               ╬               ╡')
        print(' ╠═══════════════╬═══════════════╬═══════════════╡')

        # Second set of buildings
        print(' ╠               ╬               ╬               ╡')
        print(infoLineThree.format(buildingFour, buildingFive, buildingSix))
        print(infoLineFive.format(buildingSixLevel))
        print(' ╠               ╬               ╬               ╡')
        print(' ╠═══════════════╬═══════════════╬═══════════════╡')

        print(infoLineSix.format(' ', ' ', ' '))
        print(infoLineTwo.format(moneyFormat, cofferFormat, populationFormat))
        print(' ╠═══╦═══════════╩═══════╦═══╦═══╩═══════════════╡')
        for choiceL, choiceR in zip(lMenu, rMenu):
            if number == 9:
                choiceLine = ' ╟(' + str(number) + ')╟ ' + '{:<18}' + '╟(0)╟ ' + '{:<18}' + '|'
                print(choiceLine.format(choiceL, choiceR))
            else:
                choiceLine = ' ╟(' + str(number) + ')╟ ' + '{:<18}' + '╟(' + str(number + 1) + ')╟ '+ '{:<18}' + '|'
                print(choiceLine.format(choiceL, choiceR))
                number += 2
        print(' ╚═══╩═══════════════════╩═══╩═══════════════════╡')

        townaction = input(' Choose selection: ')

        if townaction == '0':
            town = False
            writeResources(workingList)
            time.sleep(1)
            return money

        elif townaction == '1':
            transaction = deposit(money, coffer)
            money = transaction[0]
            coffer = workingList[9] = transaction[1]

        elif townaction == '2':
            transaction = withdraw(money, coffer)
            money = transaction[0]
            coffer = workingList[9] = transaction[1]

        elif townaction == '3':
            transaction = upLumber(coffer, itemWood, levelLumber)
            coffer = workingList[9] = transaction[0]
            itemWood = workingList[0] = transaction[1]
            levelLumber = workingList[3] = transaction[2]

        elif townaction == '4':
            transaction = upMine(coffer, itemWood, itemOre, levelMine)
            coffer = workingList[9] = transaction[0]
            itemWood = workingList[0] = transaction[1]
            itemOre = workingList[1] = transaction[2]
            levelMine = workingList[4] = transaction[3]

        elif townaction == '5':
            transaction = upSmith(coffer, itemOre, itemMetal, levelSmith)
            coffer = workingList[9] = transaction[0]
            itemOre = workingList[1] = transaction[1]
            itemMetal = workingList[2] = transaction[2]
            levelSmith = workingList[5] = transaction[3]

        elif townaction == '6':
            transaction = populationControl(coffer, population)
            coffer = workingList[9] = transaction[0]
            population = workingList[10] = transaction[1]

        elif townaction == '7':
            transaction = alchemistLab.alchemistUpgrade(coffer, levelAlchemist)
            coffer = workingList[9] = transaction[0]
            levelAlchemist = workingList[6] = transaction[1]

        elif townaction == '8':
            transaction = forge.forgeUpgrade(coffer, levelForge, itemOre, itemMetal)
            coffer = workingList[9] = transaction[0]
            levelForge = workingList[7] = transaction[1]
            itemOre = workingList[1] = transaction[2]
            itemMetal = workingList[2] = transaction[3]


        elif townaction == '9':
            transaction = guild.guildUpgrade(coffer, population, levelGuild, itemWood, itemOre, itemMetal)
            coffer = workingList[9] = transaction[0]
            population = workingList[10] = transaction[1]
            levelGuild = workingList[8] = transaction[2]
            itemWood = workingList[0] = transaction[3]
            itemOre = workingList[1] = transaction[4]
            itemMetal = workingList[2] = transaction[5]
