from LinkedList import LinkedList


class Search(object):
    # BUSCA EM AMPLITUDE
    def amplitude(self, begin, ends, nodes, graph):
        path = []
        for end in ends:
            # manipular a FILA para a busca
            l1 = LinkedList()
            # cópia para apresentar o path (somente inserção)
            l2 = LinkedList()

            # insere ponto inicial como nó raiz da árvore
            l1.shift(begin, 0, None)
            l2.shift(begin, 0, None)

            # controle de nós visitados
            visit = []
            row = []
            row.append(begin)
            row.append(0)
            visit.append(row)

            while l1.empty() == False:
                # remove o primeiro da fila
                current = l1.pop()

                ind = nodes.index(current.status)
                # varre todos as conexões dentro do graph a partir de current
                for new in graph[ind][::1]:
                    # pressuponho que não foi visit
                    flag = True

                    # controle de nós repetidos
                    for j in range(len(visit)):
                        if visit[j][0] == new:
                            if visit[j][1] <= (current.level + 1):
                                flag = False
                            else:
                                visit[j][1] = current.level + 1
                            break
                    # se não foi visit inclui na fila
                    if flag:
                        l1.shift(new, current.level + 1, current)
                        l2.shift(new, current.level + 1, current)

                        # marca como visit
                        row = []
                        row.append(new)
                        row.append(current.level + 1)
                        visit.append(row)

                        # verificar se é o objetivo
                        if new == end:
                            if not path:
                                path = l2.show_path()
                            else:
                                del path[len(path) - 1]
                                path += l2.show_path()
                            begin = end
                            # print("\nFila:\n", l1.show_list())
                            # print("\nÁrvore de busca:\n", l2.show_list())
                            break

        return path

    def profundidade(self, begin, end, nodes, graph):
        # manipular a PILHA para a busca
        l1 = LinkedList()

        # cópia para apresentar o path (somente inserção)
        l2 = LinkedList()

        # insere ponto inicial como nó raiz da árvore
        l1.shift(begin, 0, None)
        l2.shift(begin, 0, None)

        # controle de nós visitados
        visit = []
        row = []
        row.append(begin)
        row.append(0)
        visit.append(row)

        while l1.empty() == False:
            # remove o primeiro da fila
            current = l1.unshift()

            ind = nodes.index(current.status)

            # varre todos as conexões dentro do grafo a partir de current
            # for new in grafo[ind][::-1]:
            for new in graph[ind][::]:
                # pressuponho que não foi visit
                flag = True

                # controle de nós repetidos
                for j in range(len(visit)):
                    if visit[j][0] == new:
                        if visit[j][1] <= (current.level + 1):
                            flag = False
                        else:
                            visit[j][1] = current.level + 1
                        break

                # se não foi visit inclui na fila
                if flag:
                    l1.shift(new, current.level + 1, current)
                    l2.shift(new, current.level + 1, current)

                    # marca como visit
                    row = []
                    row.append(new)
                    row.append(current.level + 1)
                    visit.append(row)

                    # verifica se é o objetivo
                    if new == end:
                        path = []
                        path += l2.show_list()
                        # print("\nFila:\n",l1.exibeLista())
                        # print("\nÁrvore de busca:\n", l2.show_list())
                        return path

        return "path não encontrado"

    # BUSCA EM PROFUNDIDADE LIMITADA
    def prof_limitada(self, begin, end, limit, nodes, graph):
        # manipular a PILHA para a busca
        l1 = LinkedList()

        # cópia para apresentar o path (somente inserção)
        l2 = LinkedList()

        # insere ponto inicial como nó raiz da árvore
        l1.shift(begin, 0, None)
        l2.shift(begin, 0, None)

        # controle de nós visitados
        visit = []
        row = []
        row.append(begin)
        row.append(0)
        visit.append(row)

        while l1.empty() == False:
            # remove o primeiro da fila
            current = l1.unshift()

            if current.level < limit:
                ind = nodes.index(current.status)

                # varre todos as conexões dentro do graph a partir de current
                for new in graph[ind][::-1]:
                    # pressuponho que não foi visit
                    flag = True

                    # controle de nós repetidos
                    for j in range(len(visit)):
                        if visit[j][0] == new:
                            if visit[j][1] <= (current.level + 1):
                                flag = False
                            else:
                                visit[j][1] = current.level + 1
                            break

                    # se não foi visit inclui na fila
                    if flag:
                        l1.shift(new, current.level + 1, current)
                        l2.shift(new, current.level + 1, current)

                        # marca como visit
                        row = []
                        row.append(new)
                        row.append(current.level + 1)
                        visit.append(row)

                        # verifica se é o objetivo
                        if new == end:
                            path = []
                            path += l2.show_path()
                            # print("\nFila:\n",l1.exibeLista())
                            # print("\nÁrvore de busca:\n", l2.show_list())
                            return path

        return None

    # BUSCA EM APROFUNDAMENTO ITERATIVO
    def aprof_iterativo(self, begin, end, lim_max, nodes, graph):
        for limit in range(1, lim_max):
            # manipular a PILHA para a busca
            l1 = LinkedList()

            # cópia para apresentar o path (somente inserção)
            l2 = LinkedList()

            # insere ponto inicial como nó raiz da árvore
            l1.shift(begin, 0, None)
            l2.shift(begin, 0, None)

            # controle de nós visitados
            visit = []
            row = []
            row.append(begin)
            row.append(0)
            visit.append(row)

            while l1.empty() == False:
                # remove o primeiro da fila
                current = l1.unshift()

                if current.level < limit:
                    ind = nodes.index(current.status)

                    # varre todos as conexões dentro do graph a partir de current
                    for new in graph[ind][::-1]:
                        # pressuponho que não foi visit
                        flag = True

                        # controle de nós repetidos
                        for j in range(len(visit)):
                            if visit[j][0] == new:
                                if visit[j][1] <= (current.level + 1):
                                    flag = False
                                else:
                                    visit[j][1] = current.level + 1
                                break

                        # se não foi visit inclui na fila
                        if flag:
                            l1.shift(new, current.level + 1, current)
                            l2.shift(new, current.level + 1, current)

                            # marca como visit
                            row = []
                            row.append(new)
                            row.append(current.level + 1)
                            visit.append(row)

                            # verifica se é o objetivo
                            if new == end:
                                path = []
                                path += l2.show_path()
                                # print("\nFila:\n",l1.exibeLista())
                                # print("\nÁrvore de busca:\n", l2.show_list())
                                return path

        return None

        # BUSCA BIDIRECIONAL

    def bidirecional(self, begin, end, nodes, graph):
        # Primeiro Amplitude"
        # Manipular a FILA para a busca
        l1 = LinkedList()
        # cópia para apresentar o path (somente inserção)
        l2 = LinkedList()

        # Segundo Amplitude"
        # Manipular a FILA para a busca
        l3 = LinkedList()
        # cópia para apresentar o path (somente inserção)
        l4 = LinkedList()

        # insere ponto inicial como nó raiz da árvore
        l1.shift(begin, 0, None)
        l2.shift(begin, 0, None)

        l3.shift(end, 0, None)
        l4.shift(end, 0, None)

        # controle de nós visitados
        visit1 = []
        row = []
        row.append(begin)
        row.append(0)
        visit1.append(row)

        visit2 = []
        row = []
        row.append(end)
        row.append(0)
        visit2.append(row)

        level = 0
        while l1.empty() == False or l3.empty() == False:
            while l1.empty() == False:
                # para ir para o próximo amplitude
                if level != l1.first().level:
                    break

                # remove o primeiro da fila
                current = l1.pop()

                ind = nodes.index(current.status)

                # varre todos as conexões dentro do graph a partir de current
                for new in graph[ind]:
                    # pressuponho que não foi visit
                    flag = True

                    # controle de nós repetidos
                    for j in range(len(visit1)):
                        if visit1[j][0] == new:
                            if visit1[j][1] <= (current.level + 1):
                                flag = False
                            else:
                                visit1[j][1] = current.level + 1
                            break

                    # se não foi visit inclui na fila
                    if flag:
                        l1.shift(new, current.level + 1, current)
                        l2.shift(new, current.level + 1, current)

                        # marca como visit
                        row = []
                        row.append(new)
                        row.append(current.level + 1)
                        visit1.append(row)

                        # verifica se é o objetivo
                        flag = False
                        for j in range(len(visit2)):
                            if visit2[j][0] == new:
                                flag = True
                                break

                        if flag:
                            path = []
                            # print("Fila:\n",l1.exibeLista())
                            # print("\nÁrvore de busca:\n",l2.exibeLista())
                            # print("\nÁrvore de busca:\n",l4.exibeLista())
                            path += l2.show_path()
                            path += l4.show_path_b(new)
                            return path

            while l3.empty() == False:
                # para ir para o próximo amplitude
                if level != l3.first().level:
                    break

                # remove o primeiro da fila
                current = l3.pop()

                ind = nodes.index(current.status)

                # varre todos as conexões dentro do graph a partir de current
                for new in graph[ind]:
                    # pressuponho que não foi visit
                    flag = True

                    # controle de nós repetidos
                    for j in range(len(visit2)):
                        if visit2[j][0] == new:
                            if visit2[j][1] <= (current.level + 1):
                                flag = False
                            else:
                                visit2[j][1] = current.level + 1
                            break

                    # se não foi visit inclui na fila
                    if flag:
                        l3.shift(new, current.level + 1, current)
                        l4.shift(new, current.level + 1, current)

                        # marca como visit
                        row = []
                        row.append(new)
                        row.append(current.level + 1)
                        visit2.append(row)

                        # verifica se é o objetivo
                        flag = False
                        for j in range(len(visit1)):
                            if visit1[j][0] == new:
                                flag = True
                                break

                        if flag:
                            path = []
                            # print("Fila:\n",l3.exibeLista())
                            # print("\nÁrvore de busca:\n", l4.show_list())
                            # print("\nÁrvore de busca:\n", l2.show_list())
                            path += l4.show_path()
                            path += l2.show_path_b(new)
                            return path[::-1]

            level += 1

        return None
