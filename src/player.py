from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from projectile import Projectile

class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = 'cube'
        self.color = color.white
        self.scale = (1, 0.5, 2)

    def set_enemy(self, enemy):
        self.enemy = enemy

    def input(self, key):
        if key == 'left mouse down':
            projectile = Projectile(
                position=self.position + camera.forward * 2,
                direction=camera.forward,
                enemy=self.enemy
            )
