from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from maze_generator import generate_maze

height = 11
width = 27

app = Ursina()

# Define a Voxel class.
# By setting the parent to scene and the model to 'cube' it becomes a 3d button.

def update():
    if held_keys['left control']: print("CTRL pressed!") 

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white_cube',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime,
        )


    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)

            if key == 'right mouse down':
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = 'white_cube',
            scale = 150,
            double_sided = True,
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'cube',
            texture = 'white_cube',
            rotation = Vec3(150,-10,0),
            scale = 0.2,
            position = Vec2(-5,0)
        )

class Tile(Entity):
    def __init__(self,position=(0,0,0)):
        super().__init__(
            parent =scene,
            position= position,
            model = 'quad',
            rotation = Vec3(100,0,0),
            origin_y = .5,
            texture = 'white_cube',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime,
            scale = 2,
            
        )

def CreateRoom(): 
    size_room = 16
    size_wall = 5

    maze = generate_maze()

    #create floor
    #for z in range(0, height):
    #    for x in range(0, width):
    #        voxel = Voxel(position=(x,0,z))

    for y in range(size_wall):
        for i in range(0, height):
            for j in range(0, width):
                if y==0:
                    voxel = Voxel(position=(i,y,j))
                elif (maze[i][j] == 'u'):
                    pass
                elif (maze[i][j] == 'c'):
                    pass
                else:
                    voxel = Voxel(position=(i,y,j))

    """
    for z in range(size_room):
        for x in range(size_room):
            for y in range(size_wall):
                if x ==0 or z==0 or x == size_room-1 or z==size_room-1: 
                    voxel = Voxel(position=(x,y,z))
                else:
                    voxel = Voxel(position=(x,0,z))
    """

CreateRoom()
player = FirstPersonController(position=(5,0,5))
#sky = Sky()
#hand = Hand()
app.run()