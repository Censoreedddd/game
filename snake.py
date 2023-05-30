import pygame
import time

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600

# Set the colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)

# Create the game window
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Set the frame rate
fps = pygame.time.Clock()

# Set the Snake's initial position and size
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'

# Set the initial food position
food_position = [random.randrange(1, (screen_width // 10)) * 10,
                 random.randrange(1, (screen_height // 10)) * 10]
food_spawned = True

# Set the initial score
score = 0

# Function to handle keyboard events
def handle_events():
    global snake_direction

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_direction = 'RIGHT'
            elif event.key == pygame.K_LEFT:
                snake_direction = 'LEFT'
            elif event.key == pygame.K_UP:
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN:
                snake_direction = 'DOWN'

# Function to update the snake's position and check for collisions
def update_snake():
    global snake_position, snake_body, food_position, food_spawned, score

    if snake_direction == 'RIGHT':
        snake_position[0] += 10
    elif snake_direction == 'LEFT':
        snake_position[0] -= 10
    elif snake_direction == 'UP':
        snake_position[1] -= 10
    elif snake_direction == 'DOWN':
        snake_position[1] += 10

    snake_body.insert(0, list(snake_position))

    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawned = False
    else:
        snake_body.pop()

# Function to generate food at random positions
def generate_food():
    global food_position, food_spawned

    if not food_spawned:
        food_position = [random.randrange(1, (screen_width // 10)) * 10,
                         random.randrange(1, (screen_height // 10)) * 10]
        food_spawned = True

# Function to draw the Snake, food, and score on the screen
def draw():
    global score

    game_window.fill(black)

    for position in snake_body:
        pygame.draw.rect(game_window, white, pygame.Rect(
            position[0], position[1], 10, 10))

    pygame.draw.rect(game_window, red, pygame.Rect(
        food_position[0], food_position[1], 10, 10))

    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, white)
    game_window.blit(score_text, [10, 10])

    pygame.display.flip()

# Main game loop
while True:
    handle_events