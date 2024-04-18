import time
import common
import stats
import saveload

fileGuild = 'save/saveGuild.txt'
fileChar = 'save/saveOverview.txt'

def createGuild():
    # Guild Name, members, woodStored, oreStored, metalStored, experienceStored
    loadOrder =  ['', 1, 0, 0, 0, 0, 0, 0, 0]
    guildName = input(' What is your guild name? ')
    loadOrder[0] = guildName

    with open(fileGuild, 'a+') as save:

        # Set all as 0 on forge build
        save.write(str(loadOrder[0]) + '\n')
        save.write(str(loadOrder[1]) + '\n')
        save.write(str(loadOrder[2]) + '\n')
        save.write(str(loadOrder[3]) + '\n')
        save.write(str(loadOrder[4]) + '\n')
        save.write(str(loadOrder[5]) + '\n')
        save.write(str(loadOrder[6]) + '\n')
        save.write(str(loadOrder[7]) + '\n')
        save.write(str(loadOrder[8]) + '\n')

def saveGuild(resourceList):
    workingList = resourceList
    with open(fileGuild, 'w') as file:
        for item in workingList:
            item = str(item)
            item = item.replace('\n', '')
            file.write(str(item))
            file.write('\n')

def trainMembers(experience, population, members):
    if experience >= 1000:
        print("\n It's 1000 experience to train someone in guild work.")
        print(" You have " + str(population) + " population.")
        training = input(' How many would you like to train? ')

        try:
            trainingNum = int(training)
            expNeed = trainingNum * 1000
            if experience >= expNeed:
                print(' Training ' + training + ' new members...')
                time.sleep(1)
                experience -= expNeed
                population -= trainingNum
                members += trainingNum
                print(experience, population, members)
                return experience, population, members

            elif trainingNum >= population:
                print(' Not enough in the town to train.')
                time.sleep(1)
                return experience, population, members

            elif expNeed >= experience:
                difference = expNeed - experience
                print(' Need ' + common.numConversion(difference) + ' more experience.')
                time.sleep(1)
                return experience, population, members

            else:
                print(" Can't do that.")
                time.sleep(1)
                return experience, population, members

        except:
            print(' Invalid input.')
            return experience, population, members

    else:
        print(' You need 1000 experience to train a new member.')
        time.sleep(1)
        return experience, population, members

def donate(material, stored, pointer):
    pointerList = ['wood', 'ore', 'metal']
    print('\n You have ' + common.numConversion(material) + ' ' + pointerList[pointer] + '.')
    print(' PLEASE NOTE: Once you donate these materials, you cannot get them back.')
    deposit = input(' How many would you like to donate? ')

    try:
        deposit = int(deposit)

        if deposit <= material:
            material -= deposit
            stored += deposit
            print(' Donated ' + common.numConversion(deposit) + ' ' + pointerList[pointer] + ' to the guild.')
            time.sleep(1)
            return material, stored

        else:
            print(' Not enough resources.')
            time.sleep(1)
            return material, stored

    except:
        print(' Invalid input.')
        time.sleep(1)
        return material, stored

def withdraw(experience):
    print('\n You have ' + common.numConversion(experience) + ' exp available.')
    withdraw = input(' How much would you like to take? ')

    try:
        withdraw = int(withdraw)

        if withdraw <= experience:

            # Create list and load character stats
            workingList = []
            workingList = saveload.loadOver(fileChar, workingList)
            workingList[2] = int(workingList[2])
            workingList[2] += withdraw
            experience -= withdraw

            # Save experience to character file
            saveload.saveOver(fileChar, workingList)

            return experience

        else:
            print(' Not enough experience.')
            time.sleep(1)
            return experience

    except:
        print(' Invalid input.')
        time.sleep(1)
        return experience

def guildProcess(repeat, level):
    guildList = []
    with open(fileGuild) as save:
        for line in save:
            guildList.append(line)

    guildName = guildList[0]
    members = int(guildList[1])
    woodStored = int(guildList[2])
    oreStored = int(guildList[3])
    metalStored = int(guildList[4])
    experienceStored = int(guildList[5])

    materialList = [metalStored, oreStored, woodStored]
    rewardList = [25, 5, 1]

    #Initial checks to see if guild needs to run
    if experienceStored <= (level * 1000) + (members * 100):
        if woodStored > 0 or oreStored > 0 or metalStored > 0:

            # Begin run
            for x in range(1, repeat + 1):
                usedMaterials = []

                # Recheck exp and resources
                for resource, reward in zip(materialList, rewardList):
                    for body in range(1, members + 1):
                        if experienceStored <= (level * 1000):
                            openSpace = ((level * 1000) + (members * 100)) - experienceStored
                            if resource == 0 or openSpace < reward:
                                pass
                            else:
                                resource -= 1
                                experienceStored += int(reward)

                    # Add to used list for removing from starting list
                    usedMaterials.append(resource)

                guildList[4] = materialList[0] = usedMaterials[0]
                guildList[3] = materialList[1] = usedMaterials[1]
                guildList[2] = materialList[2] = usedMaterials[2]
                guildList[5] = experienceStored

            saveGuild(guildList)

        else:
            pass
    else:
        pass


def guildUpgrade(coffer, population, levelGuild, itemWood, itemOre, itemMetal):
    if levelGuild == 0:
        print('\n Creating a guild is no small task.')
        time.sleep(1)
        print(' You will be tasked with managing your resources differently.')
        time.sleep(1)
        print(' Do you want to create a guild for the following resources? \n   - 25,000,000 Muns\n  '
              ' - 120,000 wood\n   - 66,000 ore\n   - 29,000 metal')
        confirm = input(' Build for these resources? (Y or N)')

        # Check if yes and if resources are available
        if confirm.upper() == 'Y':
            if coffer >= 25000000 and itemWood >= 120000 and itemOre >= 66000 and itemMetal >= 29000:
                coffer -= 25000000
                itemWood -= 120000
                itemOre -= 66000
                itemMetal -= 29000
                levelGuild += 1
                createGuild()
                return coffer, population, levelGuild, itemWood, itemOre, itemMetal

            else:
                print(' Resources are missing.')
                time.sleep(1)
                return coffer, population, levelGuild, itemWood, itemOre, itemMetal

        else:
            print(' Confirmation not received.')
            time.sleep(1)
            return coffer, population, levelGuild, itemWood, itemOre, itemMetal

    # Allows guild functions if guild is built
    else:
        guild = True

        # Load Guild Info
        guildList = []
        with open(fileGuild, 'r') as file:
            for line in file:
                guildList.append(line)

        guildName = guildList[0].replace('\n', '')
        members = int(guildList[1])
        woodStored = int(guildList[2])
        oreStored = int(guildList[3])
        metalStored = int(guildList[4])
        experienceStored = int(guildList[5])

        resourceList = [coffer, levelGuild, itemWood, itemOre, itemMetal]
        actionList = ['Level Guild', 'Train Members', 'Donate Wood', 'Donate Ore', 'Donate Metal',
                      'Withdraw Exp', 'Return']

        # Line set up for printing
        infoLineZero = ' ║ {:<13} ║  {:<12} ║'
        infoLineOne = ' ║ Wood:{:8} ║ Ore:{:9} ║ Metal:{:7} ║'
        infoLineTwo = ' ║{:>14} ║{:>14} ║{:>14} ║'
        infoLineProgress = '{:<44}'
        infoLineThree = ' ║  [' + infoLineProgress + ']  ║'
        infoLineFour = ' ║ Stored Wood:{:1} ║ Stored Ore:{:2} ║ Stored Metal: ║'
        centered = ' Lv:' + '{}'

        while guild:
            common.clear()
            # Line printing
            percent = int((int(experienceStored) / (levelGuild * 1000)) * 44)
            number = 1
            print(' Welcome to ' + guildName + "'s hall!")
            print(' ╔═══════════════╦═══════════════╗')
            print(' ║ Guild Level:  ║ Guild Members:║')
            print(infoLineZero.format(levelGuild, members))
            print(' ╠═══════════════╬═══════════════╬═══════════════╗')
            print(infoLineOne.format(' ', ' ', ' '))
            print(infoLineTwo.format(common.numConversion(itemWood), common.numConversion(itemOre),
                                     common.numConversion(itemMetal)))
            print(' ╠═══════════════╬═══════════════╬═══════════════╣')
            print(infoLineFour.format(common.numConversion(' '), common.numConversion(' '),
                                      common.numConversion(' ')))
            print(infoLineTwo.format(common.numConversion(woodStored), common.numConversion(oreStored),
                                      common.numConversion(metalStored)))

            # Guild Coffers
            print(' ╠═══════════════╩═══════════════╩═══════════════╩══╗')
            print(' ║                                                  ║')
            print(' ║                   Guild Coffers                  ║')
            print(infoLineThree.format('▓' * percent))
            print(' ║                                                  ║')
            print(' ╠═══╦══════════════════════════════════════════════╣')

            # Print option list
            choiceNum = 1
            for choice in actionList:
                choiceLine = (' ╠(' + str(choiceNum) + ')╣ ' + '{:<44} ║')
                print(choiceLine.format(choice))
                choiceNum += 1

            print(' ╚═══╩══════════════════════════════════════════════╝')

            guildAction = input(' Choose Selection: ')

            if guildAction == '1':

                # Level Up Guild
                levelUp = levelGuild * 300
                if experienceStored >= levelUp:
                    confirm = input(' Confirm guild level up for ' + common.numConversion(levelUp) + ' exp? (Y or N) ')
                    if confirm.upper() == 'Y':
                        experienceStored -= levelUp
                        guildList[5] = experienceStored
                        levelGuild += 1
                        stats.addExpOut(levelUp)
                    else:
                        print(' Confirmation not received.')
                        time.sleep(1)

                else:
                    print(' Need ' + str(levelUp - experienceStored) + ' more exp.')
                    time.sleep(1)

            elif guildAction == '2':
                guildAction = trainMembers(experienceStored, population, members)
                experienceStored = guildList[5] = guildAction[0]
                population = guildAction[1]
                members = guildList[1] = guildAction[2]
                print(population, members)

            elif guildAction == '3':
                guildAction = donate(itemWood, woodStored, 0)
                itemWood = guildAction[0]
                woodStored = guildList[2] = guildAction[1]

            elif guildAction == '4':
                guildAction = donate(itemOre, oreStored, 1)
                itemOre = guildAction[0]
                oreStored = guildList[3] = guildAction[1]

            elif guildAction == '5':
                guildAction = donate(itemMetal, metalStored, 2)
                itemMetal = guildAction[0]
                metalStored = guildList[4] = guildAction[1]

            elif guildAction == '6':
                experienceStored = guildList[5] = withdraw(experienceStored)

            elif guildAction == '7':
                saveGuild(guildList)
                guild = False
                return coffer, population, levelGuild, itemWood, itemOre, itemMetal

            else:
                print(' Invalid choice.')
                time.sleep(1)
