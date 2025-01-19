import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Eats Cake")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Snake and cake setup
snake_pos = [100, 50]
snake_size = 40
snake_speed = 10

cake_pos = [300, 200]
cake_size = 80

# Game variables
running = True
win = False

# Main game loop
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control snake movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake_pos[1] -= snake_speed
    if keys[pygame.K_DOWN]:
        snake_pos[1] += snake_speed
    if keys[pygame.K_LEFT]:
        snake_pos[0] -= snake_speed
    if keys[pygame.K_RIGHT]:
        snake_pos[0] += snake_speed

    # Draw the snake and the cake
    pygame.draw.rect(screen, GREEN, (*snake_pos, snake_size, snake_size))
    pygame.draw.rect(screen, RED, (*cake_pos, cake_size, cake_size))

    # Check for collision
    if (abs(snake_pos[0] - cake_pos[0]) < cake_size and
        abs(snake_pos[1] - cake_pos[1]) < cake_size):
        win = True

    # Display win message
    if win:
        win_text = font.render("You Win!", True, BLACK)
        screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - win_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # Update display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
