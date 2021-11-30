from dic import dic_size, char_to_index


class Node:
    def __init__(self, value=None):
        self.children = [None] * dic_size
        self.value = value

    def __hash__(self):
        pass

    def set_value(self, value):
        self.value = value

    def get_child(self, c):
        return self.children[char_to_index(c)]

    def add_child(self, key, value):
        if not key:
            return

        par = self
        for c in key:
            idx = char_to_index(c)
            par.children[idx] = Node()
            par = par.children[idx]

        par.set_value(value)

    def is_value_node(self):
        return self.value is not None


def serialize(node):
    return node


def decode_node(buf):
    return buf
