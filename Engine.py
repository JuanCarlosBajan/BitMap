from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, gourad
from shaders import flat, unlit, gourad, toon, glow, textureBlend, jccc, jccc2, jccc3

width = 960
height = 1400

rend = Renderer(width, height)



rend.dirLight = V3(-0.5,0,-0.5)
rend.active_shader = jccc

"""
rend.active_texture = Texture("model.bmp")

rend.active_texture = Texture("earthDay.bmp")
rend.active_texture2 = Texture("earthNight.bmp")
rend.active_shader = textureBlend

rend.glLoadModel("earth.obj",
                 translate = V3(0, 0, -10),
                 scale = V3(0.01,0.01,0.01),
                 rotate = V3(0,90,0))



#rend.active_texture = Texture("models/model.bmp")
#rend.active_shader = gourad
#rend.glLoadModel("models/model.obj",
#                 translate = V3(-4, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))

#rend.active_shader = toon
#rend.glLoadModel("models/model.obj",
#                 translate = V3(0, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))

#rend.active_shader = glow
#rend.glLoadModel("models/model.obj",
#                 translate = V3(4, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))

rend.glLoadModel("model.obj",
                 translate = V3(width/2, height/2, 0),
                 rotate = V3(0, 180, 0), 
                 scale = V3(1000,1000,1000)) """

#rend.active_texture2 = Texture("earthNight.bmp")
#rend.active_shader = textureBlend

rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(2.5, 2.2, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(-2.5, 2.2, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(0, 2.2, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.active_texture = Texture("BitMap/Models&Outputs/bn.bmp")
rend.active_shader = jccc2

rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(2.5, -1, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(-2.5, -1, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(0, -1, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.active_texture = Texture("BitMap/Models&Outputs/bn.bmp")
rend.active_shader = jccc3

rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(2.5, -4.5, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(-2.5, -4.5, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.glLoadModel("BitMap/Models&Outputs/skull.obj",
                 translate = V3(0, -4.5, -10),
                 scale = V3(0.1,0.1,0.1),
                 rotate = V3(-90,0,0))

rend.glFinish("BitMap/Models&Outputs/output.bmp")