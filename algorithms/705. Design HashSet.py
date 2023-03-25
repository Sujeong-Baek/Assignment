class Mydata:
    def __init__(self):
        self.data=[[] for _ in range(10)]

    def add(self, key: int) -> None:
        data = self.data[key%10]
        if key not in data:
            data.append(key)

    def remove(self, key: int) -> None:
        data = self.data[key%10]
        for i, k in enumerate(data):
            if k == key:
                data.pop(i)

    def contains(self, key: int) -> bool:
        return key in self.data[key%10]

lst = [1,2,3,4]
# lst.pop(2) >> 3

# add(2), add(22) >> [2, 22]