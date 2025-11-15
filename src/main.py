from ursina import *

# Define a simple player ship class
class PlayerShip(Entity):
    def __init__(self):
        super().__init__(
            model='cube',  # Using a simple cube for the prototype
            color=color.white,
            scale=(1, 0.5, 2),
            position=(0, 0, 0)
        )
        self.speed = 50

    def update(self):
        # This function is called every frame and handles player controls
        # Move the ship
        self.x += held_keys['d'] * time.dt * self.speed
        self.x -= held_keys['a'] * time.dt * self.speed
        self.y += held_keys['w'] * time.dt * self.speed
        self.y -= held_keys['s'] * time.dt * self.speed

        # Rotate the ship with the mouse and keys
        self.rotation_x -= mouse.velocity[1] * 200 * time.dt
        self.rotation_y += mouse.velocity[0] * 200 * time.dt
        self.rotation_z -= held_keys['q'] * 100 * time.dt
        self.rotation_z += held_keys['e'] * 100 * time.dt


def main():
    # Initialize Ursina in standard windowed mode
    app = Ursina()

    # Create the space background
    Sky(texture='sky_default')

    # Create the player ship
    player = PlayerShip()

    # Create a static enemy ship
    enemy = Entity(
        model='cube',
        color=color.red,
        scale=(1, 0.5, 2),
        position=(10, 2, 50) # Place it in the distance
    )

    # Create the Stunt Meter UI
    stunt_meter_bg = Entity(parent=camera.ui, model='quad', scale=(.5, .02), position=(0, -.45), color=color.dark_gray)
    stunt_meter = Entity(parent=camera.ui, model='quad', scale=(0, .02), position=(-.25, -.45), color=color.cyan)


    # Set up a third-person camera
    camera.position = (0, 10, -30)
    camera.look_at(player)

    # Add a title to the window
    window.title = "Aces in the Void: Strikeforce"

    # Start the game loop
    app.run()


if __name__ == '__main__':
    main()
