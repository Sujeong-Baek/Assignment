# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) ->ListNode:
        answer=None
        q = head
        while q:
            p=ListNode(val=q.val,next=answer)
            q=q.next
            answer=p
        return answer

s = Solution()
node = s.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))))

p = node
while p:
    print(p.val)
    p = p.next