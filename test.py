from trie import Trie
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
        self.assertFalse(ok)

        key = "ab"
        proof, ok = trie.prove(key)
        self.assertTrue(ok)

        root_hash = hash(trie)
        val, ok =
        key := []
        byte
        {1, 2, 3}
        proof, ok := tr.Prove(key)
        require.
        True(t, ok)

        rootHash := tr.Hash()

        // verify
        the
        proof
        with the root hash, the key in question and its proof
        val, err := VerifyProof(rootHash, key, proof)
        require.NoError(t, err)

        // when
        the
        verification
        has
        passed, it
        should
        return the
        correct
        value
        for the key
            require.Equal(t, []
            byte("hello"), val)

