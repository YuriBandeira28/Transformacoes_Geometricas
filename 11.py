import matplotlib.pyplot as plt

# Definindo os limites dos eixos
dim = [100, 100]
plt.xlim(-dim[0], dim[0])
plt.ylim(-dim[1], dim[1])
# Mantendo a proporção dos eixos
plt.gca().set_aspect('equal', adjustable='box')


plt.axhline(0, color='black', linestyle='--')
plt.axvline(0, color='black', linestyle='--')

centro_pos = (dim[0] / 2, dim[1] / 2)

pts_x = [centro_pos[0] - 25,
         centro_pos[0] + 30,
         centro_pos[0] - 25]

pts_y = [centro_pos[1] - 25,
         centro_pos[1] - 25,
         centro_pos[1] + 10]


triangulo = plt.Polygon([[pts_x[0], pts_y[0]],
                           [pts_x[1], pts_y[1]],
                           [pts_x[2], pts_y[2]]],
                          closed=True,
                          fill = True,
                          edgecolor='blue',
                          color='blue',
                          label = "Original")

plt.gca().add_patch(triangulo)


# espelhado no eixo X
xRX = []
for x in pts_x:
  x = -x
  xRX.append(x)

triangulo_eX = plt.Polygon([[xRX[0], pts_y[0]],
                           [xRX[1], pts_y[1]],
                           [xRX[2], pts_y[2]]],
                          closed=True,
                          fill = True,
                          edgecolor='red',
                          color='red',
                          label = "Espelhado no Eixo X")
plt.gca().add_patch(triangulo_eX)


# espelhado no eixo Y
yRY = []
for y in pts_y:
  y = -y
  yRY.append(y)

triangulo_eY = plt.Polygon([[pts_x[0], yRY[0]],
                            [pts_x[1], yRY[1]],
                            [pts_x[2], yRY[2]]],
                          closed=True,
                          fill = True,
                          color = 'green',
                          edgecolor='green',
                          label = "Espelhado no Eixo Y")

plt.gca().add_patch(triangulo_eY)



plt.legend()
plt.show()