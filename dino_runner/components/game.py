import pygame

from dino_runner.utils.constants import TRK, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, DINO_START, RESET
from dino_runner.components import text_utils
from dino_runner.components.dinosaur import Dinosaur 
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 180
        self.x_pos_cloud = 0
        self.y_pos_cloud = 150
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager() 
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.death_count = 0
       # self.game_sound = pygame.mixer.Sound(SOUND_GAME)

    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                #self.game_sound.play()
                self.reset()

    def update(self):
        if self.playing:  
           user_input = pygame.key.get_pressed()
           self.player.update(user_input)
           self.obstacle_manager.update(self.game_speed, self.player)
           self.power_up_manager.update(self.game_speed, self.points, self.player)
           self.points += 1
           if self.points % 200 == 0:
               self.game_speed += 1
           if self.player.dino_dead:
              self.playing = False
              self.death_count += 1

    def draw(self):
        if self.playing:  
            self.clock.tick(FPS)
            self.screen.fill((255, 255, 255))
            self.draw_background()
            self.draw_cloud()
            self.player.draw(self.screen)
            self.draw_score()
            self.obstacle_manager.draw(self.screen)
            self.power_up_manager.draw(self.screen)
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = TRK.get_width()
        self.screen.blit(TRK, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(TRK, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(TRK, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
      
    def draw_cloud(self):
        cloud_speed = 4
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD,(image_width + self.x_pos_cloud,self.y_pos_cloud))
            self.x_pos_cloud = 0
        self.x_pos_cloud -= cloud_speed  
        
        
    def draw_score(self):
        score, score_rect = text_utils.get_message('Points' + str(self.points),20, 1000, 40)
        self.screen.blit(score, score_rect)
        
         
   # def draw_time_power(self):
       # power, score_rect = text_utils.get_message('Points' + str(self.time_to_show),20, 700, 40)
       # self.screen.blit(power, score_rect)
        
        
    def draw_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        if self.death_count ==0:
            self.screen.blit(DINO_START,(SCREEN_WIDTH // 2 -40, SCREEN_HEIGHT // 2 - 140))
            text, text_rect = text_utils.get_message('Press any Key to Star', 30)
            self.screen.blit(text, text_rect)
        else:
            self.screen.blit(DINO_START,(SCREEN_WIDTH // 2 -40, SCREEN_HEIGHT // 2 - 120))
            text, text_rect = text_utils.get_message('press any Key to Restar', 30)
            score, score_rect = text_utils.get_message('Your score: ' + str(self.points), 30, heigth = SCREEN_HEIGHT//2 + 50)       
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(RESET,(SCREEN_WIDTH // 2 -40, SCREEN_HEIGHT // 2 +150))
            
    def reset(self):
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager() 
        self.power_up_manager = PowerUpManager()
        self.points = 0