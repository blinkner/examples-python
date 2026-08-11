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

def Rz(tt):
    c= np.pi/180

    return np.array([[np.cos(tt*c), -np.sin(tt*c), 0],
                    [np.sin(tt*c),  np.cos(tt*c), 0],
                    [0,              0,           1]])

def Rx(tt):
    c= np.pi/180

    return np.array([[1,              0,           0],
                    [0,  np.cos(tt*c), -np.sin(tt*c)],
                    [0,  np.sin(tt*c),  np.cos(tt*c)]])

def Ry(tt):
    c= np.pi/180

    return np.array([[np.cos(tt*c), 0, np.sin(tt*c)],
                    [0, 1, 0],
                    [-np.sin(tt*c), 0, np.cos(tt*c)]])


def MTH2(matriz_desejada, matriz_dh, l):
    xc = matriz_desejada[0][3] - l[4]*matriz_desejada[0, 2]
    yc = matriz_desejada[1][3] - l[4]*matriz_desejada[1, 2]
    zc = matriz_desejada[2][3] - l[4]*matriz_desejada[2, 2]

    # c= np.pi/180
    r = np.sqrt(xc**2 + yc**2)
    s = zc - l[1]
    tt1 = np.arctan2(yc, xc)

    beta = np.arctan2(s, r)
    cos_gamma = (l[2]**2 - l[3]**2 + r**2 + s**2) / (2 * l[2] * np.sqrt(r**2 + s**2))
    sin_gamma = np.sqrt(1 - cos_gamma)
    gamma = np.arctan2(sin_gamma, cos_gamma)
    
    tt2 = 90 - (beta + gamma)

    sin_tt3 = (r**2 + s**2 - l[2]**2 - l[3]**2) / (2 * l[2] * l[3])
    cos_tt3 = np.sqrt(1 - sin_tt3)
    tt3 = np.arctan2(sin_tt3, cos_tt3)

    A = np.zeros((3, 1))

    for i in range(3):
        A[i] = np.block([[Rz(matriz_dh[i][0]), [0, 0, matriz_dh[i][1]]], [0, 0, 0, 1]]) @ np.block([[Rx(matriz_dh[i][3]), [matriz_dh[i][2]]], [0, 0, 0, 1]])

    H_3_0 = A[0] @ A[1] @ A[2]

    # E = np.array([[np.cos(tt4*c)*np.cos(tt5*c)*np.cos(tt6*c) - np.sin(tt4*c)*np.sin(tt6*c), -np.cos(tt4*c)*np.cos(tt5*c)*np.sin(tt6*c) - np.sin(tt4*c)*np.cos(tt6*c), np.cos(tt4*c)*np.sin(tt5*c)],
    #               [np.sin(tt4*c)*np.cos(tt5*c)*np.cos(tt6*c) + np.cos(tt4*c)*np.sin(tt6*c), -np.sin(tt4*c)*np.cos(tt5*c)*np.sin(tt6*c) + np.cos(tt4*c)*np.cos(tt6*c), np.sin(tt4*c)*np.sin(tt5*c)],
    #               [-np.sin(tt5*c)*np.cos(tt6*c), np.sin(tt5*c)*np.sin(tt6*c), np.cos(tt5*c)]])
    
    E = H_3_0 @ matriz_desejada

    cos_tt5 = E[2][2]
    sin_tt5 = np.sqrt(1 - cos_tt5)
    tt5 = np.arctan2(sin_tt5, cos_tt5)

    cos_tt4 = E[0][2] / sin_tt5
    sin_tt4 = E[1][2] / sin_tt5
    tt4 = np.arctan2(sin_tt4, cos_tt4)

    cos_tt6 = E[2][0] / (-sin_tt5)
    sin_tt6 = E[2][1] / sin_tt5
    tt6 = np.arctan2(sin_tt6, cos_tt6)

    return [tt1, tt2, tt3, tt4, tt5, tt6]




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

    # ax.invert_zaxis()                #Correção que tive que fazer pra câmera não ficar de ponta cabeça
    ax.view_init(elev=30, azim=45)
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')
    ax.set_title('Visualização do Braço Robótico')
    plt.legend()
    plt.show()


#===============Paramentros do Problema =========================================================
H0_6= np.array([[0.787, 0.079, 0.612, 0.53],
                [0.362, -0.862, -0.354, 0.18],
                [0.5, 0.5, -0.707, 0.22],
                [0, 0, 0, 1]])

l1= 0.2
l2= 0.3
l3= 0.4
l4= 0.3
l5= 0.1

Tipo= 'BF-CC'   #Braço frente | cotovelo cima

#=== Desacoplamento Cinemático====

R= H0_6[:3, :3]
O = H0_6[:3, 3].reshape(-1, 1)

Z_dir= np.array([[0],
                 [0],
                 [1]])


Oc= O - l5*(R @ Z_dir) #Origem do ponto C de desacoplamento
xc, yc, zc= Oc


#Parametros auxiliares para calculos posterriores
orintacao_braco, orientacao_cotovelo = Tipo.split('-')

rc = np.sqrt(xc**2 + yc**2) if orintacao_braco == 'BF' else -np.sqrt(xc**2 + yc**2)
s = zc - l2
h = np.sqrt((rc)**2 + (s)**2) # Hipotenusa do triângulo do braço

coss_alpha= (l3**2 + h**2 - l4**2)/(2*l3*h)
coss_alpha = np.clip(coss_alpha, -1, 1) # Evita erro numérico fora de [-1, 1]
sen_alpha= np.sqrt(1 - coss_alpha**2) if orientacao_cotovelo == 'CC' else -np.sqrt(1 - coss_alpha**2)

cos_tt3= (-l3**2 + h**2 - l4**2)/(2*l3*l4)
sen_tt3= np.sqrt(1 - cos_tt3**2) if orientacao_cotovelo == 'CC' else -np.sqrt(1 - cos_tt3**2)


#============Inversa de Posição=============
tt1= np.arctan2(yc, xc)  #θ1

tt2= np.arctan2(s, rc) - np.arctan2(coss_alpha, sen_alpha) #θ2

tt3= np.arctan2(cos_tt3, sen_tt3) #θ3


#============Inversa de Orientação=============

cos_tt5= np.sin(tt1)*R[0,2] - np.cos(tt1)*R[1,2]
sen_tt5= np.sqrt(1 - cos_tt5**2)                #TALVES TENHA QUE MUDAR O SINAL

tt5= np.arctan2(cos_tt5, sen_tt5) #θ5


cos_tt4= (np.cos(tt1)*np.cos(tt2-tt3)*R[0,2] + np.sin(tt1)*np.cos(tt2-tt3)*R[1,2] - np.sin(tt2-tt3)*R[2,2])/np.sin(tt5)
sen_tt4= (np.cos(tt1)*np.sin(tt2-tt3)*R[0,2] + np.sin(tt1)*np.sin(tt2-tt3)*R[1,2] + np.cos(tt2-tt3)*R[2,2])/np.sin(tt5)

tt4= np.arctan2(cos_tt4, sen_tt4) #θ4

cos_tt6= (-np.sin(tt1)*R[0,0] + np.cos(tt1)*R[1,0])/ np.sin(tt5)
sen_tt6= (np.sin(tt1)*R[0,1] - np.cos(tt1)*R[1,1])/ np.sin(tt5)

tt6= np.arctan2(cos_tt6, sen_tt6) #θ6

angulo_rad=[tt1, tt2, tt3, tt4, tt5, tt6]
tt1, tt2, tt3, tt4, tt5, tt6 = np.degrees(angulo_rad)


#Matrizes de transformação Ai
A1= MTH(tt1[0], l2, l1, -90)
A2= MTH(tt2[0]-90, 0, l3, 180)
A3= MTH(tt3[0], 0, 0, 90)


# Expondo os Resultados:
T1 = A1
T2 = A1 @ A2
T3 = A1 @ A2 @ A3


print(f'T6= \n{T6}')
plot_robo([T1, T2, T3, T4, T5, T6])