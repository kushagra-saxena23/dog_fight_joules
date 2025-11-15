from ursina import *
from player import Player
from enemy import Enemy

def main():
    # Initialize Ursina in standard windowed mode
    app = Ursina()

    # Create the space background
    Sky(texture='sky_default')

    # Create the player and enemy from our refactored classes
    enemy = Enemy(position=(20, 5, 100))
    player = Player(position=(0, 5, -10), speed=50, gravity=0)
    player.set_enemy(enemy) # Pass a reference of the enemy to the player for collision detection


    # Add a cockpit frame
    cockpit_frame = Entity(parent=camera.ui, model='quad', scale=0.9, color=color.clear, texture='white_cube', scale_x=0.9*window.aspect_ratio)
    cockpit_frame.texture.alpha = 128

    # Add an aiming reticle
    reticle = Text(text='+', scale=2, origin=(0,0), position=(0,0))

    # Create the Stunt Meter UI
    stunt_meter_bg = Entity(parent=camera.ui, model='quad', scale=(.5, .02), position=(0, -.45), color=color.dark_gray)
    stunt_meter = Entity(parent=camera.ui, model='quad', scale=(0, .02), position=(-.25, -.45), color=color.cyan)

    # Add control instructions
    Text("Click Window to Start | WASD to Move | Mouse to Look | Left Click to Fire",
         position=window.bottom_left + (0.01, 0.01),
         origin=(-0.5, -0.5),
         scale=1)

    # Add a title to the window
    window.title = "Aces in the Void: Strikeforce"

    # Hide and lock the mouse cursor
    mouse.locked = True

    # Start the game loop
    app.run()


if __name__ == '__main__':
    main()
