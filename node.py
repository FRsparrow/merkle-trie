from dic import dic_size, dic


class Node:
    def __init__(self, value):
        self.next = [None] * dic_size
        self.value = value

    def __hash__(self):
        pass

    def _serialize(self):
        pass