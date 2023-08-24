import matplotlib.pyplot as plt
import math
# Definindo os limites dos eixos
dim = [4, 3]
plt.xlim(0, dim[0])
plt.ylim(0, dim[1])
# Mantendo a proporção dos eixos
plt.gca().set_aspect('equal', adjustable='box')




centro = (dim[0] / 2, dim[1] / 2)

pts_x = [centro[0] - 0.5, # ponto 1 (inferior esquerdo)
     centro[0] - 0.5, # ponto 2 (superior esquerdo)
     centro[0] + 0.5, # ponto 3 (superior direito)
     centro[0] + 0.5, # ponto 4 (inferior direito)
     centro[0] - 0.5] # ligação final


pts_y = [centro[1] - 0.5, # ponto 1 (inferior esquerdo)
     centro[1] + 0.5, # ponto 2 (superior esquerdo)
     centro[1] + 0.5, # ponto 3 (superior direito)
     centro[1] - 0.5, # ponto 4 (inferior direito)
     centro[1] - 0.5] # ligação final

plt.plot(pts_x, pts_y, color='blue', label="Original")

# formula rotação



# quadrado rotacionado
rad = math.radians(45)

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



plt.plot(xR,yR, color='red', label="Rotacionado")


plt.legend()
plt.show()
