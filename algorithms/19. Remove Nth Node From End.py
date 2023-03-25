# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p=q=head
        for _ in range(n):
            q=q.next #q=3
        if not q:
            return head.next
        while q.next:
            p=p.next #14  25 36
            q=q.next
        p.next=p.next.next  #4 =6
        return head


# 1,2,3,4,5, 6 // 3
#     p      q
# 1,2,3,5,6

# 1 // 1