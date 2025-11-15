from player import Player
from enemy import Enemy

def main():
    print("Welcome to Aces in the Void: Ignition!")
    print("=" * 30)

    # 1. Create a player and an enemy
    player = Player("Interceptor")
    enemy = Enemy("Bomber")
    print(f"Player created as an {player.ship.name}")
    print(f"Enemy created as a {enemy.ship.name}")
    print("-" * 30)

    # 2. Show initial player stats
    initial_stats = player.get_stats()
    print("Player Initial Stats:")
    print(f"  - Speed: {initial_stats['speed']}")
    print(f"  - Weapon Recharge: {initial_stats['weapon_recharge']}%")
    print(f"  - Shield Strength: {initial_stats['shield_strength']}")
    print("-" * 30)


    # 3. Demonstrate the Energy Triangle
    print("Diverting all power to shields...")
    player.set_power_distribution(0, 0, 100)

    # 4. Show updated player stats
    updated_stats = player.get_stats()
    print("\nPlayer Updated Stats:")
    print(f"  - Speed: {updated_stats['speed']}")
    print(f"  - Weapon Recharge: {updated_stats['weapon_recharge']}%")
    print(f"  - Shield Strength: {updated_stats['shield_strength']}")
    print("-" * 30)

    # 5. Demonstrate secondary weapon usage
    player.ship.use_secondary()
    enemy.ship.use_secondary()


if __name__ == "__main__":
    main()
