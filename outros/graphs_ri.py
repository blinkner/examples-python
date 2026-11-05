import matplotlib.pyplot as plt
import numpy as np

# Gráficos da Questão 3.c da Atividade01.02 de Robótica Industrial
t = np.linspace(0, 6, 90)
q = - 10 - 3.704*t**3 + 0.926*t**4 - 0.062*t**5
q_dot = - 11.112*t**2 + 3.704*t**3 - 0.31*t**4
q_ddot = - 22.224*t + 11.112*t**2 - 1.24*t**3

plt.figure(1)
plt.plot(t, q, 'k', linewidth=2)
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (º)")
plt.grid()
plt.show(block=False)

plt.figure(2)
plt.plot(t, q_dot, 'k', linewidth=2)
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (º/s)")
plt.grid()
plt.show(block=False)

plt.figure(3)
plt.plot(t, q_ddot, 'k', linewidth=2)
plt.xlabel("Tempo (s)")
plt.ylabel("Aceleração ($º/s^2$)")
plt.grid()
plt.show()

# Gráficos da Questão 5.b da Atividade01.02 de Robótica Industrial
t = np.linspace(0, 8, 90)

# Trajetória cúbica
q = 1.875*t**2 - 0.156*t**3
q_dot = 3.75*t - 0.468*t**2
q_ddot = 3.75 - 0.936*t

plt.figure(1)
plt.plot(t, q, 'k', linewidth=2)
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (º)")
plt.grid()
plt.show(block=False)

plt.figure(2)
plt.plot(t, q_dot, 'k', linewidth=2)
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (º/s)")
plt.grid()
plt.show(block=False)

plt.figure(3)
plt.plot(t, q_ddot, 'k', linewidth=2)
plt.xlabel("Tempo (s)")
plt.ylabel("Aceleração ($º/s^2$)")
plt.grid()
plt.show()

# Trajetória LSPB
t1 = np.linspace(0, 2, 30)
t2 = np.linspace(2, 6, 30)
t3 = np.linspace(6, 8, 30)

plt.figure(1)
plt.plot(t1, 2.5*t1**2, 'k', linewidth=2)
plt.plot(t2, -10 + 10*t2, 'k', linewidth=2)
plt.plot(t3, -100 + 40*t3 - 2.5*t3**2, 'k', linewidth=2)
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (º)")
plt.grid()
plt.show(block=False)

plt.figure(2)
plt.plot(t1, 5*t1, 'k', linewidth=2)
plt.plot(t2, np.ones(len(t2))*10, 'k', linewidth=2)
plt.plot(t3, 40 - 5*t3, 'k', linewidth=2)
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (º/s)")
plt.grid()
plt.show(block=False)

plt.figure(3)
plt.plot(t1, np.ones(len(t1))*5, 'k', linewidth=2)
plt.plot(t2, np.zeros(len(t2)), 'k', linewidth=2)
plt.plot(t3, np.ones(len(t3))*-5, 'k', linewidth=2)
plt.vlines(x=2, ymin=0, ymax=5, color='k', linestyle='--')
plt.vlines(x=6, ymin=-5, ymax=0, color='k', linestyle='--')
plt.xlabel("Tempo (s)")
plt.ylabel("Aceleração ($º/s^2$)")
plt.grid()
plt.show()