# Memoization to reduce the time complexity
def memoization(func):
    cache = {}

    def inner(n, m):
        key = str(n) + ',' + str(m)
        if key not in cache:
            cache[key] = func(n, m)
        return cache[key]

    return inner


# Find all the possible routes for one point to the end.
@memoization
def totalPathCount(row, column):
    if row < 0: return 0
    if column < 0: return 0
    if row == 0 and column == 0: return 1
    return totalPathCount(row - 1, column) + totalPathCount(row, column - 1)


# List of the Routes That are Closed, We cannot go through that routes
# closed routes are in the format [[row1,col1],[row2,col2],...]
routeClosed = [[1, 1]]


# function to calculate the total no of possible paths form origin to
# opposite corner when some routes are closed
@memoization
def totalPathCountWithClosedRoutes(row, column):
    if row < 0: return 0
    if column < 0: return 0
    if [row, column] in routeClosed: return 0
    if row == 0 and column == 0: return 1
    return totalPathCountWithClosedRoutes(row - 1, column) + totalPathCountWithClosedRoutes(row, column - 1)


# if we are allowed to move diagonally
@memoization
def totalPathCountDiagonally(row, column):
    if row < 0 : return 0
    if column < 0 : return 0
    # To eliminate Closed Route paths uncomment the line just below
    if [row, column] in routeClosed: return 0
    if row == 0 and column == 0: return 1
    return totalPathCountDiagonally(row - 1, column) + totalPathCountDiagonally(row,column - 1) + totalPathCountDiagonally(row - 1, column - 1)

# Diver Function for testing Purpose
if __name__ == '__main__':
    print(totalPathCountDiagonally(2, 2))
