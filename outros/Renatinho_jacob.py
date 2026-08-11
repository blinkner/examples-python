import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


np.set_printoptions(precision=3, suppress=True)

#Matrizes de Rotação X, Y e Z
def T(x,y,z):
    return np.array([[1, 0, 0, x],
                    [0, 1, 0, y],
                    [0, 0, 1, z],
                    [0, 0, 0, 1]])

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
def plot_robo(matrizes_acumuladas, Tipo):
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
    ax.view_init(elev=20, azim=70)   #30, 45
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')
    ax.set_title(f'Solução: {Tipo}')
    plt.legend()
    plt.show()


#===============Paramentros do Problema =========================================================

Tipo= 'BF-CC'   #Braço Frente ou Trás | Cotovelo Cima ou Baixo | Punho Cima ou Baixo

l1= 70
l2= 30
l3= 70
l4= 60


#=== Desacoplamento Cinemático====
xc, yc, zc= [100, 0, 50]


#Parametros auxiliares para calculos posterriores
orintacao_braco, orientacao_cotovelo= Tipo.split('-')

rc = np.sqrt(xc**2 + yc**2) if orintacao_braco == 'BF' else -np.sqrt(xc**2 + yc**2)
r= rc- l2
s= zc- l1
h = np.sqrt(r**2 + s**2) 


cos_tt3= (h**2- l3**2- l4**2)/(2*l3*l4)
sen_tt3= np.sqrt(1 - cos_tt3**2) if orientacao_cotovelo == 'CC' else -np.sqrt(1 - cos_tt3**2)

beta=  np.arctan2(s, r)
cos_alpha= (l3**2 + h**2 - l4**2)/(2*l3*h)
sen_alpha= np.sqrt(1 - cos_alpha**2) if orientacao_cotovelo == 'CC' else -np.sqrt(1 - cos_alpha**2)

#============Inversa de Posição=============
tt1= np.arctan2(yc, xc)  #θ1  check
tt2= beta + np.arctan2(sen_alpha, cos_alpha) #θ2 
tt3= np.arctan2(sen_tt3, cos_tt3)

tt1, tt2, tt3= np.degrees([tt1, tt2, tt3])
# tt1= tt1[
# tt2= tt2[0]
# tt3= tt3[0]

#Matrizes de transformação Ai para posição 
A1= MTH(tt1, l1, l2, 90)
A2= MTH(tt2, 0, l3, 180)
A3= MTH(tt3, 0, l4, 0)


#====================================================

# Expondo os Resultados:
T1 = A1
T2 = A1 @ A2
T3 = A1 @ A2 @ A3


print(f'T3= \n{T3}')
print(f'Angulos: {tt1, tt2, tt3}')
plot_robo([T1, T2, T3], Tipo)


#====================== Jacobiano ==============================
tt1 = tt1 * np.pi/180
tt2 = tt2 * np.pi/180
tt3 = tt3 * np.pi/180

Jv  = np.array([[-l2*np.sin(tt1) - l3*np.sin(tt1)*np.cos(tt2)- l4*np.sin(tt1)*np.cos(tt2-tt3),   -l3*np.cos(tt1)*np.sin(tt2)- l4*np.cos(tt1)*np.sin(tt2-tt3),   l4*np.cos(tt1)*np.sin(tt2-tt3)],
                [l2*np.cos(tt1)+ l3*np.cos(tt1)*np.cos(tt2)+ l4*np.cos(tt1)*np.cos(tt2-tt3),     -l3*np.sin(tt1)*np.sin(tt2)- l4*np.sin(tt1)*np.sin(tt2-tt3),   l4*np.sin(tt1)*np.sin(tt2-tt3)],
                [                                0,                                                         l3*np.cos(tt2)+ l4*np.cos(tt2-tt3),                     -l4*np.cos(tt2-tt3)       ]])
 
v = 5
dx, dy, dz = [10, 10, 5]
d = np.sqrt(dx**2 + dy**2 + dz**2)

vx = (dx/d) * v
vy = (dy/d) * v
vz = (dz/d) * v

epsilon= np.array([[vx], [vy], [vz]])

q_dot = np.linalg.inv(Jv) @ epsilon
print(epsilon)
print(q_dot)