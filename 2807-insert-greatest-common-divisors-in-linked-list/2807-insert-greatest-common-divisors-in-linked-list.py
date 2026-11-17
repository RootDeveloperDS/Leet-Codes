# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        insert_next = head.next  # deposit the actual next
        # add new node bw the current head and head.next in next element.
        head.next = ListNode(val = gcd(head.val, head.next.val), next = insert_next)

        # since we added interm node, so jump by 2 steps for next operating node.
        self.insertGreatestCommonDivisors(head.next.next)

        return head
