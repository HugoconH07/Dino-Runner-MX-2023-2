import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.large_cactus import Large_Cactus
from dino_runner.components.obstacles.bird import Bird
class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
        
    def update(self, game_speed, player):
        if len(self.obstacles) ==0:
            if random.randint(0,2) ==0:
              self.obstacles.append(Cactus())
            elif random.randint(0,2) ==1:
                self.obstacles.append(Large_Cactus())  
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.pop()
            obstacle.update(game_speed,player)    
            
            
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)