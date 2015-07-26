__author__ = 'cloudera'


class Map:
    def __init__(self):
        self.size = 11
        self.keys = [None] * self.size
        self.datas = [None] * self.size

    def hash(self, key):
        print 'hashval is ', key % self.size
        return key % self.size

    def rehash(self, old_hash_val):
        return (old_hash_val+1) % self.size

    def show_map(self):
        print self.keys
        print self.datas

    def put(self, key, data):
        hash_val = self.hash(key)
        if self.keys[hash_val] is None:  # if nothing exist
            self.keys[hash_val] = key
            self.datas[hash_val] = data
        elif self.keys[hash_val] == key:  # replace old data
            self.datas[hash_val] = data
        else:
            new_hash_val = self.rehash(hash_val)  # if occupied calculate new hash value
            while self.keys[new_hash_val] is not None and self.keys[new_hash_val] != key:
                hash_val = new_hash_val
                new_hash_val = self.rehash(hash_val)
            self.keys[new_hash_val] = key
            self.datas[new_hash_val] = data

    def get(self, key):
        hash_val = self.hash(key)
        if self.keys[hash_val] == key:
            return self.datas[hash_val]
        elif self.keys[hash_val] == None:
            return None
        else:
            new_hash_val = self.rehash(hash_val)
            while self.keys[new_hash_val] is not None and self.keys[new_hash_val] != key:
                hash_val = new_hash_val
                new_hash_val = self.rehash(hash_val)
            return self.datas[new_hash_val]

# main - test
m = Map()
m.put(44, 'sharad')
m.put(55, 'surabhi')
m.put(66, 'kusuma')
# m.show_map()
print m.get(44)
print m.get(66)
