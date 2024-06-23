import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)


# Ball class
class Ball:
    def __init__(self):
        self.x = random.randint(20, screen_width - 20)
        self.y = random.randint(20, screen_height - 20)
        self.radius = 20
        self.dx = random.choice([-4, -3, -2, 2, 3, 4])
        self.dy = random.choice([-4, -3, -2, 2, 3, 4])

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x <= 0 or self.x >= screen_width:
            self.dx = -self.dx
        if self.y <= 0 or self.y >= screen_height:
            self.dy = -self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, white, (self.x, self.y), self.radius)

# Create balls
balls = [Ball() for _ in range(10)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    for ball in balls:
        ball.move()
        ball.draw(screen)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
