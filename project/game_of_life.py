'''AFS 505 Unit 1 Project --- Game of Life
..module:: Project01
    :platform: Unix, Windows
    :synopsis:  A simulation of cells that can be either ON or OFF and will change
                states each time point depending on the states on their neighbors
                Program accepts runtime and initial cell indexes that are ON
                Reviewed by Samodya Jayasinghe, score = 100

..moduleauthor:: Natalie Sanchez <natalies.sanchez98@gmail.com>

'''
def main():
    '''Runs a simulation of Conway's Game of Life

    Takes the number of generations the simulation will run for
    and the initial ON cells from the command line

    '''
    from sys import argv
    script, runtime, *init_cells = argv

    #Initialize 2D array that contains alive/dead info with given number of rows and columns
    cols = 80   #number of columns
    rows = 30   #number of rows
    cells = []  #2D list of cells
    for y in range(rows):
        cells.append([0]*cols)

    #Turn on initial cells from command line input
    for cell in init_cells:
        #get coordinates from y:x format to [y][x]
        coords = cell.partition(':')    #string describing an ON cell
        y = int(coords[0]) - 1          #row position of ON cell
        x = int(coords[2]) - 1          #column position of ON cell
        #Mark this cell as alive with an 1
        cells[y][x] = 1

    #create a neighbour value for each cell that is equal to the number on ON neighbours
    neighbours = []
    #Start neighbour value at 0
    for y in range(rows):
        neighbours.append([0]*cols)


    #Run the Simulation
    gen = 0     #Start the generation count at 0
    while gen <= int(runtime):

        #Display Grid
        draw_grid(cells)
        print(f"Generation: {gen}")

        #Determine how many neighbours are ON
        neighbours = get_neighbour_values(cells, neighbours)

        #Update cells
        cells = update(cells, neighbours)

        #move to next generation
        gen += 1

    print("\nGoodbye")

##### END OF MAIN #####

def draw_grid(cell_grid):
    '''Prints the 2D list to STDOUT in rows and columns

    uses '-' if the cell is OFF and a 'X' if ON

    :param cell_grid: The list that stores each cell's ON or OFF value
    :type cell_grid: any 2D list with values that can be interpreted as boolean

    '''
    for y in range(len(cell_grid)):
        for x in range(len(cell_grid[y])):
            if cell_grid[y][x]:     #If ON
                print('X', end = '')
            else:                   #If OFF
                print('-', end = '')
        print('')

def get_neighbour_values(cell_info, nvalues):
    '''Determine how many neighbours are ON

    :param cell_info: The list that stores each cell's ON or OFF value
    :type cell_info: 2D list with values 1 for ON and 0 for OFF

    :param nvalues: initialized 2D list of the same size as cell_info
    :type nvalues: 2D list of integers

    :return: 2D list with number of ON neighbours each cell has
    :rtype: 2D list of integers

    '''
    last_row = len(cell_info) - 1       #index of last row of the list
    last_col = len(cell_info[0]) - 1    #index of last column of the list

    #Middle cells
    for y in range(1, last_row):
        for x in range(1, last_col):
            nvalues[y][x] = cell_info[y-1][x-1] + cell_info[y-1][x] + cell_info[y-1][x+1]    #Northern Neighbours
            nvalues[y][x] += cell_info[y][x-1] + cell_info[y][x+1]                           #West and East Neighbours
            nvalues[y][x] += cell_info[y+1][x-1] + cell_info[y+1][x] + cell_info[y+1][x+1]   #Southern Neighbours

    #First row
    for x in range(1, last_col):
        nvalues[0][x] = cell_info[0][x-1] + cell_info[0][x+1]                      #West and East Neighbours
        nvalues[0][x] += cell_info[1][x-1] + cell_info[1][x] + cell_info[1][x+1]   #Southern Neighbours

    #Last row
    for x in range(1, last_col):
        nvalues[last_row][x] = cell_info[last_row-1][x-1] + cell_info[last_row-1][x] + cell_info[last_row-1][x+1]    #Northern Neighbours
        nvalues[last_row][x] += cell_info[last_row][x-1] + cell_info[last_row][x+1]                                  #West and East Neighbours

    #West edge
    for y in range(1, last_row):
        nvalues[y][0] = cell_info[y-1][0] + cell_info[y+1][0]                       #North and South Neighbours
        nvalues[y][0] += cell_info[y-1][1] + cell_info[y][1] + cell_info[y+1][1]    #Eastern Neighbours

    #East edge
    for y in range(1, last_row):
        nvalues[y][last_col] += cell_info[y-1][last_col-1] + cell_info[y][last_col-1] + cell_info[y+1][last_col-1]    #Western Neighbours
        nvalues[y][last_col] = cell_info[y-1][last_col] + cell_info[y+1][last_col]                                    #North and South Neighbours

    #Corners
    nvalues[0][0] = cell_info[0][1] + cell_info[1][0] + cell_info[1][1]                                    #Northwest corner
    nvalues[0][last_col] = cell_info[0][last_col-1] + cell_info[1][last_col-1] + cell_info[1][last_col]    #Northeast corner
    nvalues[last_row][0] = cell_info[last_row-1][0] + cell_info[last_row-1][1] + cell_info[last_row][1]    #Southwest corner
    nvalues[last_row][last_col] = cell_info[last_row-1][last_col-1] + cell_info[last_row-1][last_col] + cell_info[last_row][last_col-1] #Southeast corner

    return nvalues

def update(cell_info, nvalues):
    '''Update cells to follow neighbor Rules for next Generation

    Rules:  a.	Any ON cell with fewer than two live neighbors is turned OFF.
            b.	Any ON cell with two or three “on” neighbors remains ON.
            c.	Any ON cell with more than three “on” neighbors is turned OFF.
            d.	Any OFF cell with exactly three live neighbors is turned ON.

    :param cell_info: The list that stores each cell's ON or OFF value for current genreation
    :type cell_info: 2D list with values 1 for ON and 0 for OFF

    :param nvalues: 2D list with number of ON neighbours each cell has
    :type nvalues: 2D list of integers (same size as cell_info)

    :return: 2D list with values 1 for ON and 0 for OFF for next generation
    :rtype: 2D list of 1's and 0's

    '''
    for y in range(len(cell_info)):
        for x in range(len(cell_info[y])):
            if cell_info[y][x]:
                if nvalues[y][x] < 2 or nvalues[y][x] > 3:
                    cell_info[y][x] = 0
                     #Any ON cell with fewer than 2 or greater than 3 ON neighbours gets turned OFF
            else:
                if nvalues[y][x] == 3:
                    cell_info[y][x] = 1
                    #Any OFF cell wit exactly 3 ON neighbours is turned ON
    return cell_info

##### END OF FUNCTION DEFINITIONS ####

if __name__ == "__main__":
    main()
