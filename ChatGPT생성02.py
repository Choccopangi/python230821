# ChatGPT 질문: 블록 깨기 게임의 파이썬 코드를 작성해줘

import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaking Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Paddle settings
paddle_width = 150
paddle_height = 10
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 20
paddle_speed = 5

# Ball settings
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

# Block settings
block_width = 60
block_height = 20
num_blocks = 6
blocks = []

for i in range(num_blocks):
    block = pygame.Rect(90 + i * 120, 50, block_width, block_height)
    blocks.append(block)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x <= 0 or ball_x >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y

    if paddle_x <= ball_x <= paddle_x + paddle_width and paddle_y <= ball_y + ball_radius <= paddle_y + paddle_height:
        ball_speed_y = -ball_speed_y

    for block in blocks:
        if block.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
            ball_speed_y = -ball_speed_y
            blocks.remove(block)
            break

    win.fill(WHITE)

    pygame.draw.rect(win, GREEN, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(win, BLUE, (ball_x, ball_y), ball_radius)

    for block in blocks:
        pygame.draw.rect(win, RED, block)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
