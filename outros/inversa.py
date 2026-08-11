import numpy as np

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


def orientacao(matriz_desejada, matriz_dh):
    A1 = np.block([[Rz(matriz_dh[0][0]), np.array([[0], [0], [matriz_dh[0][1]]])], [np.array([[0, 0, 0, 1]])]]) @ np.block([[Rx(matriz_dh[0][3]), np.array([[matriz_dh[0][2]], [0], [0]])], [np.array([[0, 0, 0, 1]])]])
    A2 = np.block([[Rz(matriz_dh[1][0]), np.array([[0], [0], [matriz_dh[1][1]]])], [np.array([[0, 0, 0, 1]])]]) @ np.block([[Rx(matriz_dh[1][3]), np.array([[matriz_dh[1][2]], [0], [0]])], [np.array([[0, 0, 0, 1]])]])
    A3 = np.block([[Rz(matriz_dh[2][0]), np.array([[0], [0], [matriz_dh[2][1]]])], [np.array([[0, 0, 0, 1]])]]) @ np.block([[Rx(matriz_dh[2][3]), np.array([[matriz_dh[2][2]], [0], [0]])], [np.array([[0, 0, 0, 1]])]])

    H_3_0 = A1 @ A2 @ A3
    
    E = np.transpose(H_3_0[0:3,0:3]) @ matriz_desejada[0:3,0:3]

    cos_tt5 = E[2][2]
    sin_tt5 = np.sqrt(1 - cos_tt5**2)
    tt5 = np.arctan2(sin_tt5, cos_tt5)

    cos_tt4 = E[0][2] / sin_tt5
    sin_tt4 = E[1][2] / sin_tt5
    tt4 = np.arctan2(sin_tt4, cos_tt4)

    cos_tt6 = E[2][0] / (-sin_tt5)
    sin_tt6 = E[2][1] / sin_tt5
    tt6 = np.arctan2(sin_tt6, cos_tt6)

    c= 180/np.pi

    # T_6_3 = np.array([[l[4] * matriz_desejada[0][2]], [l[4] * matriz_desejada[1][2]], [l[4] * matriz_desejada[2][2]]])
    T_6_3 = np.array([[0], [0], [l[4]]])

    A4 = np.block([[Rz(tt4*c) @ Ry(tt5*c) @ Rz(tt6*c), np.zeros((3,1))], [np.zeros((1,3)), 1]])
    A5 = np.block([[np.eye(3), T_6_3], [np.array([[0, 0, 0, 1]])]])

    H = H_3_0 @ A4 @ A5

    print(H)
    return [tt1*c, tt2*c, tt3*c, tt4*c, tt5*c, tt6*c]

c = np.pi / 180

l = [0.2, 0.3, 0.4, 0.3, 0.1]
H_6_0 = np.array([[0.787, 0.079, 0.612, 0.53],
                  [0.362, -0.862, -0.354, 0.18],
                  [0.5, 0.5, -0.707, 0.22],
                  [0, 0, 0, 1]])


xc = H_6_0[0][3] - l[4]*H_6_0[0, 2]
yc = H_6_0[1][3] - l[4]*H_6_0[1, 2]
zc = H_6_0[2][3] - l[4]*H_6_0[2, 2]

r = np.sqrt(xc**2 + yc**2)
r = r - l[0]
s = zc - l[1]
tt1 = np.arctan2(yc, xc)

beta = np.arctan2(s, r)
cos_gamma = (l[2]**2 - l[3]**2 + r**2 + s**2) / (2 * l[2] * np.sqrt(r**2 + s**2))
sin_gamma = np.sqrt(1 - cos_gamma**2)
gamma = np.arctan2(sin_gamma, cos_gamma)

tt2 = np.pi/2 - (beta + gamma)

sin_tt3 = (r**2 + s**2 - l[2]**2 - l[3]**2) / (2 * l[2] * l[3])
cos_tt3 = np.sqrt(1 - sin_tt3**2)
tt3 = np.arctan2(sin_tt3, cos_tt3)

matriz_dh = np.array([[tt1*180/np.pi, l[1], l[0], -90],
                      [tt2*180/np.pi - 90, 0, l[2], 180],
                      [tt3*180/np.pi - 90, 0, l[3], 0]])

print(f"theta = {orientacao(H_6_0, matriz_dh)}")