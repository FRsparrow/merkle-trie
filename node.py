from dic import dic_size, dic


class Node:
    def __init__(self, value=None):
        self.children = [None] * dic_size
        self.value = value

    def __hash__(self):
        pass

    def get_child(self, c):
        return self.children[]

    def serialize(self):
        pass

    def is_value_node(self):
        return self.value is not None
