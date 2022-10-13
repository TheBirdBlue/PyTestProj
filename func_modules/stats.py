import common

fileLocation = 'save/saveStats.txt'

'''File Formatted as;
    LINE 1[0] > Money In
    LINE 2[1] > Experience In
    LINE 3[2] > Money Out
    LINE 4[3] > Experience Out
    LINE 5[4] > Wins
    LINE 6[5] > Losses'''

def addHuntWinnings(money, experience, win):
    importStats = []
    workingStats = []
    with open(fileLocation, 'r') as doc:
        for line in doc:
            importStats.append(line)

        for convert in importStats:
            workingStats.append(int(convert))

        workingStats[0] += money
        workingStats[1] += experience
        workingStats[4] += win

    with open(fileLocation, 'w') as doc:
        for stat in workingStats:
            str(line).rstrip('\n')
            doc.write(str(stat))
            doc.write('\n')

def addLose(lose):
    importStats = []
    workingStats = []
    with open(fileLocation, 'r') as doc:
        for line in doc:
            importStats.append(line)

        for convert in importStats:
            workingStats.append(int(convert))

        workingStats[5] += lose

    with open(fileLocation, 'w') as doc:
        for stat in workingStats:
            str(line).rstrip('\n')
            doc.write(str(stat))
            doc.write('\n')

def addExpOut(experience):
    importStats = []
    workingStats = []
    with open(fileLocation, 'r') as doc:
        for line in doc:
            importStats.append(line)

        for convert in importStats:
            workingStats.append(int(convert))

        workingStats[3] += experience

    with open(fileLocation, 'w') as doc:
        for stat in workingStats:
            str(line).rstrip('\n')
            doc.write(str(stat))
            doc.write('\n')

def addMoneyTransaction(money):
    importStats = []
    workingStats = []
    with open(fileLocation, 'r') as doc:
        for line in doc:
            importStats.append(line)

        for convert in importStats:
            workingStats.append(int(convert))

        if money > 0:
            workingStats[0] += money

        else:
            workingStats[2] -= money

    with open(fileLocation, 'w') as doc:
        for stat in workingStats:
            str(line).rstrip('\n')
            doc.write(str(stat))
            doc.write('\n')

def showStats():
    common.clear()
    showStats = []
    infoList = ['Muns Earned', 'Exp Earned', 'Muns Spent', 'Exp Used', 'Good Hunts', 'Bad Hunts']
    with open(fileLocation, 'r') as doc:
        for line in doc:
            str(line).rstrip('\n')
            showStats.append(line)

        workingDict = dict(zip(infoList, showStats))

        print(' ╔════════════════════╡')

        # GUI for Choices and Actions
        for key, value in workingDict.items():
            value = int(value)
            value = f'{value:,}'
            choiceLine = " ╟{:<20}" + "|\n" + " ╟{:>20}" + "|"
            print(choiceLine.format(key, value))

        percentLine = (' ╟Win Percent' + '{:>8}%' + '|')
        try:
            percentReturn = int(workingDict['Good Hunts']) / (int(workingDict['Good Hunts'])\
                                                              + int(workingDict['Bad Hunts']))
            percentReturn = int(percentReturn * 100)
        except (ZeroDivisionError):
            percentReturn = 0

        print(percentLine.format(percentReturn))
        print(' ╚════════════════════╧')

        input(' Press [ENTER] to return to main menu. ')
