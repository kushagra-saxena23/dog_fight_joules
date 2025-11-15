from ursina import *

class Projectile(Entity):
    def __init__(self, position, direction, enemy):
        super().__init__(
            model='quad',
            scale=(0.5, 0.1, 0.1),
            position=position,
            rotation=camera.rotation,
            color=color.yellow
        )
        self.direction = direction
        self.speed = 200
        self.enemy = enemy

    def update(self):
        self.position += self.direction * self.speed * time.dt
        if self.intersects(self.enemy).hit or self.z > 200:
            destroy(self)
