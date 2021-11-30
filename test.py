from trie import Trie, verify_proof
import unittest


class MyTest(unittest.TestCase):
    # def setUp(self) -> None:
    #     pass
    #
    # def tearDown(self) -> None:
    #     pass

    def test_get(self):
        trie = Trie({"a": "value0", "b": "value1", "ab": "value2"})
        value0 = trie.get("a")
        value1 = trie.get("b")
        value2 = trie.get("ab")

        self.assertEqual(value0, "value0")
        self.assertEqual(value1, "value1")
        self.assertEqual(value2, "value2")

    def test_put(self):
        trie = Trie()
        trie.put("a", "value0")
        trie.put("b", "value1")
        trie.put("ab", "value2")

        self.assertEqual(trie.get("a"), "value0")
        self.assertEqual(trie.get("b"), "value1")
        self.assertEqual(trie.get("ab"), "value2")

        trie.put("a", "value3")

        self.assertEqual(trie.get("a"), "value3")

    def test_data_integrity(self):
        trie = Trie()
        hash0 = hash(trie)

        trie.put("a", "value0")
        hash1 = hash(trie)

        trie.put("b", "value1")
        hash2 = hash(trie)

        trie.put("ab", "value2")
        hash3 = hash(trie)

        self.assertNotEqual(hash0, hash1)
        self.assertNotEqual(hash1, hash2)
        self.assertNotEqual(hash2, hash3)

        trie2 = Trie({{"a": "value0", "b": "value1", "ab": "value2"}})
        hash4 = hash(trie2)
        self.assertEqual(hash3, hash4)

    def test_prove_and_verify_proof(self):
        trie = Trie({"a": "value0", "b": "value1", "ab": "value2", "ac": "value3"})
        not_exist_key = "ad"
        _, ok = trie.prove(not_exist_key)
        self.assertFalse(ok)    # there exists no such key

        key = "ab"
        proof, ok = trie.prove(key)
        self.assertTrue(ok)

        root_hash = hash(trie)

        value2, ok = verify_proof(root_hash, key, proof)
        self.assertTrue(ok)
        self.assertEqual(value2, "value2")

        trie.put("acd", "value4")
        proof, ok = trie.prove(key)
        self.assertTrue(ok)

        _, ok = verify_proof(root_hash, key, proof)
        self.assertFalse(ok)    # value has been changed