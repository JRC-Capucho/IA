from Node import Node


class LinkedList(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def push(self, status, v1, v2, father):
        new_node = Node(father, status, v1, v2, None, None)
        if self.head == None:
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev = new_node
        self.head = new_node

    # INSERE NO FIM DA LISTA
    def shift(self, status, v1, v2, father):
        new_node = Node(father, status, v1, v2, None, None)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev = self.tail
        self.tail = new_node

    # INSERE NO FIM DA LISTA
    def push_x(self, status, v1, v2, father):
        # se lista estiver vazia
        if self.head is None:
            self.push(status, v1, v2, father)
        else:
            current = self.head
            while current.value < v1:
                current = current.next_node
                if current is None:
                    break

            if current == self.head:
                self.push(status, v1, v2, father)
            else:
                if current is None:
                    self.shift(status, v1, v2, father)
                else:
                    new_node = Node(father, status, v1, v2, None, None)
                    aux = current.prev
                    aux.next_node = new_node
                    new_node.prev = aux
                    current.prev = new_node
                    new_node.next_node = current

    # REMOVE NO INÍCIO DA LISTA
    def pop(self):
        if self.head is None:
            return None
        else:
            nodes = self.head
            self.head = self.head.next_node
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            return nodes

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

    def empty(self):
        if self.head is None:
            return True
        else:
            return False

    def show_list(self):
        aux = self.head
        result = []
        while aux != None:
            row = []
            row.append(aux.status)
            row.append(aux.value)
            result.append(row)
            aux = aux.next_node

        return result

    def show_tree(self):
        current = self.tail
        path = []
        while current.father is not None:
            path.append(current.status)
            current = current.father
        path.append(current.status)
        return path

    def show_tree_one(self, status):
        current = self.head
        while current.status != status:
            current = current.next_node

        path = []
        current = current.father
        while current.father is not None:
            path.append(current.status)
            current = current.father
        path.append(current.status)
        return path

    def show_tree_two(self, status, v1):
        current = self.tail

        while current.status != status or current.value != v1:
            current = current.prev

        path = []
        while current.father is not None:
            path.append(current.status)
            current = current.father
        path.append(current.status)
        return path

    def first(self):
        return self.head

    def last(self):
        return self.tail
