import matplotlib.pyplot as plt
# Definindo os limites dos eixos
dim = [400, 300]
plt.xlim(0, dim[0])
plt.ylim(0, dim[1])
# Mantendo a proporção dos eixos
plt.gca().set_aspect('equal', adjustable='box')


# ================== triangulo original ===========================

pts_x = [100, 200, 150, 100]
pts_y = [100, 100, 200, 100]

plt.plot(pts_x, pts_y, color="blue", label="Orignal")

# ============================== formula translação =======================

# x’ = x + dx
# Y’ = y + dy


# ================== triangulo transladado ===========================
# translação em X
pts_xT = []
for x in pts_x:
  x = x + 100 # + 100 unidades pra direito (+100X)
  pts_xT.append(x)

# translação em Y
pts_yT = []
for y in pts_y:
  y = y + 50 # + 50 unnidades para cima (+50Y)
  pts_yT.append(y)

plt.plot(pts_xT, pts_yT, color="red", label="Transladado")


plt.legend()
plt.show()