from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

def input(key):
    if key == 'escape':
        quit()

app = Ursina()

window.title = "py1"

mesh = Entity(model='cube',texture='assets/grass.jpg',collider='cube')

sky = Sky()

player = FirstPersonController(speed = 0.2)
player.gravity = 2
app.run()