# https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1:ListNode, l2: ListNode) ->ListNode:
        nextnum=0
        answer=ListNode()
        p=answer
   
        while l1 or l2:
            addnum=0
            num=0            
            if l1 and l1.val:
                addnum+=l1.val
            if l1:
                l1=l1.next

            if l2 and l2.val:
                addnum+=l2.val
            if l2:
                l2=l2.next
            
            num+=(addnum+nextnum)            
            p.next=ListNode(val=num%10)
            p=p.next
           
            if num>=10:
                nextnum=1
            else:
                nextnum=0
                
        if nextnum:
            p.next=ListNode(val=1)

        return answer.next