
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
    index=0

    if p.el == x:
      return index
    
    if p.el != x:
      while p.el !=x and p is not None:
        index += 1
        p=p.next
        if p is None:
          return -1
      return index

  def find_last(self, x):
    p=self._rear.prev
    index=len(self)-1

    if p.el == x :
      return index
    
    if p.el != x:
      while p.el != x and p is not None:
        index -= 1
        p=p.prev
        if p is None:
          return -1
      return index

  def count(self, x):
    count=0
    p=self._front.next
    while p != self._rear:
      if p.el == x:
        count+=1
      p=p.next
    return count

  def remove_first(self, x):
    count=self.find_first(x)
    p=self._front.next
    while count>0 :
      p=p.next
      count-=1
    p.prev.next=p.next
    p.next.prev=p.prev

  def remove_last(self, x):
    count=self.find_last(x)
    p=self._front.next
    while count>0:
      p=p.next
      count-=1
    p.prev.next=p.next
    p.next.prev=p.prev

  def remove_all(self, x):
    while self.find_first(x) != -1:
      self.remove_first(x)

  def takeout(self, n, m):
    answer=DoublyLinkedList()
    n_count=n
    m_count=m-n+1
    p=self._front.next
    while n_count>0:
      p=p.next
      n_count-=1
    p.prev.next=p.next
    p.next.prev=p.prev
    while m_count>0:
      answer.append(p.el)
      p.prev.next=p.next
      p.next.prev=p.prev
      p=p.next
      m_count-=1
    return answer


