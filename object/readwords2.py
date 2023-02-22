# readwords2.py
# read many words from a file and store using an array

import time
# from array import Array

fname = r"C:\Users\zxcwl\Desktop\Python-assignment\object\words-1000.txt"

class Array():
    """An array with size slots"""

    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        self._elements = [None] * size

    def __len__(self):
        return self._size

    def __getitem__(self, i):
        assert i >= 0 and i < len(self), "Array subscript out of range"
        return self._elements[i]

    def __setitem__(self, i, v):
        assert i >= 0 and i < len(self), "Array subscript out of range"
        self._elements[i] = v

    def __repr__(self):
        s = "Array("
        sep = ""
        for i in range(len(self)):
            s += sep + repr(self._elements[i])
            sep = ", "
        s += ")"
        return s

    def __iter__(self):
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration

class GrowArray():
    def __init__(self):
        self._a = Array(32)
        self._size = 0

    def __len__(self):
        return self._size

    def __getitem__(self, i):
        return self._a[i]

    def append(self, el):
        if self._size == len(self._a):
            oldA = self._a
            n = len(oldA)
            self._a = Array(2* n)
            for i in range(n):
                self._a[i] = oldA[i]
        self._a[self._size] = el
        self._size += 1


def readWords():
    f = open(fname, "r", encoding="utf-8")
    words = GrowArray()
    for line in f.readlines():
        s = line.strip()
        words.append(s)
    f.close()
    return words


print("Starting...")
t0 = time.time()
words = readWords()
t1 = time.time()
print("Reading all %d words took %g seconds\n" % (len(words), t1 - t0))

print("The first ten words are:")
for i in range(10):
    print(words[i])
