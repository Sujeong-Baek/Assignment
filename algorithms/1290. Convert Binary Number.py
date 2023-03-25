# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        p=head
        answer=0

        while p:
            answer*=2
            answer+=p.val # 2 + 2 = 4
            p=p.next
        return answer

#"12345" -> 12345
# 1 -> 10 + 2 -> 120 + 3 -> 1230 + 4 -> 12340 + 5
# 12345

# 101
# 1 -> 1*2 + 0 -> 2*2 + 1