from ships import Interceptor, Bomber, Fighter

class Player:
    def __init__(self, ship_class_name):
        if ship_class_name == "Interceptor":
            self.ship = Interceptor()
        elif ship_class_name == "Bomber":
            self.ship = Bomber()
        else: # Default to Fighter
            self.ship = Fighter()

        self.health = self.ship.base_health
        self.shields = self.ship.base_shields

        # Energy Triangle: Power distribution (sums to 100)
        self.power_speed = 34
        self.power_weapons = 33
        self.power_shields = 33

    def set_power_distribution(self, speed_pct, weapons_pct, shields_pct):
        """Sets the power distribution, ensuring it sums to 100."""
        if speed_pct + weapons_pct + shields_pct != 100:
            print("Error: Power distribution must sum to 100.")
            return

        self.power_speed = speed_pct
        self.power_weapons = weapons_pct
        self.power_shields = shields_pct
        print(f"Power set to: Speed={self.power_speed}%, Weapons={self.power_weapons}%, Shields={self.power_shields}%")

    def get_stats(self):
        """Returns the current stats based on power distribution."""
        # In a real implementation, these would be modified by base stats from self.ship
        speed = self.power_speed * 2 # Example modifier
        weapon_recharge = self.power_weapons
        shield_strength = self.power_shields * 1.5 + self.ship.base_shields # Example modifier
        return {"speed": speed, "weapon_recharge": weapon_recharge, "shield_strength": shield_strength}
