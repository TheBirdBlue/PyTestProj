#!/usr/bin/python

import os
import sys
import time

# Import Folder
sys.path.insert(0, './func_modules')

import hunt
import levelup
import shop
import town
import stats
import saveload
import common

# Import Folder
sys.path.insert(0, './func_modules')

run = True
fileLocationUser = 'save/saveOverview.txt'
fileLocationStats = 'save/saveStats.txt'
fileLocationResources = 'save/saveResources.txt'
list = ('Hunt', 'Level Up', 'Shop', 'Visit Town', 'Stats', 'Save & Quit')


def main():

    # Set Character values before loading
    charName = ''
    charLvl = 0
    charExp = 0
    charMun = 0
    charAtk = 0
    charDef = 0
    charSpe = 0

    loadList = [charName, charLvl, charExp, charMun, charAtk, charDef, charSpe]

    # Load or create save files
    if os.path.exists(fileLocationUser) == False:
        workingOverview = saveload.createOver(fileLocationUser, charName, charLvl, charExp, charMun, charAtk, charDef, charSpe)
        saveload.createStats(fileLocationStats)
        saveload.createResources(fileLocationResources)
        common.clear()
    elif os.stat(fileLocationUser).st_size == 0:
        workingOverview = saveload.createOver(fileLocationUser, charName, charLvl, charExp, charMun, charAtk, charDef, charSpe)
        common.clear()
    else:
        workingOverview = saveload.loadOver(fileLocationUser, loadList)
        common.clear()

    # Change values to created and loaded values
    charName = workingOverview[0]
    charLvl = workingOverview[1]
    charExp = workingOverview[2]
    charMun = workingOverview[3]
    charAtk = workingOverview[4]
    charDef = workingOverview[5]
    charSpe = workingOverview[6]

    # Main running loop
    while run == True:

        common.clear()
        workingFormat = []
        point = 0

        # Run values through formatting function
        for value in workingOverview:
            if point == 0:
                point += 1
            else:
                workingFormat.append(common.numConversion(value))
                point += 1

        # Change values to created and loaded values
        charName = workingOverview[0]
        charLvl = int(workingOverview[1])
        charExp = int(workingOverview[2])
        charMun = int(workingOverview[3])
        charAtk = int(workingOverview[4])
        charDef = int(workingOverview[5])
        charSpe = int(workingOverview[6])

        # Set formatted numbers for display
        charLvlFormat = workingFormat[0]
        charExpFormat = workingFormat[1]
        charMunFormat = workingFormat[2]
        charAtkFormat = workingFormat[3]
        charDefFormat = workingFormat[4]
        charSpeFormat = workingFormat[5]

        # GUI for Over Stats
        number = 1
        print(' Welcome ' + charName)
        print(' ╔═════════════════════════════╡')
        infoLine = ' ╟Lvl:{:>24} ╡\n ╟Exp:{:>24} ╡\n ╟Mun:{:>24} ╡'
        print(infoLine.format(charLvlFormat, charExpFormat, charMunFormat))

        # GUI for Player Stats
        print(' ╠═════════════════════════════╡')
        statHeader = ' ╠     ATK ╬     DEF ╬     SPE ╡'
        print(statHeader)
        statLine = ' ╠{:>8} ╬{:>8} ╬{:>8} ╡'
        print(statLine.format(charAtkFormat, charDefFormat, charSpeFormat))

        # GUI for Choices and Actions
        print(' ╠═══╦═════════════════════════╡')
        for choice in list:
            choiceLine = ' ╟(' + str(number) + ")╟ " + '{:<24}' + "|"
            print(choiceLine.format(choice))
            number += 1
        print(' ╚═══╩═════════════════════════╧')

        # Option select and check
        waitforinput = input(' Choose Selection: ')

        if waitforinput == '1':
            workingOverview = hunt.huntFunction(workingOverview)
            saveload.saveOver(fileLocationUser, workingOverview)

        elif waitforinput == '2':
            workingOverview = levelup.levelup(workingOverview)
            saveload.saveOver(fileLocationUser, workingOverview)

        elif waitforinput == '3':
            workingOverview = shop.specialShop(workingOverview)
            saveload.saveOver(fileLocationUser, workingOverview)

        elif waitforinput == '4':
            if charLvl >= 1000:
                munChange = town.townFunction(charMun)
                workingOverview = saveload.loadOver(fileLocationUser, loadList)
                workingOverview[3] = munChange
                saveload.saveOver(fileLocationUser, workingOverview)
            else:
                print(' Need to be level 1,000 to visit the town.')
                time.sleep(1)

        elif waitforinput == '5':
            stats.showStats()

        elif waitforinput == '6':
            saveload.saveOver(fileLocationUser, workingOverview)
            confirm = input(' Continue playing? (Y or N)')
            if confirm.upper() == 'N':
                os._exit()
            else:
                workingOverview = saveload.loadOver(fileLocationUser, workingOverview)
        else:
            print(' Invalid Choice.')
            time.sleep(1)

# Run the whole thing
main()
