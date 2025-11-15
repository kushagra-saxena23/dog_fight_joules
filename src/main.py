from ursina import *
import os

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
        # This function is called every frame
        # In a real game, this is where controls would be checked
        self.x += held_keys['d'] * time.dt * self.speed
        self.x -= held_keys['a'] * time.dt * self.speed
        self.y += held_keys['w'] * time.dt * self.speed
        self.y -= held_keys['s'] * time.dt * self.speed

        self.rotation_x -= mouse.velocity[1] * 200 * time.dt
        self.rotation_y += mouse.velocity[0] * 200 * time.dt
        self.rotation_z -= held_keys['q'] * 100 * time.dt
        self.rotation_z += held_keys['e'] * 100 * time.dt


def main():
    # Define the screenshot path
    screenshot_path = 'screenshots/04_stunt_meter_ui.png'

    # Ensure the screenshots directory exists
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    # Manually remove the old screenshot if it exists
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)

    # Initialize Ursina
    app = Ursina(window_type='offscreen', development_mode=False, borderless=False)

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
    # This is the bar that would fill up. We'll show it empty for now.
    stunt_meter = Entity(parent=camera.ui, model='quad', scale=(0, .02), position=(-.25, -.45), color=color.cyan)


    # Set up a third-person camera
    camera.position = (0, 10, -30)
    camera.look_at(player)

    # Add a title
    window.title = "Aces in the Void: Strikeforce"

    # Render a frame
    app.step()

    # Capture and quit
    print("Capturing screenshot...")
    base.screenshot(namePrefix=screenshot_path, defaultFilename=0)
    print("Screenshot saved.")
    application.quit()

if __name__ == '__main__':
    main()
