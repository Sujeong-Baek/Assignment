# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        new=ListNode()
        p=new
        while head: 
            if head.val==val:                
                p.next=None
            else:
                p.next=head
                p=p.next
            head=head.next
        return new.next