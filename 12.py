import matplotlib.pyplot as plt
import math

# Definindo os limites dos eixos
dim = [6, 6]
plt.xlim(0, dim[0])
plt.ylim(0, dim[1])
# Mantendo a proporção dos eixos
plt.gca().set_aspect('equal', adjustable='box')

# centro_pos = (dim[0] / 2, dim[1] / 2)

pts_x = [1, 2, 2, 1, 1]

pts_y = [1, 1, 2, 2, 1]


quad = plt.Polygon([[pts_x[0], pts_y[0]],
                    [pts_x[1], pts_y[1]],
                    [pts_x[2], pts_y[2]],
                    [pts_x[3], pts_y[3]]],
                          closed=True,
                          fill = False,
                          edgecolor='blue',
                          color='blue',
                          label = "Original")

plt.gca().add_patch(quad)


# rotação da origem
# # m over o quadrado para a origem
# xO = []
# for x in pts_x:
#   x = x - 1
#   xO.append(x)


# yO = []
# for y in pts_y:
#   y = y - 1
#   yO.append(y)

rad = math.radians(30)

# x = x.cos(Θ) - y.sen(Θ)
xR = []
for i, x in enumerate(pts_x):
  x = x * math.cos(rad) - pts_y[i] * math.sin(rad)
  xR.append(x)


# y = x.sen(Θ) + y.cos(Θ)
yR = []
for i,y in enumerate(pts_y):
  y = pts_x[i] * math.sin(rad) + y * math.cos(rad)
  yR.append(y)


# escalona ele
#pts =(+3x, +2y)

xRE = []
for x in xR:
  x = x + 3
  xRE.append(x)

yRE = []
for y in yR:
  y = y + 2
  yRE.append(y)

quadRE = plt.Polygon([[xRE[0], yRE[0]],
                      [xRE[1], yRE[1]],
                      [xRE[2], yRE[2]],
                      [xRE[3], yRE[3]]],
                          closed=True,
                          fill = False,
                          edgecolor='red',
                          color='red',
                          label = "Rotacionado e Escalonado")


plt.gca().add_patch(quadRE)

plt.legend()
plt.show()