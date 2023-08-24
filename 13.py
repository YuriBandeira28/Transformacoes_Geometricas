import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Slider


# Definindo os limites dos eixos
dim = [3.0, 4.5]
plt.xlim(0, dim[0])
plt.ylim(0, dim[1])
# Mantendo a proporção dos eixos
plt.gca().set_aspect('equal', adjustable='box')


#parametros (x, y), altura, largura
quad = patches.Rectangle((0.0, 1.5),
                        0.5, 0.5,
                        linewidth=1, edgecolor='black', facecolor='orange')

plt.gca().add_patch(quad)
                    # x , y , largura, altura
ax_slider = plt.axes([0.3, 0.1, 0.4, 0.03])
slider = Slider(ax_slider, 'X', 0.0, 2.486, valinit=0)


plt.subplots_adjust(bottom=0.2)  # Ajuste da posição dos controles

def upd_slider(val):
  dx = slider.val
  quad.set_x(dx) # Atualizando a posição x do quadrado
  plt.draw()


slider.on_changed(upd_slider)

plt.show()