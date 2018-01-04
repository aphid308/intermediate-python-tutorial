import pygame
import random

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()

def draw_environment():
    game_display.fill(WHITE)
    pygame.display.update()

def main():
    while True:
        for even in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment()
        clock.tick(60)


class Blob:

    def __init__(self, color):
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(4,8)
        self.color = color

    def move(self):
        self.move_x = random.randrange(-1,2)
        self.move_y = random.randrange(-1,2)
        self.x += self.move_x
        self.y += self.move_y

        if self.x < 0:
            self.x = 0

        elif self.x > WIDTH:
            self.x = WIDTH

        if self.y < 0:
            self.y = 0

        elif self.y > HEIGHT:
            self.y = HEIGHT

if __name__ == '__main__':
    main()
