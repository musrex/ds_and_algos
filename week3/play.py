import random

# the size of the 2d array
grid_size = 10
# this variable determines the number of ships to be placed on the board
num_of_ships = 5
# this is the array declaration
grid = [ ['']*grid_size for i in range(grid_size) ]
# we use this list to verify that ships aren't being placed in the same location
ships = []
# we use this list to track the number of sunken ships
sunk = []
# we use this list to tracl the number of empty spaces
water = []

def drawBoard(myBoard):
    '''Summary of Function drawBoard()
    This function takes in a board as a parameter and draws it out.
    The board is generated by the SETUPBOARD() function.

    Parameters
    arg1(2array): a grid that will house the pieces for the game.
    Use the variable GRID_SIZE to set the size of the game board.

    Returns:
    str: A string of the gameboard, with pieces in place.
    '''
    i = j = 0
    # this print statement, repeated throughout this function, creates our horizontal borders
    # this print statement gives us the top row, horizontal coordinates
    print("0","1","2","3","4","5","6","7","8","9",)
    for i in range(grid_size):
        # this print statement gives the left most row, vertical coordinates
        print("" + str(i) , end="")
        for j in range(grid_size):
            # this print statement "draws" out the ships and spaces on our board
            print("" + myBoard[i][j] , end = "")
        print()
    return(myBoard)

def setupBoard():
    '''Summary of Function setupBoard()
    This function takes in no arguments and sets up the board.
    This function places the empty spaces and the ships in the
    appropiate spaces on the board, and keeps track of them for later use.
    '''
    i = j = 0
    while i < grid_size:
        while j < grid_size:
            # store the string "i, j" into the array
            grid[i][j] = " . "
            # we append the empty spaces to a list for tracking and later use
            water.append(grid[i][j])
            j += 1
        j = 0
        i += 1
    x = 0
    while x < num_of_ships: 
        randomRow = random.randint(0, grid_size - 1)
        randomCol = random.randint(0, grid_size - 1)    
        if grid[randomRow][randomCol] not in ships:
            grid[randomRow][randomCol] = " S "
            # we append the ships to a list for tracking and later use
            ships.append(grid[randomRow][randomCol])
            x += 1

drawBoard(grid)
