import random as rd

import numpy as np


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
        # controle da árvore de busca
        self.father = father
        # indica o nó do grafo
        self.status = status
        # função de avaliação f(n) do método
        self.value = value
        # custo do caminho da origem até o nó atual
        self.value2 = value2
        # controle da lista encadeada
        self.prev = prev
        self.next_node = next_node
