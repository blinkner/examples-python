import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.set_printoptions(precision=4, suppress=True)

#Função que Monta as MTH dos frames
def MTH(tt_i, d_i, a_i, alfa_i):
    c= np.pi/180 #fatorzinho de correção pra transformar de graus pra rad

    # Rotações
    Rz = np.array([[np.cos(tt_i*c), -np.sin(tt_i*c), 0],
                   [np.sin(tt_i*c),  np.cos(tt_i*c), 0],
                   [0,              0,           1]])
    
    Rx = np.array([[1,              0,           0],
                   [0,  np.cos(alfa_i*c), -np.sin(alfa_i*c)],
                   [0,  np.sin(alfa_i*c),  np.cos(alfa_i*c)]])
    

    d = np.array([[0],[0],[d_i]])
    a = np.array([[a_i],[0],[0]])

    # Linha inferior (já como matriz 1x4 para o np.block)
    f = np.array([[0, 0, 0, 1]])

    # Montando e multiplicando as sub-transformações
    T_z = np.block([[Rz, d], [f]])
    T_x = np.block([[Rx, a], [f]])

    return T_z @ T_x



#===============================Função para uma rustica exibição do diagrama de arame=============================
def plot_robo(matrizes_acumuladas):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 1. Extração das coordenadas das origens (x, y, z)
    # Começamos pela origem da base [0, 0, 0]
    xs, ys, zs = [0], [0], [0]
    
    for T in matrizes_acumuladas:
        posicao = T[:3, 3]
        xs.append(posicao[0])
        ys.append(posicao[1])
        zs.append(posicao[2])
        
        # 2. Desenhar os eixos de cada frame (X=R, Y=G, Z=B)
        for i, cor in enumerate(['r', 'g', 'b']):
            eixo = T[:3, i]
            ax.quiver(posicao[0], posicao[1], posicao[2], 
                      eixo[0], eixo[1], eixo[2], 
                      color=cor, length=0.1, normalize=True, arrow_length_ratio=0.3)

    # 3. Desenha os elos (Diagrama de Arame)
    ax.plot(xs, ys, zs, 'o-', linewidth=4, markersize=8, color='black', label='Estrutura')

    # 4. Lógica de enquadramento automático (Câmera e Eixos)
    z_medio = np.mean(zs)
    max_range = np.max(np.abs([xs, ys, zs])) # Escala global para manter o cubo
    
    if z_medio < 0:
        # Caso o robô esteja no semi-espaço negativo de Z
        ax.set_zlim(-max_range * 1.1, max_range * 0.1)
        ax.view_init(elev=-20, azim=45) # Inclina a câmera para olhar o quadrante inferior
    else:
        # Caso o robô esteja no semi-espaço positivo (padrão)
        ax.set_zlim(-max_range * 0.1, max_range * 1.1)
        ax.view_init(elev=20, azim=45)

    # Mantém X e Y centralizados e escala 1:1:1
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    
    # Força a caixa de exibição a ser um cubo perfeito (evita esticamento)
    ax.set_box_aspect([1,1,1]) 

    ax.invert_zaxis()                #Correção que tive que fazer pra câmera não ficar de ponta cabeça
    ax.view_init(elev=30, azim=45)
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')
    ax.set_title('Visualização do Braço Robótico')
    plt.legend()
    plt.show()




#============================= Utilizando o Software KKK ====================================

#Parametros do Problema (l -> comprimeito do link | tt -> angulo theta)
l1= 0.6
l2= 0.5
l3= 0.2

tt1= 70.9137
tt2= -50.7424
tt3= -65.1713

#Matrizes de transformação Ai
A1= MTH(tt1, 0, l1, 0)
A2= MTH(tt2, 0, l2, 0)
A3= MTH(tt3, 0, l3, 0)

# Expondo os Resultados:
T1 = A1
T2 = A1 @ A2
T3 = A1 @ A2 @ A3

print(f'T3= {T3}')

plot_robo([T1, T2, T3])
