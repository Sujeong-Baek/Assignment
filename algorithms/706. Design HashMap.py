# https://leetcode.com/problems/design-hashmap/description/
class MyHashMap:

    def __init__(self):
        self.hashmap=[]

    def put(self, key: int, value: int) -> None:  
        mapping=[key,value]
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0]==key:
                self.hashmap[i]=mapping
                return
        self.hashmap.append(mapping)

    def get(self, key: int) -> int:
        for mapping in self.hashmap:
            if key == mapping[0]:
                return mapping[-1]
        return -1

    def remove(self, key: int) -> None:
        for mapping in self.hashmap:
            if key ==mapping[0]:
                self.hashmap.remove(mapping)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)