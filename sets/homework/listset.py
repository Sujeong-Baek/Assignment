# listset.py
# Implementation of Set ADT using a Python list

class Set():
    def __init__(self, elements=None):
        self._data = []  # empty list = empty set
        if elements:
            for el in elements:
                self.add(el)

    def __contains__(self, el):
        for x in self._data:
            if x == el:
                return True
        return False

    def __len__(self):
        return len(self._data)

    def add(self, el):
        if el not in self._data:
            self._data.append(el)

    def remove(self, el):
        if el in self._data:
            self._data.remove(el)  # use remove for list
        else:
            raise KeyError(el)

    def discard(self, el):
        if el in self._data:
            self._data.remove(el)  # use remove for list

    def __eq__(self, t):
        if len(self) != len(t):
            return False
        return self.issubset(t)

    def issubset(self, t):
        for el in self._data:
            if el not in t:
                return False
        return True

    def issuperset(self, t):
        return t.issubset(self)

    def union(self, t):
        newSet = Set()
        newSet._data.extend(self._data)
        for el in t:
            newSet.add(el)
        return newSet

    def intersection(self, t):
        newSet = Set()
        for el in self._data:
            if el in t:
                newSet.add(el)
        return newSet

    def difference(self, t):
        newSet = Set()
        newSet._data.extend(self._data)
        for el in t:
            newSet.discard(el)
        return newSet        

    def __iter__(self):
        return _SetIterator(self._data)

    def __repr__(self):
        s = "ListSet("
        sep = ""
        for el in self._data:
            s += sep + repr(el)
            sep = ","
        return s + ")"


class _SetIterator():
    def __init__(self, l):
        self._l = l
        self._current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current < len(self._l):
            entry = self._l[self._current]
            self._current += 1
            return entry
        else:
            raise StopIteration