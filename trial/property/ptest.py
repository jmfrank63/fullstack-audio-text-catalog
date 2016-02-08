import random

class MyList():
    def __init__(self):
        self._myList = [1, 2, 3, 4, 5]

    @property
    def myList(self):
        return self._myList

    @myList.setter
    def myList(self, val):
        self._myList = val

    @myList.getter
    def myList(self):
        return self._myList[:]
        
    def append(self, val):
        self.myList = self.myList + [val]
        return self.myList

    def extend(self, val):
        return self.myList.extend(val)

l = MyList()

s = l.myList
random.shuffle(s)

print s
print l.myList