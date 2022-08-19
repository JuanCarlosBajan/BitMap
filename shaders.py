from random import random
from mathJCB import dot, toggleSign

def flat(render, **kwargs):
    # Normal calculada por poligono
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    triangleNormal = kwargs["triangleNormal"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    dirLight = render.dirLight
    intensity = dot(triangleNormal, toggleSign(dirLight))

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def gourad(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                        nA[1] * u + nB[1] * v + nC[1] * w,
                        nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = render.dirLight
    intensity = dot(triangleNormal, toggleSign(dirLight))

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def unlit(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    return r, g, b


def toon(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                               nA[1] * u + nB[1] * v + nC[1] * w,
                               nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = render.dirLight
    intensity = dot(triangleNormal, toggleSign(dirLight))

    if intensity < 0.2:
        intensity = 0.1
    elif intensity < 0.5:
        intensity = 0.4
    elif intensity < 0.8:
        intensity = 0.7
    elif intensity <= 1:
        intensity = 1

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def glow(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                               nA[1] * u + nB[1] * v + nC[1] * w,
                               nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = render.dirLight
    intensity = dot(triangleNormal, toggleSign(dirLight))

    b *= intensity
    g *= intensity
    r *= intensity

    camForward = (render.camMatrix.item(0,2),
                  render.camMatrix.item(1,2),
                  render.camMatrix.item(2,2))

    glowAmount = 1 - dot(triangleNormal, camForward)

    if glowAmount <= 0: glowAmount = 0

    yellow = (1,1,0)

    b += yellow[2] * glowAmount
    g += yellow[1] * glowAmount
    r += yellow[0] * glowAmount

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0


def textureBlend(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                               nA[1] * u + nB[1] * v + nC[1] * w,
                               nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = render.dirLight
    intensity = dot(triangleNormal, toggleSign(dirLight))

    b *= intensity
    g *= intensity
    r *= intensity

    if render.active_texture2:
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor2 = render.active_texture2.getColor(tU, tV)

        b += (1 - intensity) * texColor2[2]
        g += (1 - intensity) * texColor2[1]
        r += (1 - intensity) * texColor2[0]

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if b < 0: b = 0
    if g < 0: g = 0
    if r < 0: r = 0

    return r, g, b


def jccc(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                        nA[1] * u + nB[1] * v + nC[1] * w,
                        nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = render.dirLight
    intensity = dot(triangleNormal, toggleSign(dirLight))


    if intensity > 0:
        b = (0.8*abs(intensity)*50)%1
        g = (0.5 *abs(intensity)*50)%1
        r = (0.3 *abs(intensity)*50)%1
        b *= (1*intensity)%1
        g *= intensity
        r *= intensity
        

    else :
        b = (1*intensity)%1
        g = (1 *intensity)%1
        r = (1 *intensity)%1

    return r, g, b

def jccc2(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                               nA[1] * u + nB[1] * v + nC[1] * w,
                               nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = render.dirLight
    intensity = dot(triangleNormal, toggleSign(dirLight))

    if intensity < -0.9:
        b = (1*intensity)%1
        g = (1 *intensity)%1
        r = (1 *intensity)%1 
    elif intensity < -0.8:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]) * abs(intensity))
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]))
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2]))
    elif intensity < -0.7:
        b = (1*intensity)%1
        g = (1 *intensity)%1
        r = (1 *intensity)%1 
    elif intensity < -0.6:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]))
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]) * abs(intensity))
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2]))
    elif intensity < -0.5:
        b = (1*intensity)%1
        g = (1 *intensity)%1
        r = (1 *intensity)%1 
    elif intensity < -0.4:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]))
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]))
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2]) * abs(intensity))
    elif intensity < -0.3:
        b = (1*intensity)%1
        g = (1 *intensity)%1
        r = (1 *intensity)%1 
    elif intensity < -0.2:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]) * abs(intensity))
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]))
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2])) 
    elif intensity < -0.1:
        b = (1*abs(intensity))
        g = (1 *abs(intensity))
        r = (1 *abs(intensity))
    elif intensity < 0:
        b = 0
        g = 0
        r = 0   
    elif intensity < 0.1:
        b = (1*intensity)%1
        g = (1 *intensity)%1
        r = (1 *intensity)%1
    elif intensity < 0.2:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]))
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]) * intensity)
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2]))
    elif intensity < 0.3:
        b = (1*intensity)%1
        g = (1 *intensity)%1
        r = (1 *intensity)%1
    elif intensity < 0.4:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]))
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]))
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2]) *intensity)
    elif intensity < 0.5:
        b = (1*intensity)%1
        g = (1 *intensity)%1
        r = (1 *intensity)%1
    elif intensity < 0.6:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]) * intensity)
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]))
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2]))
    elif intensity < 0.7:
        b = (1*intensity)%1
        g = (1 *intensity)%1
        r = (1 *intensity)%1
    elif intensity < 0.6:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]))
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]) * intensity)
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2]))
    elif intensity < 0.8:
        b = (1*intensity)%1
        g = (1 *intensity)%1
        r = (1 *intensity)%1
    elif intensity < 0.9:
        b = (abs(nA[0])*abs(nA[1])*abs(nA[2]))
        g = (abs( nB[0])*abs( nB[1])*abs( nB[2]))
        r = (abs(nC[0])*abs(nC[1])*abs(nC[2]) *intensity)
    elif intensity <= 1:
        b = (1*intensity)%1
        g = (1 *intensity)%1
        r = (1 *intensity)%1
 
    return r, g, b

def jccc3(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                               nA[1] * u + nB[1] * v + nC[1] * w,
                               nA[2] * u + nB[2] * v + nC[2] * w]

    dirLight = render.dirLight
    intensity = dot(triangleNormal, toggleSign(dirLight))

    # if intensity > 0:    
    #     b = (random() * (1/intensity))%1
    #     g = (random() * (1/intensity))%1
    #     r = (random() * (1/intensity))%1
    # elif intensity > 0.1:
    #     r = 0
    #     g = 0
    #     b = 0
    # elif intensity >= -1:
    #     b = (random() * (1/intensity))%1
    #     g = (random() * (1/intensity))%1
    #     r = (random() * (1/intensity))%1

    if intensity > 0.2:    
        g *= ((1/intensity))%1
        r *= ((1/intensity))%1
        b *= ((1/intensity))%1
    elif intensity > 0:
        b = 0*((1/intensity))%1
        g = 0*((1/intensity))%1
        r = 1*((1/intensity))%1
    elif intensity > -0.1:
        r = random()
        g = 0
        b = 0
    elif intensity >= -1:
        b = 0*((1/intensity))%1
        g = 0*((1/intensity))%1
        r = 1*((1/intensity))%1

    return r, g, b