import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.large_cactus import Large_Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import BIRD,LARGE_CACTUS,SMALL_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
        
    def update(self, game_speed, player):
        if len(self.obstacles) ==0: 
            
            obstacle_aparition = random.randint(0,2) 
            match obstacle_aparition:
                case 0:
                    self.obstacles.append(Cactus(SMALL_CACTUS))
                case 1:
                    self.obstacles.append(Large_Cactus(LARGE_CACTUS))  
                case 2:
                    self.obstacles.append(Bird(BIRD))
                 
        for obstacle in self.obstacles:
        
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.pop()
            obstacle.update(game_speed,player)    
            
            
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)