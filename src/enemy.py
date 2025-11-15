from ursina import *

class Enemy(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = 'sphere'
        self.color = color.red
        self.scale = 3
        self.original_color = self.color

    def update(self):
        # Check if we have been hit by a projectile
        hit_info = self.intersects()
        if hit_info.hit:
            if "projectile" in hit_info.entity.name: # A simple way to check if it's a projectile
                self.color = color.orange
                invoke(self.reset_color, delay=0.1)

    def reset_color(self):
        self.color = self.original_color
