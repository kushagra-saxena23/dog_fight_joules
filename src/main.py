from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

def main():
    # Initialize Ursina in standard windowed mode
    app = Ursina()

    # Create the space background
    Sky(texture='sky_default')

    # Create a reliable, built-in flight controller
    # The user will fly from a first-person perspective
    player = FirstPersonController(
        position=(0, 5, -10),
        speed=50
    )
    # Attach a simple model to the controller to represent our "ship"
    ship_model = Entity(parent=player, model='cube', scale=(1, 0.5, 2), color=color.white, position=(0, -1, 0))


    # Create a static enemy ship to fly towards
    enemy = Entity(
        model='cube',
        color=color.red,
        scale=(2, 1, 4),
        position=(20, 5, 100) # Place it in the distance
    )

    # Create the Stunt Meter UI
    stunt_meter_bg = Entity(parent=camera.ui, model='quad', scale=(.5, .02), position=(0, -.45), color=color.dark_gray)
    stunt_meter = Entity(parent=camera.ui, model='quad', scale=(0, .02), position=(-.25, -.45), color=color.cyan)

    # Add on-screen control instructions
    Text("WASD to Move | Mouse to Look",
         position=window.bottom_left + (0.01, 0.01),
         origin=(-0.5, -0.5),
         scale=1)

    # Add a title to the window
    window.title = "Aces in the Void: Strikeforce"

    # Hide the mouse cursor
    mouse.locked = True

    # Start the game loop
    app.run()


if __name__ == '__main__':
    main()
