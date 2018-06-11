from linked_list import LinkedList


class HashTable:
    def __init__(self, capacity=256):
        self._capacity = capacity
        self._data = [LinkedList()] * capacity
        self._size = 0

    def size(self):
        return self._size

    def _hash_func(self, key):
        if key is None:
            raise ValueError("Invalid key specified")
        if type(key) is str:
            return sum([ord(letter) for letter in key]) % self._capacity
        else:
            try:
                return int(key) % self._capacity
            except ValueError:
                print("Invalid key of type " + type(key).__name__)

    def _increase_capacity(self, mult=1.5):
        self._capacity = int(mult * self._capacity)
        tmp_data = [LinkedList()] * self._capacity
        tmp_data[0:len(self._data)] = self._data[:]
        self._data = tmp_data

    def _find_node_by_key(self, llist, key):
        curr = llist.head
        if curr is None:
            return None

        while curr.next is not None:
            if curr.val[0] == key:
                return curr
            curr = curr.next
        if curr.val[0] == key:
            return curr
        return None

    def insert(self, key, val):
        hash_val = self._hash_func(key)
        store = self._data[hash_val]

        # in this implementation, i'll just remove the node if the key exists
        # and re-create/append a new one to the end of the list
        existing_node = self._find_node_by_key(store, key)
        if existing_node is not None:
            store.remove(existing_node)
            self._size -= 1

        store.insert_last((key, val))
        self._size += 1

    def lookup(self, key):
        hash_val = self._hash_func(key)
        store = self._data[hash_val]
        found_node = self._find_node_by_key(store, key)
        if found_node is None:
            return None
        return found_node.val[1]
