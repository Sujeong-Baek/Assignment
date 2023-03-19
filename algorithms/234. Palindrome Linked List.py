class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        visited=[]
        while head:
            if head in visited:
                return True
            visited.append(head.val)
            head=head.next
        return False

# 1,2,3,1,2,3 => False