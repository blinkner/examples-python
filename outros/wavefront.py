import numpy as np
from collections import deque
import matplotlib.pyplot as plt

def wavefront(mapa, objetivo):
    mapa = np.array(mapa, dtype=int)

    linhas, colunas = mapa.shape

    # Matriz de distâncias
    distancias = np.full(
        (linhas, colunas),
        np.inf
    )

    x, y = objetivo

    # Validação do objetivo
    if not (0 <= x < linhas and 0 <= y < colunas):
        raise ValueError("Objetivo fora do mapa")

    if mapa[x, y] != 0:
        raise ValueError("Objetivo localizado em obstáculo")

    # Movimentos possíveis (8 direções)
    movimentos = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    # Inicializa a fila com o objetivo
    fila = deque([objetivo])
    distancias[x, y] = 0

    while fila:
        atual = fila.popleft()
        x, y = atual

        for dx, dy in movimentos:
            nx = x + dx
            ny = y + dy

            # Verifica os limites
            if not (0 <= nx < linhas and 0 <= ny < colunas):
                continue

            # Verifica obstáculos
            if mapa[nx, ny] != 0:
                continue

            # Verifica se já foi visitado
            if distancias[nx, ny] != np.inf:
                continue

            # Impede passagem diagonal entre obstáculos
            if dx != 0 and dy != 0:
                if mapa[x + dx, y] != 0 or mapa[x, y + dy] != 0:
                    continue

            # Atualiza distância
            distancias[nx, ny] = distancias[x, y] + 1
            fila.append((nx, ny))
    return distancias

def extrair_caminho(mapa, distancias, inicio, objetivo):
    movimentos = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    atual = inicio
    caminho = [atual]

    while atual != objetivo:
        x, y = atual

        melhor_vizinho = None
        menor_distancia = distancias[x, y]

        for dx, dy in movimentos:
            nx = x + dx
            ny = y + dy

            # Verifica limites
            if not (0 <= nx < mapa.shape[0] and
                    0 <= ny < mapa.shape[1]):
                continue

            # Verifica obstáculos
            if mapa[nx, ny] != 0:
                continue

            # Impede movimento diagonal entre obstáculos
            if dx != 0 and dy != 0:
                if mapa[x + dx, y] != 0 or mapa[x, y + dy] != 0:
                    continue

            # Seleciona vizinho com menor distância
            if distancias[nx, ny] < menor_distancia:
                menor_distancia = distancias[nx, ny]
                melhor_vizinho = (nx, ny)

        # Não encontrou caminho válido
        if melhor_vizinho is None:
            return None

        atual = melhor_vizinho
        caminho.append(atual)
    return caminho


def visualizar_resultado(mapa, distancias, caminho, inicio, objetivo):
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))

    # Mapa e trajetória
    ax[0].imshow(mapa, cmap="binary", origin="upper")

    if caminho is not None:
        x = [p[1] for p in caminho]
        y = [p[0] for p in caminho]

        ax[0].plot(x, y, "r-", linewidth=2)
        ax[0].plot(x, y, "ro", markersize=4)

    ax[0].scatter(
        inicio[1], inicio[0],
        color="green", s=120, label="Início"
    )

    ax[0].scatter(
        objetivo[1], objetivo[0],
        color="blue", s=120, label="Objetivo"
    )

    ax[0].set_title("Trajetória Wavefront")
    ax[0].legend()

    # Campo de distâncias
    campo = np.ma.masked_where(
        mapa == 1,
        distancias
    )

    imagem = ax[1].imshow(
        campo,
        cmap="viridis",
        origin="upper"
    )

    ax[1].set_title("Campo de distâncias")

    fig.colorbar(
        imagem,
        ax=ax[1],
        label="Distância até o objetivo"
    )

    # Configuração dos eixos
    for eixo in ax:
        eixo.set_xticks(range(mapa.shape[1]))
        eixo.set_yticks(range(mapa.shape[0]))
        eixo.grid(True)

    plt.tight_layout()
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

# Propagação
distancias = wavefront(mapa, objetivo)

# Extração do caminho
caminho = extrair_caminho(
    mapa,
    distancias,
    inicio,
    objetivo
)

print("Matriz de distâncias:")
print(distancias)

print("\nCaminho encontrado:")
print(caminho)

visualizar_resultado(
    mapa,
    distancias,
    caminho,
    inicio,
    objetivo
)