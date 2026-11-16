import numpy as np
import heapq
import math
import matplotlib.pyplot as plt

def heuristica(a, b):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])

    return max(dx, dy) + (math.sqrt(2) - 1) * min(dx, dy)


def obter_vizinhos(posicao, mapa):
    movimentos = [
        (-1, 0, 1),   # Cima
        (1, 0, 1),    # Baixo
        (0, -1, 1),   # Esquerda
        (0, 1, 1),    # Direita
        (-1, -1, math.sqrt(2)),
        (-1, 1, math.sqrt(2)),
        (1, -1, math.sqrt(2)),
        (1, 1, math.sqrt(2))
    ]

    vizinhos = []

    linhas, colunas = mapa.shape
    x, y = posicao

    for dx, dy, custo in movimentos:
        nx = x + dx
        ny = y + dy

        # Verifica os limites do mapa
        if not (0 <= nx < linhas and 0 <= ny < colunas):
            continue

        # Verifica se a posição está livre
        if mapa[nx, ny] != 0:
            continue

        # Impede atravessar diagonalmente entre dois obstáculos
        if dx != 0 and dy != 0:
            if mapa[x + dx, y] != 0 or mapa[x, y + dy] != 0:
                continue

        vizinhos.append(((nx, ny), custo))

    return vizinhos

def reconstruir_caminho(came_from, atual):
    caminho = [atual]

    while atual in came_from:
        atual = came_from[atual]
        caminho.append(atual)

    return caminho[::-1]

def astar(mapa, inicio, objetivo):
    linhas, colunas = mapa.shape

    # Validação das posições
    for posicao in [inicio, objetivo]:

        x, y = posicao

        if not (0 <= x < linhas and 0 <= y < colunas):
            raise ValueError("Posição fora dos limites do mapa")

        if mapa[x, y] != 0:
            raise ValueError("Início ou objetivo em um obstáculo")

    # Fila de prioridade
    open_set = []

    heapq.heappush(
        open_set,
        (heuristica(inicio, objetivo), inicio)
    )

    # Predecessores
    came_from = {}

    # Custo acumulado
    g_score = {inicio: 0}

    # Nós já explorados
    closed_set = set()

    while open_set:

        _, atual = heapq.heappop(open_set)

        if atual in closed_set:
            continue

        # Objetivo encontrado
        if atual == objetivo:
            return reconstruir_caminho(came_from, atual)

        closed_set.add(atual)

        # Explora os vizinhos
        for vizinho, custo_movimento in obter_vizinhos(atual, mapa):

            if vizinho in closed_set:
                continue

            custo_tentativo = (
                g_score[atual] + custo_movimento
            )

            if custo_tentativo < g_score.get(vizinho, float("inf")):
                came_from[vizinho] = atual
                g_score[vizinho] = custo_tentativo

                f_score = (
                    custo_tentativo +
                    heuristica(vizinho, objetivo)
                )

                heapq.heappush(
                    open_set,
                    (f_score, vizinho)
                )

    # Não existe caminho
    return None

def visualizar_caminho(mapa, caminho, inicio, objetivo):
    plt.figure(figsize=(8, 8))

    plt.imshow(mapa, cmap="binary", origin="upper")

    if caminho is not None:

        x = [p[1] for p in caminho]
        y = [p[0] for p in caminho]

        plt.plot(x, y, "r-", linewidth=2, label="Trajetória")
        plt.plot(x, y, "ro", markersize=4)

    plt.scatter(
        inicio[1], inicio[0],
        color="green", s=120, label="Início"
    )

    plt.scatter(
        objetivo[1], objetivo[0],
        color="blue", s=120, label="Objetivo"
    )

    plt.xticks(range(mapa.shape[1]))
    plt.yticks(range(mapa.shape[0]))

    plt.grid(True)
    plt.legend()
    plt.title("Planejamento de trajetória - A*")

    plt.show()

mapa = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
])

inicio = (0, 0)
objetivo = (7, 7)

caminho = astar(mapa, inicio, objetivo)

print("Caminho encontrado:")
print(caminho)

visualizar_caminho(mapa, caminho, inicio, objetivo)