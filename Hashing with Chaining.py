class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  #
                return
        self.table[index].append((key, value))
        self.count += 1
        self.resize_if_needed()

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Key not found

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.count -= 1
                return True
        return False  # Key not found

    def resize_if_needed(self):
        load_factor = self.count / self.size
        if load_factor > 0.7:  # Resize when load factor exceeds 0.7
            new_size = self.size * 2
            new_table = [[] for _ in range(new_size)]
            for chain in self.table:
                for key, value in chain:
                    index = hash(key) % new_size
                    new_table[index].append((key, value))
            self.size = new_size
            self.table = new_table

    def display(self):
        for i, chain in enumerate(self.table):
            print(f"Bucket {i}: {chain}")

if __name__ == "__main__":
    ht = HashTableChaining()
    ht.insert("Alice", 25)
    ht.insert("Bob", 30)
    ht.insert("Charlie", 35)
    print("Hash Table After Insertions:")
    ht.display()

    print("\nSearch for 'Alice':", ht.search("Alice"))
    print("Search for 'David':", ht.search("David"))

    print("\nDeleting 'Bob'...")
    ht.delete("Bob")
    ht.display()
