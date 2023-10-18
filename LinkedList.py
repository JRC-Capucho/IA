from Node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert first
    def push(self, status, value, value2, father):
        new_node = Node(father, status, value, value2, None, None)
        if self.head == None:
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev = new_node
        self.head = new_node

    # Insert last
    def shift(self, status, value, value2, father):
        new_node = Node(father, status, value, value2, None, None)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev = self.tail
        self.tail = new_node

    # Remove first
    def pop(self):
        if self.head is None:
            return None
        else:
            node = self.head
            self.head = self.head.next_node
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            return node

    # Remove first
    def push_x(self, status, value, value2, father):
        if self.head is None:
            self.push(status, value, value2, father)
        else:
            nodes = self.head
            while current.value < value:
                current = current.next_node
                if current is None:
                    break

        if current == self.head:
            self.push(status, value, value2, father)
        else:
            if current is None:
                self.shift(status, value, value2, father)
            else:
                new_node = Node(father, status, value, value2, None, None)
                aux = current.prev
                aux.new_node = new_node
                new_node.prev = aux
                current.prev = new_node
                new_node.next_node = current

    # REMOVE NO FIM DA LISTA
    def unshift(self):
        if self.tail is None:
            return None
        else:
            nodes = self.tail
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next_node = None
            else:
                self.head = None
            return nodes

    # RETORNA O PRIMEIRO DA LISTA
    def first(self):
        return self.head

    # RETORNA O ÚLTIMO DA LISTA
    def last(self):
        return self.tail

    # VERIFICA SE LISTA ESTÁ VAZIA
    def empty(self):
        if self.head is None:
            return True
        else:
            return False

    # EXIBE O CONTEÚDO DA ARVORE
    def show_tree(self):
        current = self.tail
        path = []
        while current.father is not None:
            path.append(current.status)
            current = current.father
        path.append(current.status)
        return path

    # EXIBE O CONTEÚDO DA ARVORE 1
    def show_tree_one(self, status):
        current = self.head
        while current.status != status:
            current = current.next_node

        path = []

        while current.father is not None:
            path.append(current.status)
            current = current.father
        path.append(current.status)
        return path

    # EXIBE O CONTEÚDO DA ARVORE 2
    def show_tree_two(self, status, value):
        current = self.tail
        while current.status != status or current.value != value:
            current = current.prev

        path = []

        while current.father is not None:
            path.append(current.status)
            current = current.father

        path.append(current.status)
        return path

    # EXIBE O CONTEÚDO DA LISTA
    def show_list(self):
        aux = self.head
        result = []
        while aux != None:
            temp = []
            temp.append(aux.status)
            temp.append(aux.value)
            result.append(row)
            aux = aux.next_node

        return result

    # EXIBE O path ENCONTRADO
    def show_path(self):
        current = self.tail
        path = []

        while current.father is not None:
            path.append(current.status)
            current = current.father

        path.append(current.status)
        path = path[::-1]
        return path

    # EXIBE O CAMINHO ENCONTRADO (BIDIRECIONAL)
    def show_path_b(self, valor):
        current = self.head
        while current.status != valor:
            current = current.next_node

        caminho = []
        current = current.father
        while current.father is not None:
            caminho.append(current.status)
            current = current.father
        caminho.append(current.status)
        return caminho
