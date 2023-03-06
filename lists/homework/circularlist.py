#
# A circular doubly-linked list
#

class Node:
    def __init__(self, el, next=None, prev=None):
        self.el = el
        self.next = next
        self.prev = prev

    def __repr__(self):
        return "<" + repr(self.el) + ">"


class CircularList:
    def __init__(self, el):
        self.front=Node(el)
        self.rear=self.front

        self.front.next=self.rear
        self.front.prev=self.rear
        self.rear.next=self.front
        self.rear.prev=self.front

    def first(self):
        return self.front

    def __repr__(self):
        res="["
        p=self.front
        while p!=self.rear:
            res+=p.el
            if p.next != self.front:
                res+=", "
            p=p.next
        res+=p.el+"]"
        return res

    def remove(self, p):
        p.prev.next=p.next
        p.next.prev=p.prev
        if p==self.rear:
            self.rear=p.prev
        elif p==self.front:
            self.front=p.next


    def __len__(self):
        count=1
        p=self.front
        while p!= self.rear:
            count+=1
            p=p.next
        return count


    def insert(self, p, el):
        el=Node(el,)
        raise NotImplementedError

    def append(self, x):
        x=Node(x, self.front, self.rear)
        self.front.prev=x
        self.rear.next=x
        self.rear=x


