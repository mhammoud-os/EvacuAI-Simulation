import pygame
import math
from queue import PriorityQueue

# Pygame setup
pygame.init()

# Define constants
WIDTH = 600  # Width of the window
ROWS = 100  # Increased number of rows for smaller cells
CELL_SIZE = WIDTH // ROWS
TRANSPARENCY = 80

background_image = pygame.image.load("image.png")  # Load the image
background_image = pygame.transform.scale(background_image, (WIDTH, 600))  # Scale to fit the window
#background_image.set_alpha(200)

WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("AI Pathfinding Simulation")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)


# Spot class representing each cell in the grid
class Spot:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = row * CELL_SIZE
        self.y = col * CELL_SIZE
        self.color = WHITE
        self.neighbors = []

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_obstacle(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == BLUE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_obstacle(self):
        self.color = BLACK

    def make_end(self):
        self.color = BLUE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        rect_surface = pygame.Surface((CELL_SIZE,CELL_SIZE))  # Size of the rectangle
        rect_surface.fill(self.color)  # Fill with the desired color
        rect_surface.set_alpha(TRANSPARENCY)
        win.blit(rect_surface, (self.x, self.y))
    #pygame.draw.rect(WIN, self.color, (self.x, self.y, CELL_SIZE, CELL_SIZE))


    def update_neighbors(self, grid):

        self.neighbors = []
        if self.row < ROWS - 1 and not grid[self.row + 1][self.col].is_obstacle():  # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_obstacle():  # UP
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < ROWS - 1 and not grid[self.row][self.col + 1].is_obstacle():  # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_obstacle():  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])


# Heuristic function for A* (Manhattan distance)
def heuristic(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


# Reconstructs the path after A* finds the shortest route
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


# A* algorithm for pathfinding
def a_star(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = heuristic(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False


# Create the grid
def make_grid():
    grid = []
    for i in range(ROWS):
        grid.append([])
        for j in range(ROWS):
            spot = Spot(i, j)
            grid[i].append(spot)
    return grid


# Draw grid lines
def draw_grid(win):
    for i in range(ROWS):
        pygame.draw.line(win, GREY, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE))
        pygame.draw.line(win, GREY, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH))


# Draw the entire window
def draw(win, grid):
    WIN.blit(background_image, (0, 0))
    #win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win)
    pygame.display.update()


# Get the clicked position on the grid
def get_clicked_pos(pos):
    y, x = pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    return row, col


# Main function
def main(win):
    grid = make_grid()
    start = None
    end = None

    run = True
    started = False

    while run:
        draw(win, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # LEFT click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_obstacle()

            elif pygame.mouse.get_pressed()[2]:  # RIGHT click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    a_star(lambda: draw(win, grid), grid, start, end)

    pygame.quit()


main(WIN)
