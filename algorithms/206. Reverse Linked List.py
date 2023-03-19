# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) ->ListNode:
        answer=None

        while head:
            p=head           
            head=head.next            
            p.next = answer            
            answer=p          
        return answer