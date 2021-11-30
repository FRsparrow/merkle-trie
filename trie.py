from node import Node


class Trie:
    def __init__(self, txs=None):
        self.root = Node()
        for key in txs:
            self.put(key, txs[key])

    def __hash__(self):
        pass

    def _locate(self, key):
        node = self.root
        while key:
            c = key[0]
            if node.children[c] !=

    def get(self, key):
        node = self.root
        while True:
            if node is None:
                return None, False

            if len(key) >= 1:
                c = key[0]
                node = node.children[c]
                key = key[1:]
            elif node.is_value_node():
                return node.value, True
            else:
                return None, False

    def put(self, key, value):
        node = self.root


    def prove(self, key):
        pass


def verify_proof(root_hash, key, proof):
    pass