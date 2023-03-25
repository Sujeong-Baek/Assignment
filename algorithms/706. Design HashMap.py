# https://leetcode.com/problems/design-hashmap/description/
class MyHashMap:

    def __init__(self):
        self.data=[]

    def put(self, key: int, value: int) -> None:  
        mapping=(key,value)
        for i,(k, _) in enumerate(self.data):
            if k ==key:
                self.data[i]=mapping
                return
        self.data.append(mapping)

    def get(self, key: int) -> int:
        for k,v in self.data:
            if key == k:
                return v
        return -1

    def remove(self, key: int) -> None:
        for i,(k,_) in enumerate(self.data):
            if key ==k:
                self.data.pop(i)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)