import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS
class Cactus(Obstacle):
    
    Y_POS_CACTUS = 325
    
    def __init__(self,image):
        self.type = random.choice([0,2])
        super().__init__(image,self.type)
        self.rect.y = self.Y_POS_CACTUS