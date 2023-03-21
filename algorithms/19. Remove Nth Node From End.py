# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length=0
        p=head
        sentinel=q=ListNode()
        q.next=head
        while p:
            length+=1
            p=p.next

        count=length-n
        while q and q.next:
            if count!=0:    
                q=q.next
                print(sentinel)      
            else:
                q.next=q.next.next
                print(sentinel)                
            count-=1
        return sentinel.next