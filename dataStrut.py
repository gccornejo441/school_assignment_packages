
class DataStrut:
    def __init__(self, init_cap=10):
        # initialize the hash table with empty bucket list entries.
        self.hashtable = []
        for x in range(init_cap):
            self.hashtable.append([])

    # This function takes two arguments;returns from hashtable
    def numList(self, key):
        res = hash(key) % len(self.hashtable)
        listNumber = self.hashtable[res]
        return listNumber


    # Searches for matching prop
    def adjuster(self, key, item):
        for x in self.numList(key):
            # print (key_value)
            if x[0] == key:
                x[1] = item
                return True


    # Removes an item with matching key from the hash table.
    def remove(self, key):
        for x in self.numList(key):
            if x[0] == key:
                self.numList(key).remove([x[0], x[1]])


    ## Use works with integrated hash table that returns prop if found
    def hotItem(self, x):
            for i in self.numList(x):
                if i[0] == x:
                    return i[1]

