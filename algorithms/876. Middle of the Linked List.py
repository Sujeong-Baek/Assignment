# https://leetcode.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p=head
        length=0        
        while p:
            p=p.next
            length+=1

        for _ in range(length//2):
            head=head.next
        return head