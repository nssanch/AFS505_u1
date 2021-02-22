'''AFS 505 Unit 1 Project --- Game of Life
..module:: Project01
    :platform: Unix, Windows
    :synopsis:  A simulation of cells that can be either ON or OFF and will change
                states each time point depending on the states on their neighbors

                Program accepts runtime and initial cell indexes that are ON

..moduleauthor:: Natalie Sanchez natalies.sanchez98@gmail.com

'''
import pygame

def main():
    '''Runs a simulat ion of Conway's Game of Life

    Takes the number of generations the simulation will run for
    and the initial ON cells from the command line

    '''
    from sys import argv
    script, runtime, *init_cells = argv

    #Initialize 2D arrays that contains alive/dead info with given number of rows and columns
    cols = 80
    rows = 30
    cells = []
    old_cells = []
    neighbours = []
    for y in range(rows):
        cells.append([0]*cols)
        old_cells.append([0]*cols)
        neighbours.append([0]*cols)

    #Turn on initial cells from command line input
    for cell in init_cells:
        #get coordinates from y:x format to [y][x]
        coords = cell.partition(':')
        y = int(coords[0]) - 1
        x = int(coords[2]) - 1
        #Mark this cell as alive with an 1
        cells[y][x] = 1

    #Things you need to do in order to have pretty graphics
    pygame.init()

    #Set cell sizes and positions and initialie screen
    cell_size = cell_x, cell_y = 10, 10
    pt = 2
    ulx = 200
    uly = 100
    canvas = pygame.display.set_mode((1600,900))
    canvas.fill((0, 0, 0))

    #Make a list of rects that represent each cell
    rects = []
    for y in range(rows):
        new_rects = []
        for x in range(cols):
            new_rects.append(((ulx+(cell_x+pt)*x,uly+(cell_y+pt)*y), cell_size))
        rects.append(new_rects)
    #Make each cell teal
    for y in range(rows):
        for x in range(cols):
            pygame.draw.rect(canvas, (0, 255, 160), rects[y][x])

    #Make the generation counter display
    words = pygame.font.Font('freesansbold.ttf', 14).render('Generation: ', True, (240, 240, 240))
    words_rect = words.get_rect(center = (ulx+50, uly+(cell_y+pt)*(rows+1)))
    canvas.blit(words, words_rect)

    pygame.display.flip()

    #Run the Simulation
    #Set the generation count to 0

    gen = 0
    while gen <= int(runtime):

        #Display Grid
        draw_grid(cells, old_cells, canvas, rects, gen)
        counter = pygame.font.Font('freesansbold.ttf', 14).render(str(gen), True, (240, 240, 240))
        counter_rect = counter.get_rect(center = (ulx+words_rect.width+10, uly+(cell_y+pt)*(rows+1)))
        pygame.draw.rect(canvas, (0,0,0),counter_rect)
        canvas.blit(counter, counter_rect)
        pygame.display.update(counter_rect)
        print_grid(cells)
        print(f"Generation: {gen}")

        #Determine how many neighbours are ON
        neighbours = get_neighbour_values(cells, neighbours)

        #Update cells
        for y in range(rows):
            for x in range(cols):
                old_cells[y][x] = cells[y][x]
        cells = update(cells, neighbours)

        #move to next generation
        gen += 1
        pygame.time.wait(200)

    pygame.time.wait(2000)
    print("\nGoodbye")

##### END OF MAIN #####

def draw_grid(cell_grid, last_g, screen, surrects, g):
    '''Draws a pretty picture representing the ON and OFF cells

    :param cell_grid: The list that stores each cell's ON or OFF value
    :type cell_grid: any 2D list with values that can be interpreted as boolean

    :param old_cells: The list that stores each cell's ON or OFF value for the previous generation
    :type old_cells: any 2D list with values that can be interpreted as boolean

    '''
    updated_rects = []
    for y in range(len(cell_grid)):
        for x in range(len(cell_grid[y])):
            if cell_grid[y][x] == last_g[y][x]:
                pass
            elif cell_grid[y][x] == 1:
                pygame.draw.rect(screen, (0, 0, 255), surrects[y][x])
                updated_rects.append(surrects[y][x])
            elif cell_grid[y][x] == 0:
                pygame.draw.rect(screen, (0, 255, 0), surrects[y][x])
                updated_rects.append(surrects[y][x])
    pygame.display.update(updated_rects)



def print_grid(cell_grid):
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
    last_row = len(cell_info) - 1
    last_col = len(cell_info[0]) - 1

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
            else:
                if nvalues[y][x] == 3:
                    cell_info[y][x] = 1

    return cell_info

##### END OF FUNCTION DEFINITIONS ####

if __name__ == "__main__":
    main()
