def push_right(grid):
    for row in grid:
        for i, number in reversed(list(enumerate(row))):
            if number == row[i-1]:
                row[i] = number + row[i-1]
                row[i-1] = 0
        row.sort(key=lambda v: v != 0)
        
    return grid


def push_left(grid):
    for row in grid:
        for i, number in reversed(list(enumerate(row))):
            if number == row[i - 1]:
                row[i] = number + row[i - 1]
                row[i - 1] = 0
        row.sort(key=lambda v: v != 0, reverse=True)

    return grid

   
def push_up(grid):
    myArray = grid
    i = 0
    for j in range(0, 4):
        if myArray[i][j] != 0 or myArray[i + 1][j] != 0 or myArray[i + 2][j] != 0 or myArray[i + 3][j] != 0:
            if myArray[i][j] == 0:
                while myArray[i][j] == 0:
                    myArray[i][j] = myArray[i + 1][j]
                    myArray[i + 1][j] = myArray[i + 2][j]
                    myArray[i + 2][j] = myArray[i + 3][j]
                    myArray[i + 3][j] = 0
            if myArray[i + 1][j] == 0 and (myArray[i + 2][j] != 0 or myArray[i + 3][j] != 0):
                while myArray[i + 1][j] == 0:
                    myArray[i + 1][j] = myArray[i + 2][j]
                    myArray[i + 2][j] = myArray[i + 3][j]
                    myArray[i + 3][j] = 0
            if myArray[i + 2][j] == 0 and (myArray[i + 3][j] != 0):
                while myArray[i + 2][j] == 0:
                    myArray[i + 2][j] = myArray[i + 3][j]
                    myArray[i + 3][j] = 0
    i = 0
    for j in range(0, 4):
        if myArray[i][j] == myArray[i + 1][j]:
            myArray[i][j] = myArray[i][j] + myArray[i + 1][j]
            myArray[i + 1][j] = myArray[i + 2][j]
            myArray[i + 2][j] = myArray[i + 3][j]
            myArray[i + 3][j] = 0
        if myArray[i + 1][j] == myArray[i + 2][j]:
            myArray[i + 1][j] = myArray[i + 1][j] + myArray[i + 2][j]
            myArray[i + 2][j] = myArray[i + 3][j]
            myArray[i + 3][j] = 0
        if myArray[i + 2][j] == myArray[i + 3][j]:
            myArray[i + 2][j] = myArray[i + 2][j] + myArray[i + 3][j]
            myArray[i + 3][j] = 0

    return myArray


def push_down(grid):
    myArray=grid
    i = 0
    for j in range(0, 4):
        if myArray[i][j] != 0 or myArray[i + 1][j] != 0 or myArray[i + 2][j] != 0 or myArray[i + 3][j] != 0:
            if myArray[i + 3][j] == 0:
                while myArray[i + 3][j] == 0:
                    myArray[i + 3][j] = myArray[i + 2][j]
                    myArray[i + 2][j] = myArray[i + 1][j]
                    myArray[i + 1][j] = myArray[i][j]
                    myArray[i][j] = 0
            if myArray[i + 2][j] == 0 and (myArray[i + 1][j] != 0 or myArray[i][j] != 0):
                while myArray[i + 2][j] == 0:
                    myArray[i + 2][j] = myArray[i + 1][j]
                    myArray[i + 1][j] = myArray[i][j]
                    myArray[i][j] = 0

            if myArray[i + 1][j] == 0 and myArray[i][j] != 0:
                while myArray[i + 1][j] == 0:
                    myArray[i + 1][j] = myArray[i][j]
                    myArray[i][j] = 0
    i = 0
    for j in range(0, 4):
        if myArray[i + 3][j] == myArray[i + 2][j]:
            myArray[i + 3][j] = myArray[i + 3][j] + myArray[i + 2][j]
            myArray[i + 2][j] = myArray[i + 1][j]
            myArray[i + 1][j] = myArray[i][j]
            myArray[i][j] = 0
        if myArray[i + 2][j] == myArray[i + 1][j]:
            myArray[i + 2][j] = myArray[i + 2][j] + myArray[i + 1][j]
            myArray[i + 1][j] = myArray[i][j]
            myArray[i][j] = 0
        if myArray[i + 1][j] == myArray[i][j]:
            myArray[i + 1][j] = myArray[i + 1][j] + myArray[i][j]
            myArray[i][j] = 0
    return myArray
