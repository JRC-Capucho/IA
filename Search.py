from LinkedList import LinkedList


class Search(object):
    
    # BUSCA EM CUSTO UNIFORM
    def custom_uniform(self,begins,ends,nodes,graph):
        l1 = LinkedList()
        l2 = LinkedList()

        visit = []

        l1.shift(begin,0,0,None)
        l2.shift(begin,0,0,None)

        row = []
        row.append(begin)
        row.append(0)
        visit.append(row)

        while l1.empty() == False:
            current = l1.pop()

            if current.status == ends:
                path = []
                path = l2.show_tree_two(current.status,current.value)

                return path, current.value2

            ind = nodes.index(current.status)
            for new in graph[ind]:
                v2 = current.value2 + new[1] # custo do caminho
                v1 = v2 # f1(n)

                flag1 = True
                flag2 = True

                for j in range(len(visit)):
                    if visit[j][0] == new[0]:
                        if visit[j][1]<=2:
                            flag1 = False
                        else:
                            visit[j][1] = v2
                            flag2 = False
                        break

                    if flag1:
                        l1.push_x(new[0],v1,v2,current)
                        l2.push_x(new[0],v1,v2,current)
                        if flag2:
                            row=[]
                            row.append(new[0])
                            row.append(v2)
                            visit.append(row)
            return "Caminho nao encontrado"

    # GREDDY
    def greddy(self,begin,ends,nodes,graph):
        ind_f = nodes.index(ends)
        l1 = LinkedList()
        l2 = LinkedList()
        visit=[]

        l1.shift(begin,0,0,None)
        l2.shift(begin,0,0,None)

        row=[]
        row.append(begin)
        row.append(0)
        visit.append(row)

        while l1.empty() == False:
            current = l1.pop()

            if current.status == ends:
                path=[]
                path=l2.show_tree_two(current.status,current,value)
                return path,current.value2

            ind = nodes.index(current.status)

            for new in graph[ind]:
                ind1 = nodes.index(new[0])
                v2 = current.value2 + new[1] # custo do caminho
                v1 = h[ind_f][ind1] # f2(n)

                flag1 = True
                flag2 = True
                
                for j in range(len(visit)):
                    if visit[j][0] == new[0]:
                        if visit[j][1]<=v2:
                            flag1 = False
                        else:
                            visit[j][1]=v2;
                        break
                    if flag1:
                        l1.push_x(new[0],v1,v2,current)
                        l2.push_x(new[0],v1,v2,current)
                        if flag2:
                            row = []
                            row.append(new[0])
                            row.append(v2)
                            visit.append(row)

        return "Caminho nao encontrado"

    def a_estrela(self,begin,ends,nodes,graph):
        ind_f = nodes.index(ends)
        l1 = LinkedList()
        l2 = LinkedList()
        visit = []

        l1.shift(begin,0,0,None)
        l2.shift(begin,0,0,None)
        row = []
        row.append(begin)
        row.append(0)
        visit.append(0)

        while l1.empty() == False:
            current = l1.pop()

            if current.status == ends:
                path = []
                path = l2.show_tree_two(current.status,current.value)
                return path, current.value2

            ind = nodes.index(current.status)
            for new in graph[ind]:

                ind1 = nodes.index(new[0])

                v2 = current.value2 + new[1]
                v1 = v2 + h[ind_f][ind1]

                flag1 = True
                flag2 = True
                for j in range(len(visit)):
                    if visit[j][0]==new[0]:
                        if visit[j][1]<=v2:
                            flag1 = False
                        else:
                            visit[j][1]=v2
                            flag2 = False
                        break
                    if flag1:
                        l1.push_x(new[0],v1,v2,current)
                        l2.push_x(new[0],v1,v2,current)
                        if flag2:
                            row = []
                            row.append(new[0])
                            row.append(v2)
                            visit.append(row)

        return "Caminho nao encontrado"

    def aia_estrela(self,begin,ends,nodes,graph,limit):
        ind_f = nodes.index(ends)
        while True:
            lim_exc = []
            l1 = LinkedList()
            l2 = LinkedList()
            visit = []

            l1.shift(begin,0,0,None)
            l2.shift(begin,0,0,None)

            row = []
            row.append(begin)
            row.append(0)
            visit.append(row)

            while l1.empty() == False:
                current = l1.pop()

                if current.status == ends:
                    path = []
                    path = l2.show_tree_two(current.status,current.value)
                    return path, current.value2

                ind = nodes.index(current.status)
                for new in graph[ind]:
                    ind1 = nodes.index(new[0]) 

                    v2 = current.value2 + new[1]
                    v1 = v2 + h[ind_f][ind1]

                    if v1<=limit:
                        flag1 = True
                        flag2 = True
                        for j in range(len(visit)):
                            if visit[j][0] == new[0]:
                                if visit[j][1] <= v2:
                                    flag1 = False
                                else:
                                    visit[j][1]=v2
                                    flag2 = False
                                break
                            if flag1:
                                l1.push_x(new[0],v1,v2,current)
                                l2.push_x(new[0],v1,v2,current)
                                if flag2:
                                    row = []
                                    row.append(new[0])
                                    row.append(v2)
                                    visit.append(row)
                    else:
                        lim_exc.append(v1)
                limit = sum(lim_exc)/len(lim_exc)
            return "Caminho nao encontrado"
