import random as rd

import numpy as np
from flask import Flask, render_template, request
from flask_cors import CORS

from Search import Search

app = Flask(__name__)

CORS(app)

nodes = [
    "RUA1",
    "RUA2",
    "RUA3",
    "RUA4",
    "RUA5",
    "RUA6",
    "RUA7",
    "RUA8",
    "RUA9",
    "RUA10",
    "RUA11",
    "RUA12",
    "RUA13",
    "RUA14",
    "RUA15",
    "RUA16",
    "RUA17",
    "RUA18",
    "RUA19",
    "RUA20",
]

graph = [
    [["RUA20", 150], ["RUA17", 236], ["RUA16", 280]],
    [["RUA18", 170], ["RUA14", 202], ["RUA7", 180], ["RUA6", 422]],
    [["RUA15", 292], ["RUA14", 276], ["RUA4", 240]],
    [["RUA11", 150], ["RUA3", 240]],
    [["RUA8", 172]],
    [["RUA16", 198], ["RUA2", 422]],
    [["RUA2", 180]],
    [["RUA18", 196], ["RUA5", 172]],
    [["RUA19", 184], ["RUA12", 164]],
    [["RUA17", 222], ["RUA11", 140]],
    [["RUA10", 140], ["RUA4", 150]],
    [["RUA9", 164]],
    [["RUA20", 142], ["RUA16", 302]],
    [["RUA15", 194], ["RUA3", 276], ["RUA2", 202]],
    [["RUA16", 160], ["RUA14", 194], ["RUA3", 292]],
    [["RUA15", 160], ["RUA13", 302], ["RUA6", 198], ["RUA1", 280]],
    [["RUA10", 222], ["RUA1", 236]],
    [["RUA19", 284], ["RUA8", 196], ["RUA2", 170]],
    [["RUA18", 284], ["RUA9", 184]],
    [["RUA13", 142], ["RUA1", 150]],
]


def gera_H(n, nodes, graph):
    aux = Search()
    h = np.zeros((n, n), int)
    i = 0
    for node_from in nodes:
        j = 0
        for node_destiny in nodes:
            if node_from != node_destiny:
                cam, v = aux.custom_uniform(node_from, node_destiny, nodes, graph)
                h[i][j] = v * rd.uniform(0, 1)
            j += 1
        i += 1
    return h


@app.route("/custom_uniform", methods=["POST"])
def custom_uniform():
    sol = Search()

    data = request.get_json()

    aux = data["begin"].upper()
    res = []
    for path in data["ends"]:
        path = path.upper()
        res.append(sol.custom_uniform(aux, path, nodes, graph))
        aux = path
    return res


@app.route("/greedy", methods=["POST"])
def greedy():
    sol = Search()
    h = gera_H(len(nodes), nodes, graph)

    data = request.get_json()

    aux = data["begin"].upper()
    res = []
    for path in data["ends"]:
        path = path.upper()
        res.append(sol.greedy(aux, path, nodes, graph, h))
        aux = path
    return res


@app.route("/a_star", methods=["POST"])
def a_star():
    sol = Search()
    h = gera_H(len(nodes), nodes, graph)

    data = request.get_json()

    aux = data["begin"].upper()
    res = []
    for path in data["ends"]:
        path = path.upper()
        res.append(sol.a_star(aux, path, nodes, graph, h))
        aux = path
    return res


@app.route("/aia_star", methods=["POST"])
def aia_star():
    sol = Search()
    h = gera_H(len(nodes), nodes, graph)

    data = request.get_json()

    aux = data["begin"].upper()
    res = []
    for path in data["ends"]:
        path = path.upper()
        limit = h[nodes.index(aux)][nodes.index(path)]
        res.append(sol.aia_estrela(aux, path, nodes, graph, limit, h))
        aux = path
    return res


if __name__ == "__main__":
    app.run(debug=True)
