import random
import time
import sys
import common
import saveload

sys.path.insert(0, './func_modules')

fileForge = 'save/forge.txt'
fileCharacter = 'save/saveOverview.txt'

def createForge():
    loadOrder = [0, 0, 0, 0, 0]
    with open(fileForge, 'a+') as save:

        # Set all as 0 on forge build
        save.write(str(loadOrder[0]) + '\n')
        save.write(str(loadOrder[1]) + '\n')
        save.write(str(loadOrder[2]) + '\n')
        save.write(str(loadOrder[3]) + '\n')
        save.write(str(loadOrder[4]) + '\n')

def saveForge(resourceList):
    workingList = resourceList
    with open(fileForge, 'w') as file:
        for item in workingList:
            item = int(item)
            file.write(str(item))
            file.write('\n')

def setForgeChoice(ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, scale, choice):
    weaponMenu = ['Dagger', 'Short Sword', 'Long Sword', 'War Hammer', 'Enchantment Rune']
    armorMenu = ['Hand Guard', 'Helmet', 'Sturdy Brace', 'Tower Shield', 'Reinforced Plate']
    choiceMenu = []
    costMenu = ['2000/250', '3000/800', '5000/1500', '20000/8000', '100000/200000']

    for weapon, armor in zip(weaponMenu, armorMenu):
        choiceMenu.append(weapon)
        choiceMenu.append(armor)

    cost = costMenu[scale]
    oreMetalCost = cost.split('/')
    print(' For one ' + choiceMenu[choice] + ' it will cost;'
                                                    '\n   - ' + oreMetalCost[0] + ' ores'
          '\n   - ' + oreMetalCost[1] + ' metal')
    confirm = input(' Continue with forging? (Y or N) ')

    if confirm.upper() == 'Y':
        oreCost = int(oreMetalCost[0])
        metalCost = int(oreMetalCost[1])
        if ore >= oreCost and metal >= metalCost:
            ore -= oreCost
            metal -= metalCost
            oreBase = oreCost
            metalBase = metalCost
            time.sleep(1)
            return ore, metal, oreBase, metalBase, choice, 0, 0

        else:
            print(' Not enough resources.')
            time.sleep(1)
            return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, 0, 0

    else:
        print(' Confirmation not received.')
        time.sleep(1)
        return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, 0, 0


def forgeSmithing(repeat):
    checkList = False
    resourceList = []

    with open(fileForge, 'r') as file:
        for line in file:
            resourceList.append(int(line))

    # Set names to list on load
    baseList = [resourceList[0], resourceList[1]]
    progressList = [resourceList[2], resourceList[3]]
    chanceTable = [5, 9]
    resourcePointer = 2

    if baseList[0] > 0 and baseList[1] > 0:
        checkList = True

        # Run item forging
        for progress, base, success in zip(progressList, baseList, chanceTable):
            for x in range(1, repeat + 1):
                if progress >= base:
                    pass
                else:
                    if 1 == random.randrange(1, success + 1):
                        resourceList[resourcePointer] += 1
                        progress += 1

            resourcePointer += 1

        saveForge(resourceList)

    else:
        pass

    if checkList == True and baseList == progressList:
        print(' Forge is completed! Go collect your item.')

def forgeFire(ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer):
    weaponMenu = ['Dagger', 'Short Sword', 'Long Sword', 'War Hammer', 'Enchantment Rune']
    armorMenu = ['Hand Guard', 'Helmet', 'Sturdy Brace', 'Tower Shield', 'Reinforced Plates']
    choiceMenu = []
    rewardMenuStat = [100, 100, 250, 250, 550, 550, 1200, 1200, 2800, 2800]
    rewardMenuMuns = [100000, 100000, 300000, 300000, 800000, 800000, 2500000, 2500000, 10000000, 10000000]

    for weapon, armor in zip(weaponMenu, armorMenu):
        choiceMenu.append(weapon)
        choiceMenu.append(armor)

    if oreBase == 0 and metalBase == 0:

        # Print Forge Options
        number = 1
        print(' ╔═══╦═══════════════════╦═══╦═══════════════════╡')
        for weapon, armor in zip(weaponMenu, armorMenu):
            if number == 9:
                choiceLine = ' ╟(' + str(number) + ')╟ ' + '{:<18}' + '╟(0)╟ ' + '{:<18}' + '|'
                print(choiceLine.format(weapon, armor))
            else:
                choiceLine = ' ╟(' + str(number) + ')╟ ' + '{:<18}' + '╟(' + str(number + 1) + ')╟ ' + '{:<18}' + '|'
                print(choiceLine.format(weapon, armor))
                number += 2
        print(' ╚═══╩═══════════════════╩═══╩═══════════════════╡')

        forgeChoice = input(' Please select a project or leave blank to return: ')

        try:
            forgeChoice = int(forgeChoice)

            if forgeChoice == 1:
                forgeAction = setForgeChoice(ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, 0, forgeChoice - 1)
                print(forgeAction)
                ore = forgeAction[0]
                metal = forgeAction[1]
                oreBase = forgeAction[2]
                metalBase = forgeAction[3]
                oreProgress = forgeAction[4]
                metalProgress = forgeAction[5]
                itemChoice = forgeAction[6]
                return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

            elif forgeChoice == 3:
                forgeAction = setForgeChoice(ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, 1, forgeChoice - 1)
                ore = forgeAction[0]
                metal = forgeAction[1]
                oreBase = forgeAction[2]
                metalBase = forgeAction[3]
                oreProgress = forgeAction[4]
                metalProgress = forgeAction[5]
                itemChoice = forgeAction[6]
                return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

            elif forgeChoice == 5:
                forgeAction = setForgeChoice(ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, 2, forgeChoice - 1)
                ore = forgeAction[0]
                metal = forgeAction[1]
                oreBase = forgeAction[2]
                metalBase = forgeAction[3]
                oreProgress = forgeAction[4]
                metalProgress = forgeAction[5]
                itemChoice = forgeAction[6]
                return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

            elif forgeChoice == 7:
                forgeAction = setForgeChoice(ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, 3, forgeChoice - 1)
                ore = forgeAction[0]
                metal = forgeAction[1]
                oreBase = forgeAction[2]
                metalBase = forgeAction[3]
                oreProgress = forgeAction[4]
                metalProgress = forgeAction[5]
                itemChoice = forgeAction[6]
                return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

            elif forgeChoice == 9:
                forgeAction = setForgeChoice(ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, 4, forgeChoice - 1)
                ore = forgeAction[0]
                metal = forgeAction[1]
                oreBase = forgeAction[2]
                metalBase = forgeAction[3]
                oreProgress = forgeAction[4]
                metalProgress = forgeAction[5]
                itemChoice = forgeAction[6]
                return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

            elif forgeChoice == 2:
                forgeAction = setForgeChoice(ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, 0, forgeChoice - 1)
                ore = forgeAction[0]
                metal = forgeAction[1]
                oreBase = forgeAction[2]
                metalBase = forgeAction[3]
                oreProgress = forgeAction[4]
                metalProgress = forgeAction[5]
                itemChoice = forgeAction[6]
                return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

            elif forgeChoice == 4:
                forgeAction = setForgeChoice(ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, 1, forgeChoice - 1)
                ore = forgeAction[0]
                metal = forgeAction[1]
                oreBase = forgeAction[2]
                metalBase = forgeAction[3]
                oreProgress = forgeAction[4]
                metalProgress = forgeAction[5]
                itemChoice = forgeAction[6]
                return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

            elif forgeChoice == 6:
                forgeAction = setForgeChoice(ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, 2, forgeChoice - 1)
                ore = forgeAction[0]
                metal = forgeAction[1]
                oreBase = forgeAction[2]
                metalBase = forgeAction[3]
                oreProgress = forgeAction[4]
                metalProgress = forgeAction[5]
                itemChoice = forgeAction[6]
                return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

            elif forgeChoice == 8:
                forgeAction = setForgeChoice(ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, 3, forgeChoice - 1)
                ore = forgeAction[0]
                metal = forgeAction[1]
                oreBase = forgeAction[2]
                metalBase = forgeAction[3]
                oreProgress = forgeAction[4]
                metalProgress = forgeAction[5]
                itemChoice = forgeAction[6]
                return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

            elif forgeChoice == 0:
                forgeAction = setForgeChoice(ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, 4, 9)
                ore = forgeAction[0]
                metal = forgeAction[1]
                oreBase = forgeAction[2]
                metalBase = forgeAction[3]
                oreProgress = forgeAction[4]
                metalProgress = forgeAction[5]
                itemChoice = forgeAction[6]
                return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

            elif forgeChoice == '':
                return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

            else:
                print(' Invalid choice. Returning to forge...')
                time.sleep(1)
                return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer
        except:
            if forgeChoice == '':
                return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

            else:
                print(' Invalid choice. Returning to forge...')
                time.sleep(1)
                return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

    elif oreProgress == oreBase and metalProgress == metalBase:

        # Check if weapon or armor
        if (itemChoice % 2) == 0:
            atkordef = 'attack'
        else:
            atkordef = 'defense'

        # Alert player to rewards
        print('\n Your ' + choiceMenu[itemChoice] + ' is ready!')
        time.sleep(1)
        print('\n You may take the item for: ')
        print('   (1) ' + str(rewardMenuStat[itemChoice]) + ' ' + atkordef)
        print('   OR')
        print('   (2) ' + str(rewardMenuMuns[itemChoice]) + ' Muns.')
        rewardChoice = input(' Which would you like? (1 or 2) ')

        # Load and change character stats.
        if rewardChoice == '1':

            # Load character stats before stat boost
            statList = []
            statList = saveload.loadOver(fileCharacter, statList)
            statList[1] = int(statList[1])
            statList[4] = int(statList[4])
            statList[5] = int(statList[5])
            if (itemChoice % 2) == 0:
                statList[1] += rewardMenuStat[itemChoice]
                statList[4] += rewardMenuStat[itemChoice]
                print(' Attack raised by ' + str(rewardMenuStat[itemChoice]) + '.')

                # Reset base and choice to 0 and save
                oreBase, metalBase, oreProgress, metalProgress, itemChoice = 0, 0, 0, 0, 0
                time.sleep(1)
                saveload.saveOver(fileCharacter, statList)
                return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

            else:
                statList[1] += rewardMenuStat[itemChoice]
                statList[5] += rewardMenuStat[itemChoice]
                print(' Defense raised by ' + str(rewardMenuStat[itemChoice]) + '.')

                # Reset base and choice to 0 and save
                oreBase, metalBase, oreProgress, metalProgress, itemChoice = 0, 0, 0, 0, 0
                time.sleep(1)
                saveload.saveOver(fileCharacter, statList)
                return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

        # Set for item to be sold for muns
        elif rewardChoice == '2':
            coffer += rewardMenuMuns[itemChoice]
            cofferFormat = common.numConversion(rewardMenuMuns[itemChoice])
            print(' ' + cofferFormat + ' has been put into the coffers.')
            time.sleep(1)
            oreBase, metalBase, oreProgress, metalProgress, itemChoice = 0, 0, 0, 0, 0
            return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

        else:
            print(" Didn't catch that. We'll hold on to this for now.")
            oreBase, metalBase, oreProgress, metalProgress, itemChoice = 0, 0, 0, 0, 0
            return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

    else:
        print(' The forge is running. Please clear the forge if you wish to change.')
        time.sleep(2)
        return ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer

def forgeUpgrade(coffer, forgeLevel, ore, metal):
    # Check if Forge is built
    if forgeLevel == 0:
        build = input('\n Would you like to build a forge for the following materials? '
                      '\n   - 10,000 ore'
                      '\n   - 1,000 metal'
                      '\n   - 1,000,000 Muns'
                      '\n (Y)es or (N)o? ')

        if build.upper() == 'Y':
            if coffer >= 100000 and ore >= 10000 and metal >= 1000:
                coffer -= 100000
                ore -= 10000
                metal -= 1000
                forgeLevel += 1
                createForge()
                return coffer, forgeLevel, ore, metal

            else:
                print(' Not enough resources.')
                time.sleep(1)
                return coffer, forgeLevel, ore, metal

        else:
            print(' Confirmation not received.')
            time.sleep(1)
            return coffer, forgeLevel, ore, metal

    # Run if forge is built
    else:
        forge = True
        actionList = ['Fire Up The Forge', 'Clear The Forge', 'Return to Town']

        # Load Forge values from file
        forgeList = []
        with open(fileForge, 'r') as file:
            for line in file:
                forgeList.append(line)

        oreBase = int(forgeList[0])
        metalBase = int(forgeList[1])
        oreProgress = int(forgeList[2])
        metalProgress = int(forgeList[3])
        itemChoice = int(forgeList[4])

        while forge == True:
            common.clear()

            forgeImport = [coffer, ore, metal]

            cofferFormat = forgeImport[0]
            oreFormat = common.numConversion(forgeImport[1])
            metalFormat = common.numConversion(forgeImport[2])

            # Calculate and set progress
            base = [oreBase * 10, metalBase * 100]
            progress = [oreProgress * 10, metalProgress * 100]
            percent = []
            for max, current in zip(base, progress):
                try:
                    percent.append(int((current / max) * 44))
                except (ZeroDivisionError):
                    percent.append(int(0))

            # Print forge menu
            infoLineOne = ' ╟ Ores: {:17} ╬ Metals: {:13}  ╡'
            infoLineTwo = ' ╟{:>24} ╬{:>23} ╡'
            infoLineProgress = '{:<44}'
            infoLineThree = ' ╟  [' + infoLineProgress + ']  ╡'

            # Forge resource line
            print(' ╔══════════════════════════════════════════════════╡')
            print(infoLineOne.format(' ', ' ', ' '))
            print(infoLineTwo.format(oreFormat, metalFormat))

            # Forge Progress
            print(' ╠══════════════════════════════════════════════════╡')
            print(' ╠                                                  ╡')
            print(' ╠                  Forge Progress                  ╡')
            print(infoLineThree.format('▓' * int((percent[0] + percent[1]) / 2)))
            print(' ╠                                                  ╡')
            print(' ╠═══╦══════════════════════════════════════════════╡')

            # Print option list
            choiceNum = 1
            for choice in actionList:
                choiceLine = (' ╠(' + str(choiceNum) + ')╬ ' + '{:<44} ╡')
                print(choiceLine.format(choice))
                choiceNum += 1

            print(' ╚═══╩══════════════════════════════════════════════╡')

            forgeAction = input(' Choose selection: ')

            if forgeAction == '1':
                actionReturn = forgeFire(ore, metal, oreBase, metalBase, oreProgress, metalProgress, itemChoice, coffer)
                print(actionReturn)
                ore = actionReturn[0]
                metal = actionReturn[1]
                oreBase = forgeList[0] = actionReturn[2]
                metalBase = forgeList[1] = actionReturn[3]
                oreProgress = forgeList[2] = actionReturn[4]
                metalProgress = forgeList[3] = actionReturn[5]
                itemChoice = forgeList[4] = actionReturn[6]
                coffer = actionReturn[7]

            elif forgeAction == '2':
                confirm = input(' You will not be able to recover anything.\n Are you sure you want to clear the forge?(Y or N) ')
                if confirm.upper() == 'Y':
                    forgeList = [0, 0, 0, 0, 0]
                    print(' The forge has been emptied.')
                    time.sleep(1)

                else:
                    print(' Resuming forge...')
                    time.sleep(1)

            elif forgeAction == '3':
                forge = False
                print(forgeList)
                saveForge(forgeList)
                return coffer, forgeLevel, ore, metal

            else:
                print('Invalid input.')
                time.sleep(1)
