import pygame
from .player import Player
from .maze import Maze
import sys
from .objective import Objective

# Initialize Pygame
pygame.init()

# Constants
HEIGHT = 600
WIDTH = 800
FPS = 60
cell_size = 50

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# Create player
maze = Maze(cell_size, 20, 20)
maze.randomize_maze()
maze.grid[0][0].collidable = False
player = Player(maze.player_start, 5)
objective = Objective(maze.objective_position)
print(maze)
points = 0

# Clock for controlling frame rate
clock = pygame.time.Clock()


def handle_events(): ...


while True:
    handle_events()

    # Update game state
    # Add any game logic updates here

    # Clear the screen

    # Draw everything
    screen.fill((0, 0, 0))
    maze.draw(screen)
    player.draw(screen)
    objective.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
