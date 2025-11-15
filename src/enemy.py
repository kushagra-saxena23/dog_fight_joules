from ships import Interceptor, Bomber, Fighter

class Enemy:
    def __init__(self, ship_class_name):
        if ship_class_name == "Interceptor":
            self.ship = Interceptor()
        elif ship_class_name == "Bomber":
            self.ship = Bomber()
        else: # Default to Fighter
            self.ship = Fighter()

        self.health = self.ship.base_health
        self.shields = self.ship.base_shields
