import matplotlib.pyplot as plt
# Definindo os limites dos eixos
dim = [500, 500]
plt.xlim(0, dim[0])
plt.ylim(0, dim[1])
# Mantendo a proporção dos eixos
plt.gca().set_aspect('equal', adjustable='box')



# ========================================== 1 =================================================
plt.axhline((dim[0] / 2), color='b', linestyle='-')
plt.axvline((dim[1] / 2), color='r', linestyle='-')

# ========================================== 2 =================================================

circulo = plt.Circle((dim[0]/2, dim[1]/2), 50, fill=False, color='g')
plt.gca().add_artist(circulo)

# ========================================== 3 =================================================
circulo = plt.Circle((0, dim[1]), 100, fill=True, color='yellow')
plt.gca().add_artist(circulo)

# ========================================== 4 =================================================

                      #X        #Y
centro_quadrande_1 = ((dim[0] / 2) / 2), (((dim[1] / 2) / 2) + dim[1] / 2)

x = [centro_quadrande_1[0] - 50, # ponto 1 (inferior esquerdo)
     centro_quadrande_1[0] - 50, # ponto 2 (superior esquerdo)
     centro_quadrande_1[0] + 50, # ponto 3 (superior direito)
     centro_quadrande_1[0] + 50, # ponto 4 (inferior direito)
     centro_quadrande_1[0] - 50] # ligação final


y = [centro_quadrande_1[1] - 50, # ponto 1 (inferior esquerdo)
     centro_quadrande_1[1] + 50, # ponto 2 (superior esquerdo)
     centro_quadrande_1[1] + 50, # ponto 3 (superior direito)
     centro_quadrande_1[1] - 50, # ponto 4 (inferior direito)
     centro_quadrande_1[1] - 50] # ligação final

plt.plot(x, y, color="pink")

# ========================================== 5 =================================================

centro_quadrande_3 = (((dim[0] / 2) / 2) + dim[0] / 2), ((dim[1] / 2) / 2)

# circulo = plt.Circle(centro_quadrande_3, 5, fill=True, color='yellow')
# plt.gca().add_artist(circulo)

x = [centro_quadrande_3[0] - 75, # ponto 1 (inferior esquerdo)
     centro_quadrande_3[0] - 75, # ponto 2 (superior esquerdo)
     centro_quadrande_3[0] + 75, # ponto 3 (superior direito)
     centro_quadrande_3[0] + 75, # ponto 4 (inferior direito)
     centro_quadrande_3[0] - 75] # ligação final


y = [centro_quadrande_3[1] - 75, # ponto 1 (inferior esquerdo)
     centro_quadrande_3[1] + 75, # ponto 2 (superior esquerdo)
     centro_quadrande_3[1] + 75, # ponto 3 (superior direito)
     centro_quadrande_3[1] - 75, # ponto 4 (inferior direito)
     centro_quadrande_3[1] - 75] # ligação final

plt.plot(x, y, color="orange")

# ========================================== 6 =================================================

x1 = (0, dim[0])
y1 = (dim[1], 0)

plt.plot(x1,y1, color="cyan")

x2 = (0, dim[0])
y2 = (0, dim[1])

plt.plot(x2,y2, color="cyan")

# ========================================== 7 =================================================

circulo = plt.Circle((dim[0]/ 2, dim[1]/2), 150, fill=False, color='purple')
plt.gca().add_artist(circulo)


###################################
# Mostrando o gráfico
plt.show()