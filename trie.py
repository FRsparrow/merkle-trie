from node import Node, serialize, decode_node


class Trie:
    def __init__(self, txs=None):
        self.root = Node()
        if txs:
            for key in txs:
                self.put(key, txs[key])

    def __hash__(self):
        return hash(self.root)

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
        path = key
        node, key = self._locate(key)
        if key:
            node.add_child(key, value)
        else:
            node.set_value(value)

        self.set_dirty_on_path(path)

    def set_dirty_on_path(self, path):
        node = self.root
        for c in path:
            node.flags.set_dirty()
            node = node.get_child(c)

        node.flags.set_dirty()

    def prove(self, key):
        node = self.root
        proof_db = {}

        while key:
            c = key[0]
            cld = node.get_child(c)
            if cld:
                proof_db[str(hash(node))] = serialize(node)
                node = cld
                key = key[1:]
            else:
                return None, False

        if node.is_value_node():
            proof_db[str(hash(node))] = serialize(node)
            return proof_db, True
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

    # def resolve_hash(self, hash_node):
    #     h = hash_node.h
    #     return self.db.get(hash_node)


def verify_proof(root_hash, key, proof):
    want_hash = root_hash
    while True:
        if want_hash in proof:
            buf = proof[want_hash]
            n = decode_node(buf)

            if key:
                want_hash = n.get_child(key[0])
                key = key[1:]
            elif n.is_value_node():
                return n.value, True
            else:
                return None, False
        else:
            return None, False
