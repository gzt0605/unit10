# Ryan Ge
# November 21, 2016
# Apply the target class

import pygame, sys
from pygame.locals import *
import target

def main():
    '''
    This is the main function that sets up the Pygame interface with a target class
    :return: nothing
    '''

    pygame.init()
    target_surface = pygame.display.set_mode((600, 600), 0, 32)
    pygame.display.set_caption('Archery Game')


    main_surface = target.Target(target_surface)
    main_surface.draw_target()

    click = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                click += 1
                if click > 5:
                    pygame.quit()
                else:
                    main_surface.get_score(pygame.mouse.get_pos())

main()
