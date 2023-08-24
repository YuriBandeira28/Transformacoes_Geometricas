import matplotlib.pyplot as plt

# Definindo os limites dos eixos
dim = [3, 3]
plt.xlim(0, dim[0])
plt.ylim(0, dim[1])
# Mantendo a proporção dos eixos
plt.gca().set_aspect('equal', adjustable='box')


# ================== ORIGINAL ======================

pts_x = [1 - 0.3,
         1 + 0.3,
         1 + 0.5,
         1,
         1 - 0.5
         ]


pts_y = [1 - 0.5,
         1 - 0.5,
         1,
         1 + 0.3,
         1]

pentagono = plt.Polygon([[pts_x[0], pts_y[0]],
                    [pts_x[1], pts_y[1]],
                    [pts_x[2], pts_y[2]],
                    [pts_x[3], pts_y[3]],
                    [pts_x[4], pts_y[4]]],
                    closed=True,
                    fill = False,
                    edgecolor='red',
                    label = "Original")

plt.gca().add_patch(pentagono)

# ================== escalonado ======================

# formula
# x’ = x • Sx
# y’= y • Sy

xE = []
for x in pts_x:
  x = x * 2
  xE.append(x)


yE = []
for y in pts_y:
  y = y * 0.5
  yE.append(y)


pentagonoE = plt.Polygon([[xE[0], yE[0]],
                          [xE[1], yE[1]],
                          [xE[2], yE[2]],
                          [xE[3], yE[3]],
                          [xE[4], yE[4]]],
                          closed=True,
                          fill = False,
                          edgecolor='blue',
                          label = "Escalonado")

plt.gca().add_patch(pentagonoE)

plt.legend()
plt.show()