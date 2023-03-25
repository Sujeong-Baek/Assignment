class Mydata:
    def __init__(self):
        self.data=[]
  

    def add(self, key: int) -> None:
        if not key in self.data:
            self.data.append(key)

    def remove(self, key: int) -> None:
        for i, k in enumerate(self.data):
            if k == key:
                self.data.pop(i)

    def contains(self, key: int) -> bool:
        return key in self.data

lst = [1,2,3,4]
# lst.pop(2) >> 3