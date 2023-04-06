import random
from dino_runner.components.obstacles.obstacle import Obstacle
#from dino_runner.utils.constants import ROCK

class Rock(Obstacle):
    
    Y_POS_ROCK = 355
    
    def __init__(self,image):
        self.type = random.choice([0])
        super().__init__(image, self.type)
        self.rect.y = self.Y_POS_ROCK