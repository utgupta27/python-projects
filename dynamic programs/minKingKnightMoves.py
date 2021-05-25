from math import sqrt

def minDistance(row,col):
    points = [[row, col],
            [row - 1, col - 2],
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
        for item in points:
            if item[0] < 1 or item[1] < 1:
                points.remove(item)
    for i in range(3):
        for item in points:
            if item[0] > 8 or item[1] > 8:
                points.remove(item)
    for i in range(len(points)):
        points[i].append(int(sqrt((points[i][0]-destRow)*(points[i][0]-destRow) + (points[i][1]-destCol)*(points[i][1]-destCol))))
    min = 100
    for i in range(len(points)):
        if points[i][2] < min:
            min = points[i][2]
    for pt in points:
        if pt[2] == min:
            return pt[0],pt[1],pt[2]


def minimumSteps(row,col,dist=100):
    if dist == 0 : return 0
    count = 0
    row,col,dist = minDistance(row,col)
    print(row,col,dist)
    temp = minimumSteps(row,col,dist)
    count =  count + temp
    return count + 1



if __name__ == '__main__':
    srcRow,srcCol = 1,6
    destRow,destCol  = 8,8
    print("Minimum No. of steps required is: " + str(minimumSteps(srcRow, srcCol)))