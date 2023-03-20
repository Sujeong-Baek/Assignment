# https://leetcode.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p=head
        lenth=0        
        while p:
            p=p.next
            lenth+=1

        middle=lenth//2
        while middle>0:
            head=head.next
            middle -=1
        return head