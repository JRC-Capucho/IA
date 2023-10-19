import random as rd
import sys

import numpy as np

from Search import Search


def gera_H(n, nodes, graph):
    aux = Search()
    h = np.zeros((n, n), int)
    i = 0
    for no_origem in nodes:
        j = 0
        for no_destino in nodes:
            if no_origem != no_destino:
                cam, v = aux.custom_uniform(no_origem, no_destino, nodes, graph)
                h[i][j] = v * rd.uniform(0, 1)
            j += 1
        i += 1
    return h


sol = Search()

path = []

sol = Search()

inicio = "ARAD"
fim = "BUCARESTE"

h = gera_H(len(nos), nos, grafo)

caminho, custo = sol.custom_uniform("ARAD", "BUCARESTE", nos, grafo)

print("Custo Uniform: ", caminho[::-1], "\nCusto do Caminho: ", custo)

caminho, custo = sol.greedy("ARAD", "BUCARESTE", nos, grafo, h)

print("Greedy: ", caminho[::-1], "\nCusto do Caminho: ", custo)

caminho, custo = sol.a_star("ARAD", "BUCARESTE", nos, grafo, h)

print("A_estrela: ", caminho[::-1], "\nCusto do Caminho: ", custo)

ind_inicio = nos.index("ARAD")
ind_fim = nos.index("BUCARESTE")

limit = h[ind_inicio][ind_fim]

caminho, custo = sol.aia_estrela("ARAD", "BUCARESTE", nos, grafo, limit, h)

print("AIA_estrela: ", caminho[::-1], "\nCusto do Caminho: ", custo)
