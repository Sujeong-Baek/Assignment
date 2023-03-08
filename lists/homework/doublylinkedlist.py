
class EmptyListError(Exception):
  pass

class Node:
  def __init__(self, el, next=None, prev=None):
    self.el = el
    self.next = next
    self.prev = prev

  def __repr__(self):
    return "<" + repr(self.el) + ">"  



class DoublyLinkedList:
  def __init__(self):
    self._front = Node(None)
    self._rear = Node(None, prev=self._front)
    self._front.next = self._rear
  
  def is_empty(self):
    return self._front.next == self._rear

  def first(self):
    if self.is_empty():
      raise EmptyListError
    return self._front.next

  def last(self):
    if self.is_empty():
      raise EmptyListError
    return self._rear.prev

  def __repr__(self):
    res = "["
    p = self._front.next
    while p != self._rear:
      res += str(p.el)
      if p.next != self._rear:
        res += ", "
      p = p.next
    res += "]"
    return res

  def __len__(self):
    p = self._front.next
    count = 0
    while p != self._rear:
      count += 1
      p = p.next
    return count

  def insert_after(self, n, el):
    p = Node(el, n.next, n)
    n.next.prev = p
    n.next = p

  def prepend(self, el):
    self.insert_after(self._front, el)
  
  def append(self, el):
    self.insert_after(self._rear.prev, el)

  def remove(self, n):
    n.prev.next = n.next
    n.next.prev = n.prev

  def find_first(self, x):    
    p=self._front.next
    while p != self._rear and p.el !=x:
    # while p.el != x and p is not None:
      p=p.next
    return p if p != self._rear else None

  def find_last(self, x):
    p=self._rear.prev
    while p != self._front and p.el != x:
        p=p.prev
    return p if p != self._front else None

  def count(self, x):
    count=0
    p=self._front.next
    while p != self._rear:
      if p.el == x:
        count+=1
      p=p.next
    return count

  def remove_first(self, x):
    node=self.find_first(x) # 99
    if not node:
      return    
    node.prev.next=node.next
    node.next.prev=node.prev
    

  def remove_last(self, x):
    node=self.find_last(x)
    if not node:
      return
    node.prev.next=node.next
    node.next.prev=node.prev

  def remove_all(self, x): # x = 3
    node=self._front.next
    while node != self._rear: # [1,2,,5,3,5,3,3,]
      if node.el==x:
        self.remove(node)
      node=node.next


  def takeout(self, n, m):
    answer=DoublyLinkedList()
    n.prev.next=m.next
    m.next.prev=n.prev
    answer._front.next=n
    n.prev=answer._front
    answer._rear.prev=m
    m.next=answer._rear
   
    return answer

