import random


def randomString(long, symbol):
    symbolList = []
    for index in range(1, long + 1):
        symbolList.append(random.choice(symbol))
    return ''.join(symbolList)

