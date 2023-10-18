class Node(object):
    def __init__(
        self,
        father=None,
        status=None,
        value=None,
        value2=None,
        prev=None,
        next_node=None,
    ):
        self.father = father
        self.status = status
        self.level = level
        self.value = value
        self.value2 = value2
        self.prev = prev
        self.next_node = next_node
