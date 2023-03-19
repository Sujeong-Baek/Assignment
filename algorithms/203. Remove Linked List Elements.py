# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        p = sentinel =ListNode()
        p.next = head # []
        while p and p.next: # 0
            if p.next.val==val:                
                p.next=p.next.next
            else:
                p=p.next
        return sentinel.next