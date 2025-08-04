from hash_table import HashTable

hash_table = HashTable(1)

for i in range(20):
    pairs = len(hash_table)
    empty = hash_table.capacity - pairs
    print(
        f"{pairs:>2}/{hash_table.capacity:>2}",
        ("X" * pairs) + ("." * empty)
    )
    hash_table[i] = i