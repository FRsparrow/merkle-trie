from trie import Trie


def main():
    txs = {
        "a": "value0",
        "ab": "value1",
        "abc": "value2",
        "abd": "value3"
    }

    trie = Trie(txs)
    trie.put("b", "value4")
    val1 = trie.get("")