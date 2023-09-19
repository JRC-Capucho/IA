from re import S
from flask import Flask, render_template, request
from Search import Search

app = Flask(__name__)


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


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process_form", methods=["POST"])
def process_form():
    origin = request.form.get("origin")
    destinys = request.form.get("destiny")
    limit = request.form.get("limit")
    search_type = request.form.get("search_type")

    destinys = destinys.split(",")
    nodes, graph = creates("ruas.txt")
    sol = Search()

    if search_type == "1":
        path = sol.amplitude(origin, destinys, nodes, graph)
        return str(path)

    if search_type == "2":
        path_prof = []
        for destiny in destinys:
            path_prof += sol.profundidade(origin, destiny, nodes, graph)
            del path_prof[len(path_prof) - 1]
            origin = destiny
        return str(path_prof)

    if search_type == "3":
        path_prof = []
        for destiny in destinys:
            aux = sol.prof_limitada(origin, destiny, limit, nodes, graph)
            if isinstance(aux, list):
                path_prof += aux
                del path_prof[len(path_prof) - 1]
            else:
                print(aux)
            origin = destiny
        return str(path_prof)

    if search_type == "4":
        path_prof = []
        for destiny in destinys:
            aux = sol.aprof_iterativo(origin, destiny, limit, nodes, graph)
            if isinstance(aux, list):
                path_prof += aux
                del path_prof[len(path_prof) - 1]
            else:
                print(aux)
            origin = destiny

        return str(path_prof)

    if search_type == "5":
        path_prof = []
        for destiny in destinys:
            aux = sol.bidirecional(origin, destiny, nodes, graph)
            if isinstance(aux, list):
                path_prof += aux
                del path_prof[len(path_prof) - 1]
            else:
                print(aux)
            origin = destiny

        return str(path_prof)
    return "Error"


if __name__ == "__main__":
    app.run(debug=True)
