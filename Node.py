class Node(object):
    def __init__(self, father=None, status=None, level=None, prev=None, next_node=None):
        self.father = father
        self.status = status
        self.level = level
        self.prev = prev
        self.next_node = next_node
