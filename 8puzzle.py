import pygame
import random

pygame.init()

# Window settings
WIDTH = 450
HEIGHT = 450
ROWS = 3
TILE_SIZE = WIDTH // ROWS
PADDING = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8 Puzzle Game")

font = pygame.font.SysFont("arial", 70, bold=True)

# Colors
BG_COLOR = (25, 25, 40)
TILE_COLOR = (90, 170, 255)
TEXT_COLOR = (255, 255, 255)
EMPTY_COLOR = (40, 40, 60)
BORDER_COLOR = (15, 15, 30)

# Generate puzzle
def generate_puzzle():
    nums = list(range(9))
    random.shuffle(nums)
    puzzle = [nums[i:i+3] for i in range(0, 9, 3)]
    return puzzle

puzzle = generate_puzzle()

# Find blank tile
def find_blank():
    for i in range(ROWS):
        for j in range(ROWS):
            if puzzle[i][j] == 0:
                return i, j

# Move tile
def move(dx, dy):
    x, y = find_blank()
    nx = x + dx
    ny = y + dy

    if 0 <= nx < ROWS and 0 <= ny < ROWS:
        puzzle[x][y], puzzle[nx][ny] = puzzle[nx][ny], puzzle[x][y]

# Draw board
def draw():
    screen.fill(BG_COLOR)

    for i in range(ROWS):
        for j in range(ROWS):

            value = puzzle[i][j]

            x = j * TILE_SIZE + PADDING
            y = i * TILE_SIZE + PADDING
            size = TILE_SIZE - PADDING * 2

            rect = pygame.Rect(x, y, size, size)

            if value != 0:
                pygame.draw.rect(screen, TILE_COLOR, rect, border_radius=15)

                text = font.render(str(value), True, TEXT_COLOR)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

            else:
                pygame.draw.rect(screen, EMPTY_COLOR, rect, border_radius=15)

    pygame.display.update()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                move(1,0)

            if event.key == pygame.K_DOWN:
                move(-1,0)

            if event.key == pygame.K_LEFT:
                move(0,1)

            if event.key == pygame.K_RIGHT:
                move(0,-1)

    draw()

pygame.quit()