
class DataStrut:

    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, init_cap=10):
        # initialize the hash table with empty bucket list entries.
        self.hashtable = []
        for x in range(init_cap):
            self.hashtable.append([])

    # finds  the bucket_list
    def bucket_list(self, key):
        res = hash(key) % len(self.hashtable)
        listNumber = self.hashtable[res]
        return listNumber



    # update key if it is already in the bucket
    def update(self, key, item):
        for x in self.bucket_list(key):
            # print (key_value)
            if x[0] == key:
                x[1] = item
                return True


    # Removes an item with matching key from the hash table.
    def remove(self, key):
        for x in self.bucket_list(key):
            # print (key_value)
            if x[0] == key:
                self.bucket_list(key).remove([x[0], x[1]])


    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, x):
            for i in self.bucket_list(x):
                if i[0] == x:
                    return i[1]

