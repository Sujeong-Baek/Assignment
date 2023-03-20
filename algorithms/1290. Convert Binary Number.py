# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        p=head
        length=0
        answer=0

        while p:
            p=p.next
            length+=1
        
        exponent=length-1
        while exponent>=0:
            if head.val:
                answer+=2**exponent
            head=head.next
            exponent-=1
        return answer