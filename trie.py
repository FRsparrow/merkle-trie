from node import Node, serialize, decode_node


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
            cld = node.get_child(c)
            if cld:
                node = cld
                key = key[1:]
            else:
                return node, key

        return node, key

    def get(self, key):
        node, key = self._locate(key)
        if key or not node.is_value_node():
            return None, False
        else:
            return node.value, True

    def put(self, key, value):
        node, key = self._locate(key)
        if key:
            node.add_child(key, value)
        else:
            node.set_value(value)

    def prove(self, key):
        node = self.root
        proof = {hash(node): serialize(node)}

        while key:
            c = key[0]
            cld = node.get_child(c)
            if cld:
                node = cld
                key = key[1:]
            else:
                return None, False

        if node.is_value_node():
            return proof, True
        else:
            return None, False

        # while key:
        #     c = key[0]
        #     cld = node.get_child(c)
        #     if cld:
        #         proof[hash(node)] = serialize(node)
        #         node = cld
        #         key = key[1:]
        #     else:
        #         return None, False
        #
        # if node.is_value_node():
        #     proof[hash(node)] = serialize(node)
        #     return proof, True
        # else:
        #     return None, False


def verify_proof(root_hash, key, proof):
    want_hash = root_hash
    buf = proof[want_hash]
    n = decode_node(buf)
    return n.get(key)