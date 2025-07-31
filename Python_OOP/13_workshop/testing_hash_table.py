from unittest import TestCase, main
from hash_table import HashTable

class HashTableTests(TestCase):
    def setUp(self):
        self.hash_table = HashTable(capacity=4)
        self.hash_table["hello"] = "Hello World!"
        self.hash_table[False] = True
        self.hash_table[98.6] = 37

    def test_should_create_hash_table(self):
        self.assertIsNotNone(self.hash_table)

    def test_should_report_len_of_empty_table(self):
        self.assertEqual(0, len(HashTable(100)))

    def test_should_create_empty_pair_slots(self):
        hash_table = HashTable(4)
        expected = [None] * 4
        actual = hash_table._array
        self.assertEqual(expected, actual)

    def test_should_insert_key_value_pairs(self):
        self.assertIn(("hello", "Hello World!"), self.hash_table.array)
        self.assertIn((False, True), self.hash_table.array)
        self.assertIn((98.6, 37), self.hash_table.array)


if __name__ == '__main__':
    main()
