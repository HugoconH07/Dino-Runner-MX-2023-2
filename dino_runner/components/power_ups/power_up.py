import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class PowerUp(Sprite):
    Y_POS_POWER_UP = 125
    POWER_UP_DURATION = 4200
    def __init__(self, image, type):
        print("power")
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS_POWER_UP
        self.rect.x = SCREEN_WIDTH
        self.start_time = 0
        self.time_up = 0
        self.used = False
        
    def update(self, game_speed, player):
        self.rect.x -= game_speed
        if self.rect.colliderect(player.dino_rect):
            self.start_time = pygame.time.get_ticks()
            self.time_up = self.start_time + self.POWER_UP_DURATION
            self.used = True
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)