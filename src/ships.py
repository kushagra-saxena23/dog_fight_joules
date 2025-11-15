class Ship:
    def __init__(self, name, health, shields):
        self.name = name
        self.base_health = health
        self.base_shields = shields

    def use_secondary(self):
        raise NotImplementedError

class Interceptor(Ship):
    def __init__(self):
        super().__init__("Interceptor", 80, 60)
        self.primary_weapon = "Homing Missiles"
        self.secondary_weapon = "Afterimage Decoy"

    def use_secondary(self):
        print(f"{self.name} deploys an afterimage decoy!")

class Bomber(Ship):
    def __init__(self):
        super().__init__("Bomber", 150, 100)
        self.primary_weapon = "Proton Torpedoes"
        self.secondary_weapon = "Point-Defense Turret"

    def use_secondary(self):
        print(f"{self.name} deploys a point-defense turret!")

class Fighter(Ship):
    def __init__(self):
        super().__init__("Fighter", 100, 80)
        self.primary_weapon = "Rapid-fire Cannons"
        self.secondary_weapon = "Target-Lock Breaker"

    def use_secondary(self):
        print(f"{self.name} emits a target-lock breaker EMP pulse!")
