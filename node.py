from dic import dic_size, char_to_index


class Node:
    def __init__(self, value=None):
        self.children = [None] * dic_size
        self.value = value
        self.flags = NodeFlag() # hash cache and dirty flag

    def __hash__(self):
        if self.hash_valid():
            return self.flags.h
        else:
            h = hash(serialize(self))
            self.flags.set_h(h)
            return h

    def set_value(self, value):
        self.value = value

    def get_child(self, c):
        return self.children[char_to_index(c)]

    # key length > 1, add all nodes at one time
    def add_child(self, key, value):
        if not key:
            return

        par = self
        for c in key:
            idx = char_to_index(c)
            par.children[idx] = Node()
            par = par.children[idx]

        par.set_value(value)

    def hash_valid(self):
        return self.flags.valid()

    def is_value_node(self):
        return self.value is not None


# class HashNode:
#     def __init__(self, node):
#         self.h = hash(serialize(node))


class NodeFlag:
    def __init__(self):
        self.h = None
        self.dirty = False

    def set_h(self, h):
        self.h = h
        self.dirty = False

    def set_dirty(self):
        self.dirty = True

    def valid(self):
        return self.h and not self.dirty


# (idx,cld_hash,)*value
# '1,5354039371319016526,2,6770954456685134596,value0'
def serialize(node):
    enc = ""
    for idx, cld in enumerate(node.children):
        if cld:
            h = hash(cld)
            enc += f"{idx},{h},"

    if node.is_value_node():
        enc += str(node.value)

    return enc


def decode_node(buf):
    node = Node()
    enc = buf.split(',')
    if len(enc) % 2:
        node.set_value(enc[-1])
        enc = enc[:-1]

    for i in range(1, len(enc), 2):
        idx = int(enc[i-1])
        h = enc[i]
        node.children[idx] = h

    return node
