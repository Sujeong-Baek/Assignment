#
# A circular doubly-linked list
#
class ValueError(Exception):
    pass

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
        self.front.next=self.front
        self.front.prev=self.front

    def first(self):
        return self.front

    def __repr__(self):
        res="["
        p=self.front
        while True:
            res+=p.el
            if p.next != self.front:
                res+=", "
            p=p.next
            if p==self.front:
                res+="]"
                break
        return res
    
    def remove(self, p):
        if len(self)==1:
            raise ValueError("Cannot remove only node of a CircularList")
        
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
        el=Node(el)
        p.prev.next=el
        el.prev=p.prev
        el.next=p
        p.prev=el
        

    def append(self, x):
        x=Node(x)
        self.front.prev=x
        self.rear.next=x
        x.prev=self.rear
        x.next=self.front
        self.rear=x