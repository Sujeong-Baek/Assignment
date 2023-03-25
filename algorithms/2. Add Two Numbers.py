# https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1:ListNode, l2: ListNode) ->ListNode:
        carry=0
        answer=ListNode()
        p=answer
   
        while l1 or l2:
            num=0
            if l1 and l1.val:
                num+=l1.val
            if l1:
                l1=l1.next

            if l2 and l2.val:
                num+=l2.val
            if l2:
                l2=l2.next
            num += carry
            carry, num = divmod(num, 10)
            p.next=ListNode(num)
            p=p.next
        if carry:
            p.next=ListNode(val=1)

        return answer.next
    
    def addTwoNumbers2(self, l1:ListNode, l2: ListNode) ->ListNode:
        carry=0
        answer=ListNode()
        p=answer
        while l1 and l2:
            num = l1.val+l2.val+ carry
            l1=l1.next
            l2=l2.next
            carry, num = divmod(num, 10)
            p.next=ListNode(num)
            p=p.next

        while l1:
            num = l1.val + carry
            carry, num = divmod(num, 10)
            p.next=ListNode(num)
            p=p.next
            l1=l1.next
        while l2:
            num = l2.val + carry
            carry, num = divmod(num, 10)
            p.next=ListNode(num)
            p=p.next
            l2=l2.next
        if carry:
            p.next=ListNode(val=1)
        return answer.next