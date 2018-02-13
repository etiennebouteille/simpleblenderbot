import bpy
from random import randrange
from math import radians

rotation = randrange(0, 360, 1)
print("degrees = ", rotation)
print("radians = ", radians(rotation))

bpy.data.objects['Suzanne'].select = True
bpy.context.scene.objects.active = bpy.data.objects['Suzanne']
bpy.context.object.rotation_euler[2] = radians(rotation)

rndr = bpy.data.scenes['Scene'].render
rndr.filepath = 'mypicture.png'
bpy.ops.render.render(write_still=True)
