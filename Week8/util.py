def create_grid(grid):
  rows, cols = (4, 4)
  for i in range(cols):
    col = []
    for j in range(rows):
        col.append(0)
    grid.append(col)
  

def print_grid(grid):
   print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                      for row in grid]))

      


def check_lost(grid):
    import numpy as np
    a = np.array(grid)
    vertical = np.where((a == np.roll(a, 1, 0))[1:-1])
    # print(vertical)  # prints out the coordinate of the of the repeating numbers's
    horizontal = np.where((a == np.roll(a, 1, 1))[:, 1:-1])
    # print(horizontal)  # prints out the coordinate of the of the repeating numbers's

    for row in grid:
        for element in row:
            if element != 0:
                if not any(map(len,vertical)):
                    if not any(map(len, horizontal)):
                        return True
                else:
                    return False
            else:
                    return False
            

def check_won(grid):

    flag = False
    for row in grid:
        for c in row:
            if c >= 32:
                flag = True
                break
    return flag

def copy_grid(grid):
    a =[row[:] for row in grid]
    return a
  
def grid_equal(grid1, grid2):
      if grid1== grid2:
        return True
      else:
        return False