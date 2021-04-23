def memoisation(func):
    cache = {}
    def inner(n,m,a,b):
        key = str(n) + "," + str(m) + "," + str(a) + "," + str(b)
        if key not in cache:
            cache[key] = func(n,m,a,b)
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

@memoisation
def minimumPossibleMove(srcRow, srcCol, destRow, destCol):
    if srcRow < 1 or srcRow > 8: return 0
    if srcCol < 1 or srcCol > 8: return 0
    # if [destRow, destCol] not in moveOfNewCharacter(srcRow, srcCol): return 0
    if [destRow, destCol] in moveOfNewCharacter(srcRow, srcCol): return 1
    # count = 0
    for pos in moveOfNewCharacter(srcRow, srcCol):
        temp = minimumPossibleMove(srcRow + 1, srcCol, destRow, destCol) \
               + minimumPossibleMove(srcRow, srcCol + 1, destRow, destCol) \
               + minimumPossibleMove(srcRow - 1, srcCol, destRow, destCol) \
               + minimumPossibleMove(srcRow, srcCol - 1, destRow, destCol) \
               + minimumPossibleMove(srcRow + 1, srcCol + 1, destRow, destCol) \
               + minimumPossibleMove(srcRow - 1, srcCol - 1, destRow, destCol)
        print(temp)

if __name__ == '__main__':
    print(minimumPossibleMove(5,5,8,8))
