A **HashMap** is a data structure that stores elements as key-value pairs, allowing for efficient data retrieval based on keys. It is widely used in programming due to its fast access times, achieved through the use of hashing.

## **How HashMap Works**

1. **Key-Value Pairs**:

   - Each entry in a HashMap consists of a unique key and an associated value.
   - Keys are used to compute a hash code, which determines the storage location (bucket) of the entry.

2. **Hashing Mechanism**:

   - A hash function converts a key into an integer (hash code).
   - The hash code is then mapped to an index within an array of buckets using a modulo operation or bitwise operations for efficiency.

3. **Buckets**:

   - A bucket is a container where entries with the same hash code are stored.
   - If multiple keys map to the same bucket (collision), they are stored in a linked list or tree structure within that bucket.

4. **Collision Handling**:

   - **Separate Chaining**: Colliding entries are stored in a linked list or tree at the same bucket.
   - **Open Addressing**: Probes nearby buckets to find an empty one.

5. **Load Factor and Resizing**:
   - The load factor determines when the HashMap increases its capacity (e.g., when it becomes too full).
   - Resizing involves rehashing all entries into a larger array.

## **Basic Operations**

1. **Insertion (`put`)**:
   - Compute the hash code of the key.
   - Determine the index using the hash code.
   - Insert the key-value pair into the corresponding bucket.
2. **Retrieval (`get`)**:

   - Compute the hash code of the key.
   - Locate the bucket using the index.
   - Search for the key in that bucket and return its value.

3. **Deletion (`remove`)**:

   - Locate the bucket using the key's hash code.
   - Remove the corresponding entry from that bucket.

4. **Iteration**:
   - HashMaps allow iteration over keys, values, or entries.

## **Representation**

Internally, a HashMap can be visualized as follows:

| Bucket Index | Entries (Key-Value Pairs)        |
| ------------ | -------------------------------- |
| 0            | [(key1, value1)]                 |
| 1            | [(key2, value2), (key3, value3)] |
| 2            | []                               |
| ...          | ...                              |

Here, collisions at index 1 are handled using separate chaining (linked list/tree).

### Example in Python (Custom Implementation):

```python
class SimpleHashMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def put(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

# Usage
map = SimpleHashMap()
map.put("Alice", 25)
print(map.get("Alice")) # Output: 25
```
