# Ryan Ge
# November 21, 2016
# Archery target

import pygame
class Target:

    def __init__(self, surface):
        pygame.init()
        self.surface = surface
        self.surface.fill((255, 255, 255))
        self.total_score = 0


    def draw_target(self):
        WHITE = (254, 254, 254)
        BLACK = (0, 0, 0)
        BLUE = (0, 0, 255)
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        DARK_GREY = (1, 1, 1)

        pygame.draw.circle(self.surface, DARK_GREY, (300, 300), 151, 0)
        pygame.draw.circle(self.surface, WHITE, (300, 300), 150, 0)
        pygame.draw.circle(self.surface, BLACK, (300, 300), 120, 0)
        pygame.draw.circle(self.surface, BLUE, (300, 300), 90, 0)
        pygame.draw.circle(self.surface, RED, (300, 300), 60, 0)
        pygame.draw.circle(self.surface, YELLOW, (300, 300), 30, 0)

        pygame.display.update()

    def get_score(self, position):
        self.surface.fill((255, 255, 255))
        self.draw_target()

        YELLOW = (255, 255, 0, 255)
        RED = (255, 0, 0, 255)
        BLUE = (0, 0, 255, 255)
        BLACK = (0, 0, 0, 255)
        WHITE = (254, 254, 254, 255)

        target_color = self.surface.get_at(position)
        archery_score = 0
        if target_color == YELLOW:
            archery_score = 9
        elif target_color == RED:
            archery_score = 7
        elif target_color == BLUE:
            archery_score = 5
        elif target_color == BLACK:
            archery_score = 3
        elif target_color == WHITE:
            archery_score = 1

        self.total_score += archery_score

        score_font = pygame.font.SysFont("Helvetica", 32)
        score_label = score_font.render(str(self.total_score), 1, (0, 0, 0))
        self.surface.blit(score_label, (10, 10))

        pygame.display.update()
