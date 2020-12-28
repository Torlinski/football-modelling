import pygame

from dimensions import DIMENSIONS        
from color import BLACK, BLUE, RED, GREEN, WHITE

pygame.init()

class Display:
    def __init__(self):
        self.width = 1600
        self.height = 1000
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.screen.fill((0,255,0))
        self.num_players = 4
        self.players = self.setup_players(self.num_players)
        self.setup_pitch()
        self.setup_goal()
        self.running = True
        while self.running:
            self.run()
        pygame.quit()

    def setup_players(self, n):
        pygame.draw.circle(self.screen, BLUE, (250, 250), DIMENSIONS["player_width"])
        pygame.draw.circle(self.screen, BLUE, (300, 300), DIMENSIONS["ball"])
        #pass

    def setup_pitch(self):
        pygame.draw.line(self.screen, WHITE, (200, 200), (250, 400))

    def setup_goal(self):
        #arguably should extend pygame.sprite.Sprite class
        goal_surf = pygame.Surface((DIMENSIONS["goal_width"], 2))
        goal_surf.fill(BLACK)
        goal_coords = goal_surf.get_rect(
                topleft=((self.width - DIMENSIONS["goal_width"])/2, 0))
        self.screen.blit(goal_surf, goal_coords)

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        pygame.display.flip()

class Player:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team

Display()
