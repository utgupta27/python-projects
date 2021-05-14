def memoization(func):
    cache = {}

    def inner(n, m):
        key = str(n) + "," + str(m)
        if key not in cache:
            cache[key] = func(n, m)
        return cache[key]

    return inner

def checkBorderConstrains(temp):
    for i in range(2):
        for item in temp:
            if item[0] < 1 or item[1] < 1:
                temp.remove(item)
    for i in range(3):
        for item in temp:
            if item[0] > 8 or item[1] > 8:
                temp.remove(item)
    return temp

def possibleKnightMoves(row, col):
    temp = [[row - 1, col - 2],
            [row + 1, col - 2],
            [row + 2, col - 1],
            [row + 2, col + 1],
            [row + 1, col + 2],
            [row - 1, col + 2],
            [row - 2, col + 1],
            [row - 2, col - 1], ]
    return checkBorderConstrains(temp)

def possibleKingsMoves(row, col):
    temp = [[row - 1, col - 1],
            [row, col - 1],
            [row + 1, col - 1],
            [row + 1, col + 0],
            [row + 1, col + 1],
            [row, col + 1],
            [row - 1, col + 1],
            [row - 1, col], ]
    return checkBorderConstrains(temp)

def moveOfNewCharacter(row, col):
    return possibleKingsMoves(row, col) + possibleKnightMoves(row, col)


def possibleMoves(row,col):
    temp = [[row - 1, col - 2],
            [row + 1, col - 2],
            [row + 2, col - 1],
            [row + 2, col + 1],
            [row + 1, col + 2],
            [row - 1, col + 2],
            [row - 2, col + 1],
            [row - 2, col - 1],
            [row - 1, col - 1],
            [row, col - 1],
            [row + 1, col - 1],
            [row + 1, col + 0],
            [row + 1, col + 1],
            [row, col + 1],
            [row - 1, col + 1],
            [row - 1, col]]
    for i in range(2):
        for item in temp:
            if item[0] < 1 or item[1] < 1:
                temp.remove(item)
    for i in range(3):
        for item in temp:
            if item[0] > 8 or item[1] > 8:
                temp.remove(item)
    return temp






destRow = 6
destCol = 6


# @memoization
def minimumPossibleMove(srcRow, srcCol):
    if srcRow < 1 or srcRow > 8: return 0
    if srcCol < 1 or srcCol > 8: return 0
    # if [destRow, destCol] not in possibleMoves(srcRow, srcCol): return 0
    if [destRow, destCol] in possibleMoves(srcRow, srcCol):
        return 1

    return minimumPossibleMove(srcRow + 1, srcCol) \
           + minimumPossibleMove(srcRow, srcCol + 1) \
           + minimumPossibleMove(srcRow + 1, srcCol + 1) \

if __name__ == '__main__':
    print(minimumPossibleMove(8,8))
    # for i in range(1,9):
    #     for j in range(1, 9):
    #         print(possibleMoves(i, j))