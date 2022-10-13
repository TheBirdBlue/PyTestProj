def createOver(file, charName, charLvl, charExp, charMun, charAtk, charDef, charSpe):
    loadOrder = ['', 1, 0, 0, 1, 1, 1]
    name = input(' What is your name? ')
    loadOrder[0] = name
    with open(file, 'a+') as save:
        save.write(name)
        save.write('\n')

        # Overworld Info
        save.write(str(loadOrder[1]) + '\n')
        save.write(str(loadOrder[2]) + '\n')
        save.write(str(loadOrder[3]) + '\n')

        # Stat Info
        save.write(str(loadOrder[4]) + '\n')
        save.write(str(loadOrder[5]) + '\n')
        save.write(str(loadOrder[6]) + '\n')

    return loadOrder

def createStats(file):
    loadOrder = [0, 0, 0, 0, 0, 0]
    with open(file, 'a+') as save:

        # Set all as 0 on new save
        save.write(str(loadOrder[0]) + '\n')
        save.write(str(loadOrder[1]) + '\n')
        save.write(str(loadOrder[2]) + '\n')
        save.write(str(loadOrder[3]) + '\n')
        save.write(str(loadOrder[4]) + '\n')
        save.write(str(loadOrder[5]) + '\n')

        return file

def createResources(file):
    loadOrder = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    with open(file, 'a+') as save:

        # Set all as 0 on new save
        save.write(str(loadOrder[0]) + '\n')
        save.write(str(loadOrder[1]) + '\n')
        save.write(str(loadOrder[2]) + '\n')
        save.write(str(loadOrder[3]) + '\n')
        save.write(str(loadOrder[4]) + '\n')
        save.write(str(loadOrder[5]) + '\n')
        save.write(str(loadOrder[6]) + '\n')
        save.write(str(loadOrder[7]) + '\n')
        save.write(str(loadOrder[8]) + '\n')
        save.write(str(loadOrder[9]) + '\n')
        save.write(str(loadOrder[10]) + '\n')

        return file

def loadOver(file, loadList):
    loadOrder = []
    with open(file, 'r') as save:
        for line in save:
            line = line.replace('\n', '')
            loadOrder.append(line)

    return loadOrder

def saveOver(file, charList):
    saveOrder = [charList[0], charList[1], charList[2], charList[3], charList[4], charList[5], charList[6]]
    with open(file, 'w') as save:
        for line in saveOrder:
            str(line).rstrip('\n')
            save.write(str(line))
            save.write('\n')

