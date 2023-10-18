import random as rd
import sys

import numpy as np

from Search import Search


def gera_H(n):
    aux = Search()
    h = np.zero((n, n), int)
    i = 0
    for no_origem in nodes:
        j = 0
        for no_destino in nodes:
            if no_origem != no_destino:
                cam, v = aux.custom_uniform(no_origem, no_destino)
                h[i][j] = v * rd.uniform(0, 1)
            j += 1
        i += 1
    return h


def creates(file):
    f = open(file, "r")

    i = 0
    nodes = []
    graph = []

    for str1 in f:
        str1 = str1.strip("\n")
        str1 = str1.split(",")
        if i == 0:
            nodes = str1
        else:
            graph.append(str1)

        i += 1

    return nodes, graph


nodes, graph = creates("ruas.txt")

sol = Search()
path = []

origin = "Rua1"
destinys = ["Rua10", "Rua5", "Rua15"]

if origin not in nodes:
    print("Rua não está na lista")
    sys.exit()

for node in nodes:
    if node not in nodes:
        print("Rua não está na lista")
        sys.exit()


# path = sol.prof_limitada(origin, destiny, 3, nodes, graph)
# path = sol.aprof_iterativo(origin, destiny, 5, nodes, graph)
# path = sol.bidirecional(origin, destiny, nodes, graph)

path = sol.amplitude(origin, destinys, nodes, graph)

print("\n*****AMPLITUDE*****\n", path)

path_prof = []
for destiny in destinys:
    path_prof += sol.profundidade(origin, destiny, nodes, graph)
    del path_prof[len(path_prof) - 1]
    origin = destiny

print("\n*****PROFUNDIDA*****\n", path_prof)
#
path_prof = []
for destiny in destinys:
    aux = sol.prof_limitada(origin, destiny, 3, nodes, graph)
    if isinstance(aux, list):
        path_prof += aux
        del path_prof[len(path_prof) - 1]
    else:
        print(aux)
    origin = destiny

print("\n*****PROFUNDIDA LIMIT*****\n", path_prof)
#
path_prof = []
for destiny in destinys:
    aux = sol.aprof_iterativo(origin, destiny, 10, nodes, graph)
    if isinstance(aux, list):
        path_prof += aux
        del path_prof[len(path_prof) - 1]
    else:
        print(aux)
    origin = destiny

print("\n*****APROF ITERATIVA*****\n", path_prof)

path_prof = []
for destiny in destinys:
    aux = sol.bidirecional(origin, destiny, nodes, graph)
    if isinstance(aux, list):
        path_prof += aux
        del path_prof[len(path_prof) - 1]
    else:
        print(aux)
    origin = destiny

print("\n*****BIDIRECIONAL*****\n", path_prof)
