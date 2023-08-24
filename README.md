# Transoformações Geométricas

Exercícios realizados para matéria de Computação Gráfica

# Enunciados:

## 1 a 7

1. Acrescente uma linha na cor azul cortando toda a janela ao meio na horizontal e uma na cor
vermelha cortando toda a janela ao meio na vertical.
2. Coloque um círculo sem preenchimento, de raio 50, com a origem no encontro das linhas
desenhadas, no centro da janela.
3. Crie um segundo círculo, preenchido de amarelo, de raio 100, com o seu centro no canto superior
esquerdo da janela.
4. Construa um quadrado rosa de lado 100, exatamente no centro do primeiro quadrante (lado
superior esquerdo).
5. Construa um segundo quadrado laranja de lado 150, exatamente no centro do terceiro quadrante
(lado inferior direito).
6. Trace duas linhas em ciano na diagonal, formando um X, indo de um extremo ao outro da janela.
7. Desenhe um círculo sem preenchimento com raio 180 e centro no meio da janela.

## 8

TRANSLAÇÃO: Crie um programa que gere uma área de 400x300 e desenhe um triângulo com os
seguintes vértices: p1(100, 100), p2(200, 100) e p3(150, 200) - use obrigatoriamente a plt.plot( ).
Após isso translade o triângulo 100 unidades à direita e 50 unidades para cima utilizando as fórmulas
vistas em aula. Utilize a Matplotlib para visualizar o triângulo original e o transladado na mesma área,
com cores diferentes.

## 9

ROTAÇÃO: Crie um programa que que gere uma área de 3x3 e desenhe um quadrado de lado 1 no
meio - use obrigatoriamente a plt.plot( ). Após isso, rotacione o quadrado 45 graus em torno de seu
centro (não em torno da origem do plano). Utilize a Matplotlib para visualizar o quadrado original e o
rotacionado na mesma área, com cores diferentes.

# 10

ESCALONAMENTO: Crie um programa que desenhe um pentágono (use a classe Polygon) e o
escale em 2 vezes no eixo X e 0.5 vezes no eixo Y. Utilize a Matplotlib para visualizar o pentágono
original e o escalonado em cores diferentes. Gere a área de exibição de forma que os dois
pentágonos sejam visíveis simultaneamente.

# 11

REFLEXÃO: Crie um programa que desenhe um triângulo retângulo (use a classe Polygon) e o
reflita em torno do eixos Y e X (separadamente). Utilize a Matplotlib para visualizar simultaneamente o
triângulo original e os dois refletidos, todos em cores diferentes.

# 12

COMPOSIÇÃO DE TRANSFORMAÇÕES: Crie um programa que gere uma área de 6x6 e desenhe
um quadrado de lado 1 (use a classe Polygon) com o canto inferior esquerdo no ponto p(1, 1).
Aplique sobre esse quadrado uma rotação de 30 graus seguida de uma translação de 3 unidades à
direita e 2 unidades para cima. Utilize a Matplotlib para visualizar o quadrado original e o
transformado em cores diferentes.

# 13

TRANSLAÇÃO e interação: Crie um programa que gere uma área de 3.0x4.5 e desenhe um
quadrado de lado 0.5 com o canto inferior esquerdo no ponto p(0.0, 1.5) - use obrigatoriamente a
classe Rectangle. O quadrado deve ser preenchido de cor laranja, com a borda preta. Após isso
acrescente um objeto Slider (posicione-o adequadamente) acoplado a uma função que atualize a
translação do quadrado em X, movimentando o quadrado entre os extremos horizontais da área (de 0
até 3).

# 14

TRANSLAÇÃO, ROTAÇÃO, ANIMAÇÃO e COLISÕES: Desenvolva um programa em Python
utilizando a biblioteca Matplotlib para simular um quadrado que rotaciona em torno de seu próprio
centro e se move dentro de uma área de plotagem, invertendo o sentido do movimento ao colidir com
os limites da área, como se fosse uma bola quicando.
Requisitos:
- Área de Plotagem: Crie uma área de plotagem de tamanho 5x5. Os limites devem ser claramente
definidos, e o aspecto do gráfico deve ser igual.
- Quadrado: Desenhe um quadrado de lado 1 com o canto inferior esquerdo no ponto (1,1). Utilize a
classe Polygon da Matplotlib.
- Rotação: Faça o quadrado rotacionar continuamente em torno de seu próprio centro. A rotação
deve ser realizada sem o uso de bibliotecas específicas, exceto a biblioteca math, que pode ser
utilizada para cálculo de seno, cosseno e conversão de graus em radianos.
- Movimentação: Faça o quadrado se mover em linha reta pela área de plotagem. Ao colidir com os
limites da área, o quadrado deve inverter o sentido do movimento, como se estivesse quicando.
- Controle de Colisões: Implemente um controle preciso de colisões para evitar que o quadrado
ultrapasse os limites da área de plotagem.
- Animação: Utilize um loop para atualizar o gráfico e criar a animação do quadrado rotacionando e
se movendo. Não pode ser utilizada a biblioteca animation da Matplotlib.