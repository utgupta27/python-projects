# A separate function to optimise the solution using function memoisation
# by passing the whole function to this func: "memoisation()" and storing
# the previously calculated values.
def memoization(func):
    cache = {}

    def inner(n, m):
        key = str(n) + "," + str(m)
        if key not in cache:
            cache[key] = func(n, m)
        return cache[key]

    return inner


# Some Unnecessary functions that lead to the solution of the problem

# This function is used to check and eliminate the index that are out of the scope
# of the chess coordinates
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

# Below function returns all the possible moves of a Knight in chess
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

# Below function returns all the possible moves of a King in chess
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

# This function returns all the possible moves of a customised character(knight + King)
def moveOfNewCharacter(row, col):
    return possibleKingsMoves(row, col) + possibleKnightMoves(row, col)



# The func: "possibleMoves(row,col)" combines the move of the Knight and king
# and returns the set of all possible coordinates form a specific given point.
# [[3, 2], [2, 3], [0, 0], [2, 1], [2, 2], [1, 2]]
# [[3, 1], [3, 3], [2, 4], [0, 1], [1, 1], [2, 1], [2, 2], [2, 3], [1, 3]]
# [[2, 1], [3, 2], [3, 4], [2, 5], [0, 2], [1, 2], [2, 2], [2, 3], [2, 4], [1, 4]]
# [[2, 2], [3, 3], [3, 5], [2, 6], [0, 3], [1, 3], [2, 3], [2, 4], [2, 5], [1, 5]]
# [[2, 3], [3, 4], [3, 6], [2, 7], [0, 4], [1, 4], [2, 4], [2, 5], [2, 6], [1, 6]]
# [[2, 4], [3, 5], [3, 7], [2, 8], [0, 5], [1, 5], [2, 5], [2, 6], [2, 7], [1, 7]]
# [[2, 5], [3, 6], [3, 8], [0, 6], [1, 6], [2, 6], [2, 7], [2, 8], [1, 8]]
# [[2, 6], [3, 7], [0, 7], [1, 7], [2, 7], [2, 8]]
# [[4, 2], [3, 3], [1, 3], [2, 0], [3, 1], [3, 2], [2, 2], [1, 2], [1, 1]]
# [[4, 1], [4, 3], [3, 4], [1, 4], [1, 1], [2, 1], [3, 1], [3, 2], [3, 3], [2, 3], [1, 3], [1, 2]]
# [[1, 1], [3, 1], [4, 2], [4, 4], [3, 5], [1, 5], [1, 2], [2, 2], [3, 2], [3, 3], [3, 4], [2, 4], [1, 4], [1, 3]]
# [[1, 2], [3, 2], [4, 3], [4, 5], [3, 6], [1, 6], [1, 3], [2, 3], [3, 3], [3, 4], [3, 5], [2, 5], [1, 5], [1, 4]]
# [[1, 3], [3, 3], [4, 4], [4, 6], [3, 7], [1, 7], [1, 4], [2, 4], [3, 4], [3, 5], [3, 6], [2, 6], [1, 6], [1, 5]]
# [[1, 4], [3, 4], [4, 5], [4, 7], [3, 8], [1, 8], [1, 5], [2, 5], [3, 5], [3, 6], [3, 7], [2, 7], [1, 7], [1, 6]]
# [[1, 5], [3, 5], [4, 6], [4, 8], [1, 6], [2, 6], [3, 6], [3, 7], [3, 8], [2, 8], [1, 8], [1, 7]]
# [[1, 6], [3, 6], [4, 7], [1, 7], [2, 7], [3, 7], [3, 8], [1, 8]]
# [[5, 2], [4, 3], [2, 3], [1, 2], [4, 0], [4, 1], [4, 2], [3, 2], [2, 2], [2, 1]]
# [[5, 1], [5, 3], [4, 4], [2, 4], [1, 3], [1, 1], [2, 1], [3, 1], [4, 1], [4, 2], [4, 3], [3, 3], [2, 3], [2, 2]]
# [[2, 1], [4, 1], [5, 2], [5, 4], [4, 5], [2, 5], [1, 4], [1, 2], [2, 2], [3, 2], [4, 2], [4, 3], [4, 4], [3, 4], [2, 4], [2, 3]]
# [[2, 2], [4, 2], [5, 3], [5, 5], [4, 6], [2, 6], [1, 5], [1, 3], [2, 3], [3, 3], [4, 3], [4, 4], [4, 5], [3, 5], [2, 5], [2, 4]]
# [[2, 3], [4, 3], [5, 4], [5, 6], [4, 7], [2, 7], [1, 6], [1, 4], [2, 4], [3, 4], [4, 4], [4, 5], [4, 6], [3, 6], [2, 6], [2, 5]]
# [[2, 4], [4, 4], [5, 5], [5, 7], [4, 8], [2, 8], [1, 7], [1, 5], [2, 5], [3, 5], [4, 5], [4, 6], [4, 7], [3, 7], [2, 7], [2, 6]]
# [[2, 5], [4, 5], [5, 6], [5, 8], [1, 8], [1, 6], [2, 6], [3, 6], [4, 6], [4, 7], [4, 8], [3, 8], [2, 8], [2, 7]]
# [[2, 6], [4, 6], [5, 7], [1, 7], [2, 7], [3, 7], [4, 7], [4, 8], [2, 8]]
# [[6, 2], [5, 3], [3, 3], [2, 2], [5, 0], [5, 1], [5, 2], [4, 2], [3, 2], [3, 1]]
# [[6, 1], [6, 3], [5, 4], [3, 4], [2, 3], [2, 1], [3, 1], [4, 1], [5, 1], [5, 2], [5, 3], [4, 3], [3, 3], [3, 2]]
# [[3, 1], [5, 1], [6, 2], [6, 4], [5, 5], [3, 5], [2, 4], [2, 2], [3, 2], [4, 2], [5, 2], [5, 3], [5, 4], [4, 4], [3, 4], [3, 3]]
# [[3, 2], [5, 2], [6, 3], [6, 5], [5, 6], [3, 6], [2, 5], [2, 3], [3, 3], [4, 3], [5, 3], [5, 4], [5, 5], [4, 5], [3, 5], [3, 4]]
# [[3, 3], [5, 3], [6, 4], [6, 6], [5, 7], [3, 7], [2, 6], [2, 4], [3, 4], [4, 4], [5, 4], [5, 5], [5, 6], [4, 6], [3, 6], [3, 5]]
# [[3, 4], [5, 4], [6, 5], [6, 7], [5, 8], [3, 8], [2, 7], [2, 5], [3, 5], [4, 5], [5, 5], [5, 6], [5, 7], [4, 7], [3, 7], [3, 6]]
# [[3, 5], [5, 5], [6, 6], [6, 8], [2, 8], [2, 6], [3, 6], [4, 6], [5, 6], [5, 7], [5, 8], [4, 8], [3, 8], [3, 7]]
# [[3, 6], [5, 6], [6, 7], [2, 7], [3, 7], [4, 7], [5, 7], [5, 8], [3, 8]]
# [[7, 2], [6, 3], [4, 3], [3, 2], [6, 0], [6, 1], [6, 2], [5, 2], [4, 2], [4, 1]]
# [[7, 1], [7, 3], [6, 4], [4, 4], [3, 3], [3, 1], [4, 1], [5, 1], [6, 1], [6, 2], [6, 3], [5, 3], [4, 3], [4, 2]]
# [[4, 1], [6, 1], [7, 2], [7, 4], [6, 5], [4, 5], [3, 4], [3, 2], [4, 2], [5, 2], [6, 2], [6, 3], [6, 4], [5, 4], [4, 4], [4, 3]]
# [[4, 2], [6, 2], [7, 3], [7, 5], [6, 6], [4, 6], [3, 5], [3, 3], [4, 3], [5, 3], [6, 3], [6, 4], [6, 5], [5, 5], [4, 5], [4, 4]]
# [[4, 3], [6, 3], [7, 4], [7, 6], [6, 7], [4, 7], [3, 6], [3, 4], [4, 4], [5, 4], [6, 4], [6, 5], [6, 6], [5, 6], [4, 6], [4, 5]]
# [[4, 4], [6, 4], [7, 5], [7, 7], [6, 8], [4, 8], [3, 7], [3, 5], [4, 5], [5, 5], [6, 5], [6, 6], [6, 7], [5, 7], [4, 7], [4, 6]]
# [[4, 5], [6, 5], [7, 6], [7, 8], [3, 8], [3, 6], [4, 6], [5, 6], [6, 6], [6, 7], [6, 8], [5, 8], [4, 8], [4, 7]]
# [[4, 6], [6, 6], [7, 7], [3, 7], [4, 7], [5, 7], [6, 7], [6, 8], [4, 8]]
# [[8, 2], [7, 3], [5, 3], [4, 2], [7, 0], [7, 1], [7, 2], [6, 2], [5, 2], [5, 1]]
# [[8, 1], [8, 3], [7, 4], [5, 4], [4, 3], [4, 1], [5, 1], [6, 1], [7, 1], [7, 2], [7, 3], [6, 3], [5, 3], [5, 2]]
# [[5, 1], [7, 1], [8, 2], [8, 4], [7, 5], [5, 5], [4, 4], [4, 2], [5, 2], [6, 2], [7, 2], [7, 3], [7, 4], [6, 4], [5, 4], [5, 3]]
# [[5, 2], [7, 2], [8, 3], [8, 5], [7, 6], [5, 6], [4, 5], [4, 3], [5, 3], [6, 3], [7, 3], [7, 4], [7, 5], [6, 5], [5, 5], [5, 4]]
# [[5, 3], [7, 3], [8, 4], [8, 6], [7, 7], [5, 7], [4, 6], [4, 4], [5, 4], [6, 4], [7, 4], [7, 5], [7, 6], [6, 6], [5, 6], [5, 5]]
# [[5, 4], [7, 4], [8, 5], [8, 7], [7, 8], [5, 8], [4, 7], [4, 5], [5, 5], [6, 5], [7, 5], [7, 6], [7, 7], [6, 7], [5, 7], [5, 6]]
# [[5, 5], [7, 5], [8, 6], [8, 8], [4, 8], [4, 6], [5, 6], [6, 6], [7, 6], [7, 7], [7, 8], [6, 8], [5, 8], [5, 7]]
# [[5, 6], [7, 6], [8, 7], [4, 7], [5, 7], [6, 7], [7, 7], [7, 8], [5, 8]]
# [[8, 3], [6, 3], [5, 2], [8, 0], [8, 1], [8, 2], [7, 2], [6, 2], [6, 1]]
# [[8, 4], [6, 4], [5, 3], [5, 1], [6, 1], [7, 1], [8, 1], [8, 2], [8, 3], [7, 3], [6, 3], [6, 2]]
# [[6, 1], [8, 1], [8, 5], [6, 5], [5, 4], [5, 2], [6, 2], [7, 2], [8, 2], [8, 3], [8, 4], [7, 4], [6, 4], [6, 3]]
# [[6, 2], [8, 2], [8, 6], [6, 6], [5, 5], [5, 3], [6, 3], [7, 3], [8, 3], [8, 4], [8, 5], [7, 5], [6, 5], [6, 4]]
# [[6, 3], [8, 3], [8, 7], [6, 7], [5, 6], [5, 4], [6, 4], [7, 4], [8, 4], [8, 5], [8, 6], [7, 6], [6, 6], [6, 5]]
# [[6, 4], [8, 4], [8, 8], [6, 8], [5, 7], [5, 5], [6, 5], [7, 5], [8, 5], [8, 6], [8, 7], [7, 7], [6, 7], [6, 6]]
# [[6, 5], [8, 5], [5, 8], [5, 6], [6, 6], [7, 6], [8, 6], [8, 7], [8, 8], [7, 8], [6, 8], [6, 7]]
# [[6, 6], [8, 6], [5, 7], [6, 7], [7, 7], [8, 7], [8, 8], [6, 8]]
# [[7, 3], [6, 2], [8, 2], [7, 2], [7, 1]]
# [[7, 4], [6, 3], [6, 1], [7, 1], [8, 1], [8, 3], [7, 3], [7, 2]]
# [[7, 1], [7, 5], [6, 4], [6, 2], [7, 2], [8, 2], [8, 4], [7, 4], [7, 3]]
# [[7, 2], [7, 6], [6, 5], [6, 3], [7, 3], [8, 3], [8, 5], [7, 5], [7, 4]]
# [[7, 3], [7, 7], [6, 6], [6, 4], [7, 4], [8, 4], [8, 6], [7, 6], [7, 5]]
# [[7, 4], [7, 8], [6, 7], [6, 5], [7, 5], [8, 5], [8, 7], [7, 7], [7, 6]]
# [[7, 5], [6, 8], [6, 6], [7, 6], [8, 6], [8, 8], [7, 8], [7, 7]]
# [[7, 6], [6, 7], [7, 7], [8, 7], [7, 8]]
def possibleMoves(row, col):

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
    # filtering out the contents that are not the possible coordinates of the Chess.
    # here the range of the coordinates is form (1,1) to (8,8) including the points (8,8)
    for i in range(2):
        for item in temp:
            if item[0] < 1 or item[1] < 1:
                temp.remove(item)
    for i in range(3):
        for item in temp:
            if item[0] > 8 or item[1] > 8:
                temp.remove(item)
    # returning the possible moves
    return temp


@memoization
def minimumPossibleMove1(srcRow, srcCol):
    if srcRow < 1 or srcRow > 8: return 0
    if srcCol < 1 or srcCol > 8: return 0
    # if [destRow, destCol] not in possibleMoves(srcRow, srcCol): return 0
    if [destRow, destCol] in possibleMoves(srcRow, srcCol):
        return 1
    return minimumPossibleMove1(srcRow + 1, srcCol) \
               + minimumPossibleMove1(srcRow, srcCol + 1) \
               + minimumPossibleMove1(srcRow + 1, srcCol + 1)

@memoization
def minimumPossibleMove2(srcRow, srcCol):
    if srcRow < 1 or srcRow > 8: return 0
    if srcCol < 1 or srcCol > 8: return 0
    # if [destRow, destCol] not in possibleMoves(srcRow, srcCol): return 0
    if [destRow, destCol] in possibleMoves(srcRow, srcCol):
        return 1
    return minimumPossibleMove2(srcRow + 1, srcCol) \
           + minimumPossibleMove2(srcRow, srcCol - 1) \
           + minimumPossibleMove2(srcRow + 1, srcCol - 1)

@memoization
def minimumPossibleMove3(srcRow, srcCol):
    if srcRow < 1 or srcRow > 8: return 0
    if srcCol < 1 or srcCol > 8: return 0
    # if [destRow, destCol] not in possibleMoves(srcRow, srcCol): return 0
    if [destRow, destCol] in possibleMoves(srcRow, srcCol):
        return 1
    return minimumPossibleMove3(srcRow - 1, srcCol) \
           + minimumPossibleMove3(srcRow, srcCol + 1) \
           + minimumPossibleMove3(srcRow - 1, srcCol + 1)

@memoization
def minimumPossibleMove4(srcRow, srcCol):
    if srcRow < 1 or srcRow > 8: return 0
    if srcCol < 1 or srcCol > 8: return 0
    # if [destRow, destCol] not in possibleMoves(srcRow, srcCol): return 0
    if [destRow, destCol] in possibleMoves(srcRow, srcCol):
        return 1
    return minimumPossibleMove4(srcRow - 1, srcCol) \
           + minimumPossibleMove4(srcRow, srcCol - 1) \
           + minimumPossibleMove4(srcRow - 1, srcCol - 1)

def drive(srcRow, srcCol):
    if srcRow == destRow and srcCol == destCol:
        return 0
    elif srcRow <= destRow and srcCol <= destCol:
        return minimumPossibleMove1(srcRow,srcCol)
    elif srcRow > destRow and srcCol < destCol:
        return minimumPossibleMove3(srcRow, srcCol)
    elif srcRow < destRow and srcCol > destCol:
        return minimumPossibleMove2(srcRow, srcCol)
    elif srcRow > destRow and srcCol > destCol:
        return minimumPossibleMove4(srcRow, srcCol)

if __name__ == '__main__':
    # Destination path(we have to reach this path in minimum number of steps)
    # the range of the coordinates is form (1,1) to (8,8) including the points (8,8)
    destRow = 2
    destCol = 6

    print( "Total possible Moves to reach destination is : "+ str(drive(1, 1)))


    # For printing all the possible combination of moves from each Coordinate
    # for i in range(1,9):
    #     for j in range(1, 9):
    #         print(possibleMoves(i, j))
