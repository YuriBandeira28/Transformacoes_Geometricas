import matplotlib.pyplot as plt
import math


# Definindo os limites dos eixos
dim = [5, 5]
plt.xlim(0, dim[0])
plt.ylim(0, dim[1])
# Mantendo a proporção dos eixos
plt.gca().set_aspect('equal', adjustable='box')

pts_x = [1, 2, 2, 1]

pts_y = [1, 1, 2, 2]


quad = plt.Polygon([[pts_x[0], pts_y[0]],
                    [pts_x[1], pts_y[1]],
                    [pts_x[2], pts_y[2]],
                    [pts_x[3], pts_y[3]]],
                          closed=True,
                          fill = False,
                          edgecolor='blue',
                          color='blue')

plt.gca().add_patch(quad)


def rotacao(rad, pts_x, pts_y, centro_x, centro_y):

    # pontos_x = [-0.5, 0.5 ,0.5 ,-0.5, -0.5]
    # pontos_y = [-0.5,-0.5,0.5, 0.5, -0.5]

    pontos_x = [centro_x - pts_x[0],
                centro_x - pts_x[1],
                centro_x - pts_x[2],
                centro_x - pts_x[3],
                centro_x - pts_x[4]]
    
    pontos_y = [centro_y - pts_y[0],
                centro_y - pts_y[1],
                centro_y - pts_y[2],
                centro_y - pts_y[3],
                centro_y - pts_y[4]]


    # x = x.cos(Θ) - y.sen(Θ)
    xR = []
    for i, x in enumerate(pontos_x):
        x = x * math.cos(rad) - pontos_y[i] * math.sin(rad)
        xR.append(x)

    # y = x.sen(Θ) + y.cos(Θ)
    yR = []
    for i,y in enumerate(pontos_y):
        y = pontos_x[i] * math.sin(rad) + y * math.cos(rad)
        yR.append(y)


    x_final = []
    for i, x in enumerate(pts_x):
        # x =  centro_x - (centro_x - xR[i])
        x = centro_x - xR[i]

        x_final.append(x)


    y_final = []
    for i, y in enumerate(pts_y):
        # y = centro_y - (centro_y - yR[i])

        y = centro_y - yR[i]
        y_final.append(y)

 

    quad.set_xy(list(zip(x_final, y_final)))


def translacao(mv_x, mv_y, pontos_x, pontos_y):

  pts_xT = []
  for x in pontos_x:
    x = x + mv_x
    pts_xT.append(x)

  # translação em Y
  pts_yT = []
  for y in pontos_y:
    y = y + mv_y
    pts_yT.append(y)

  quad.set_xy(list(zip(pts_xT, pts_yT)))

def get_xy():

  pontos = quad.get_xy()

  x = list(pontos[:, 0])
  y = list(pontos[:, 1])

  return x, y


def on_close(event):
    exit()

def centro_quadrado(x, y):
    tam = len(x) # tamanho igual pra x e y
    tX = 0
    tY = 0
    for i in range(tam):
        tX += x[i]
        tY += y[i]

    centro_x = tX / tam
    centro_y = tY / tam

    return centro_x, centro_y



rad = -0.1
mv_x = 0.3
mv_y = -0.04

while True:
    x, y = get_xy()


    for vx in x:
        if vx <= 0.1 or vx >= (dim[0]- 0.1):
            mv_x *= -1
            rad *= -1

    for vy in y:
        if vy <= 0.1 or vy >= (dim[1] - 0.1):
            mv_y *= -1
            rad *= -1

    centro_x, centro_y = centro_quadrado(x, y)
    rotacao(rad, x, y, centro_x, centro_y)


    x, y = get_xy()

    translacao(mv_x, mv_y, x, y)

    cid = plt.connect('close_event', on_close)

    plt.draw()
    plt.pause(0.05)

