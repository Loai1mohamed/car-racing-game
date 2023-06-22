import pygame
import random

# Define constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
CAR_WIDTH = 50
CAR_HEIGHT = 100
CAR_SPEED = 5
OBSTACLE_SPEED = 5

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Load images
car_image = pygame.image.load("Ci7l2LV.jpg")
car_image = pygame.transform.scale(car_image, (CAR_WIDTH, CAR_HEIGHT))
obstacle_image = pygame.image.load("312673618.jpg")
obstacle_image = pygame.transform.scale(obstacle_image, (CAR_WIDTH, CAR_HEIGHT))

# Create the car
car_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
car_y = SCREEN_HEIGHT - CAR_HEIGHT - 20
car_dx = 0

# Create the obstacles
obstacles = []
for i in range(5):
    obstacle_x = random.randint(0, SCREEN_WIDTH - CAR_WIDTH)
    obstacle_y = random.randint(-SCREEN_HEIGHT, -CAR_HEIGHT)
    obstacles.append((obstacle_x, obstacle_y))

# Create the clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_dx = -CAR_SPEED
            elif event.key == pygame.K_RIGHT:
                car_dx = CAR_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and car_dx < 0:
                car_dx = 0
            elif event.key == pygame.K_RIGHT and car_dx > 0:
                car_dx = 0

    # Move the car
    car_x += car_dx
    if car_x < 0:
        car_x = 0
    elif car_x > SCREEN_WIDTH - CAR_WIDTH:
        car_x = SCREEN_WIDTH - CAR_WIDTH

    # Move the obstacles
    for i in range(len(obstacles)):
        obstacle_x, obstacle_y = obstacles[i]
        obstacle_y += OBSTACLE_SPEED
        if obstacle_y > SCREEN_HEIGHT:
            obstacle_x = random.randint(0, SCREEN_WIDTH - CAR_WIDTH)
            obstacle_y = random.randint(-SCREEN_HEIGHT, -CAR_HEIGHT)
        obstacles[i] = (obstacle_x, obstacle_y)

    # Check for collisions
    car_rect = pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT)
    for obstacle in obstacles:
        obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], CAR_WIDTH, CAR_HEIGHT)
        if car_rect.colliderect(obstacle_rect):
            running = False

    # Draw the screen
    screen.fill((255, 255, 255))
    screen.blit(car_image, (car_x, car_y))
    for obstacle in obstacles:
        screen.blit(obstacle_image, obstacle)
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Clean up
pygame.quit()