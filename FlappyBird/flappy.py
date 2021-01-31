import pygame
import neat
import time
import os
import random

WIN_WIDTH = 300
WIN_HEIGHT = 900

DOT_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "dot.png")))
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png")))


class Dot:
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tick_count = 0
        self.vel = 0
        self.height = self.y

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        d = (self.vel * self.tick_count) + (1.5 * self.tick_count ** 2)

        # FAIL SAFE
        if d >= 16:  # if moving down >= 16 pixels
            d = 16  # so we don't move to fast
        if d < 0:  # if moving upwards
            d -= 2  # move a little bit more

        self.y = self.y + d  # change y position
        #####################

    def draw(self, win):
        win.blit(DOT_IMG, (0, 0))

    def get_mask(self):
        return pygame.mask.from_surface(DOT_IMG)


def draw_window(win, dot):
    win.blit(BG_IMG, (0, 0))
    dot.draw(win)
    pygame.display.update()


def main():
    dot = Dot(200, 200)
    win = pygame.display.set_mode((WIN_HEIGHT, WIN_HEIGHT))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(win, dot)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
