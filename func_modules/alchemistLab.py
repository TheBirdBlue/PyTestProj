import random
import time
import sys
import common
import saveload

sys.path.insert(0, './func_modules')

fileAlchemist = 'save/alchemistLab.txt'
fileCharacter = 'save/saveOverview.txt'

def createAlchemist():
    loadOrder = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    with open(fileAlchemist, 'a+') as save:

        # Set all as 0 on alchemist build
        save.write(str(loadOrder[0]) + '\n')
        save.write(str(loadOrder[1]) + '\n')
        save.write(str(loadOrder[2]) + '\n')
        save.write(str(loadOrder[3]) + '\n')
        save.write(str(loadOrder[4]) + '\n')
        save.write(str(loadOrder[5]) + '\n')
        save.write(str(loadOrder[6]) + '\n')
        save.write(str(loadOrder[7]) + '\n')
        save.write(str(loadOrder[8]) + '\n')

def saveAlchemist(resourceList):
    workingList = resourceList
    with open(fileAlchemist, 'w') as file:
        for item in workingList:
            file.write(str(item))
            file.write('\n')

def alchemistCollection(repeat):
    checkList = False
    resourceList = []
    with open(fileAlchemist, 'r') as file:
        for line in file:
            resourceList.append(int(line))

    # Set names on to list on load
    leafRed = resourceList[0]
    leafBlue = resourceList[1]
    leafGold = resourceList[2]
    slotRedBase = resourceList[3]
    slotBlueBase = resourceList[4]
    slotGoldBase = resourceList[5]
    slotRedProgress = resourceList[6]
    slotBlueProgress = resourceList[7]
    slotGoldProgress = resourceList[8]

    # The many needed lists
    leafList = [leafRed, leafBlue, leafGold]
    dropTable = [100, 100, 1000]
    baseList = [slotRedBase, slotBlueBase, slotGoldBase]
    progressList = [slotRedProgress, slotBlueProgress, slotGoldProgress]
    resourceGain = []


    # Run leaf collection
    resourcePointer = 0
    for leaf, drop in zip(leafList, dropTable):
        count = 0
        for x in range(1, repeat + 1):
            if 1 == random.randrange(1, drop + 1):
                resourceList[resourcePointer] += 1
                count += 1

        resourceGain.append(count)
        resourcePointer += 1

    # Run potion brewing
    resourcePointer = 6
    for progress, base, success in zip(progressList, baseList, dropTable):
        for x in range(1, repeat + 1):
            if resourceList[resourcePointer] >= base:
                pass
            else:
                if 1 == random.randrange(1, success + 1):
                    resourceList[resourcePointer] += 1

        resourcePointer += 1

    saveAlchemist(resourceList)

    # Display leaf gains
    if resourceGain[0] > 0 or resourceGain[1] > 0 or resourceGain[2] > 0:
        print('\n')

    if resourceGain[0] > 0:
        if resourceGain[0] > 1:
            print(' Gained ' + str(resourceGain[0]) + ' red leaves.')
            time.sleep(1)
        else:
            print(' Gained ' + str(resourceGain[0]) + ' red leaf.')
            time.sleep(1)
    else:
        pass

    if resourceGain[1] > 0:
        if resourceGain[0] > 1:
            print(' Gained ' + str(resourceGain[1]) + ' blue leaves.')
            time.sleep(1)
        else:
            print(' Gained ' + str(resourceGain[1]) + ' blue leaf.')
            time.sleep(1)
    else:
        pass

    if resourceGain[2] > 0:
        if resourceGain[0] > 1:
            print(' Gained ' + str(resourceGain[2]) + ' gold leaves.')
            time.sleep(1)
        else:
            print(' Gained ' + str(resourceGain[2]) + ' gold leaf.')
            time.sleep(1)
    else:
        pass

def workPotion(action, resource, base, progress):
    action -= 1
    word = ['red', 'blue', 'gold']
    stat = ['attack', 'defense', 'special']
    print(' You currently have ' + str(resource) + ' ' + word[action] + ' leaves.')

    if base == 0:
        setLeaves = input('\n How many leaves would you like to use? ')
        try:
            setLeaves = int(setLeaves)
            if setLeaves <= resource:
                base = setLeaves
                resource -= setLeaves
                print(' Creating ' + word[action] + ' potion with ' + str(setLeaves) + ' leaves.')
                time.sleep(1)
                return resource, base, progress
            else:
                print(' Not enough ' + word[action] + ' leaves available.')
                time.sleep(1)
                return resource, base, progress

        except:
            print(' Invalid input.')
            time.sleep(1)
            return resource, base, progress

    elif progress < base:
        print('\n Your potion is still brewing...')
        time.sleep(1)
        return resource, base, progress

    elif progress == base:
        confirm = input('\n Your potion is ready! Would you like to drink it? (Y or N) ')
        if confirm.upper() == 'Y':
            charList = []

            # Load current character
            charList = saveload.loadOver(fileCharacter, charList)

            # Change character values
            charList[1] = int(charList[1]) + base
            charList[action + 4] = int(charList[action + 4]) + base

            # Save changed values to be reloaded on town exit
            saveload.saveOver(fileCharacter, charList)
            print(' Your ' + stat[action] + ' and level increased by ' + str(base) + '.')
            time.sleep(2)
            base = 0
            progress = 0
            return resource, base, progress

        else:
            print(' Confirmation not received.')
            time.sleep(1)
            return resource, base, progress

def alchemistUpgrade(coffer, alchemistLevel):

    # Check if Alchemist is built
    if alchemistLevel == 0:
        build = input('\n Would you like to invite an alchemist for 100,000 Muns? (Y or N)')
        if build.upper() == 'Y':
            if coffer >= 100000:
                coffer -= 100000
                alchemistLevel += 1
                createAlchemist()
                return coffer, alchemistLevel

            else:
                print(' Not enough in the coffers.')
                time.sleep(1)
                return coffer, alchemistLevel

        else:
            print(' Confirmation not received.')
            time.sleep(1)
            return coffer, alchemistLevel

    else:
        alchemy = True
        actionList = ['Red Pot', 'Blue Pot', 'Gold Pot', 'Return to Town']

        # Load Alchemist values from file
        alchemistList = []
        with open(fileAlchemist, 'r') as file:
            for line in file:
                alchemistList.append(line)

        leafRed = int(alchemistList[0])
        leafBlue = int(alchemistList[1])
        leafGold = int(alchemistList[2])
        slotRedBase = int(alchemistList[3])
        slotBlueBase = int(alchemistList[4])
        slotGoldBase = int(alchemistList[5])
        slotRedProgress = int(alchemistList[6])
        slotBlueProgress = int(alchemistList[7])
        slotGoldProgress = int(alchemistList[8])

        while alchemy == True:
            common.clear()


            workingList = [leafRed, leafBlue, leafGold, slotRedBase, slotBlueBase, slotGoldBase, slotRedProgress,
                           slotBlueProgress, slotGoldProgress]

            # Calculate and set progress
            base = [slotRedBase, slotBlueBase, slotGoldBase]
            progress = [slotRedProgress, slotBlueProgress, slotGoldProgress]
            percent = []
            for max, current in zip(base, progress):
                try:
                    percent.append(int((current/max) * 10))
                except (ZeroDivisionError):
                    percent.append(int(0))

            # Print Alchemist menu
            infoLineOne = ' ╟ Red Leafs:{:4} ╬ Blue Leafs:{:3} ╬ Gold Leafs:{:3} ╡'
            infoLineTwo = ' ╟{:>15} ╬{:>15} ╬{:>15} ╡'
            infoLineProgress = '{:<10}'
            infoLineThree = ' ╟  [' + infoLineProgress + ']  ╬  [' + infoLineProgress + ']  ╬  [' + infoLineProgress + ']  ╡'

            # Alchemist resource line
            number = 1
            print(' ╔════════════════╦════════════════╦════════════════╡')
            print(infoLineOne.format(' ', ' ', ' '))
            print(infoLineTwo.format(leafRed, leafBlue, leafGold))

            # Brewing stations
            print(' ╠════════════════╬════════════════╬════════════════╡')
            print(' ╠                ╬                ╬                ╡')
            print(' ╠    Red Pot     ╬    Blue Pot    ╬    Gold Pot    ╡')
            print(infoLineThree.format('▓'*percent[0], '▓'*percent[1], '▓'*percent[2]))
            print(' ╠                ╬                ╬                ╡')
            print(' ╠═══╦════════════╬════════════════╬════════════════╡')

            # Print option list
            choiceNum = 1
            for choice in actionList:
                choiceLine = (' ╠(' + str(choiceNum) + ')╬ ' + '{:<44} ╡')
                print(choiceLine.format(choice))
                choiceNum += 1

            print(' ╚═══╩══════════════════════════════════════════════╡')

            alchemyAction = input(' Choose selection:')

            if alchemyAction == '1':
                transaction = workPotion(1, leafRed, slotRedBase, slotRedProgress)
                leafRed = alchemistList[0] = transaction[0]
                slotRedBase = alchemistList[3] = transaction[1]
                slotRedProgress = alchemistList[6] = transaction[2]

            elif alchemyAction == '2':
                transaction = workPotion(2, leafBlue, slotBlueBase, slotBlueProgress)
                leafBlue = alchemistList[1] = transaction[0]
                slotBlueBase = alchemistList[4] = transaction[1]
                slotBlueProgress = alchemistList[7] = transaction[2]

            elif alchemyAction == '3':
                transaction = workPotion(3, leafGold, slotGoldBase, slotGoldProgress)
                leafGold = alchemistList[2] = transaction[0]
                slotGoldBase = alchemistList[5] = transaction[1]
                slotGoldProgress = alchemistList[8] = transaction[2]

            elif alchemyAction == '4':
                saveAlchemist(workingList)
                alchemy = False
                return coffer, alchemistLevel
