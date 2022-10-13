import os

def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def numConversion(number):
    try:
        value = int(number)
        value = f'{value:,}'
        return value
    except (ValueError):
        return number
