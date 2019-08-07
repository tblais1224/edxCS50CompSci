import cs50
import math


def change():
    changeIn = cs50.get_float("Change owed: ")
    if changeIn <= 0.00:
        changeIn = cs50.get_float("Change owed: ")
    return changeIn


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


def getQuarters(change, count):
    if change > 0.249 and change < 0.25:
        change = round_up(change, 2)
    if change >= 0.25:
        change = change - 0.25
        count = count + 1
        getQuarters(change, count)
    else:
        getDimes(change, count)


def getDimes(change, count):
    if change > 0.099 and change < 0.10:
        change = round_up(change, 2)
    if change >= 0.10:
        change = change - 0.10
        count = count + 1
        getDimes(change, count)
    else:
        getNickles(change, count)


def getNickles(change, count):
    if change > 0.049 and change < 0.05:
        change = round_up(change, 2)
    if change >= 0.05:
        change = change - 0.05
        count = count + 1
        getNickles(change, count)
    else:
        getPennies(change, count)


def getPennies(change, count):
    if change > 0.009 and change < 0.01:
        change = round_up(change, 2)
    if change >= 0.01:
        change = change - 0.01
        count = count + 1
        getPennies(change, count)
    else:
        print(count)


change = change()
getQuarters(change, 0)

