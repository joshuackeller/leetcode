from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Reorder without creating an extra array
# O(n) time
# O(1) space
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # Reorder the list
        cur = head
        while cur and prev:
            cur_temp, prev_temp = cur.next, prev.next
            cur.next = prev
            prev.next = cur_temp
            cur, prev = cur_temp, prev_temp


# Reorder assigning all the nodes to an array
# O(n) time
# O(n) space
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         nodes = []
#         cur = head
#         while cur:
#             nodes.append(cur)
#             cur = cur.next
#
#         end = len(nodes) - 1
#         for front in range(len(nodes) // 2):
#             nodes[end].next = nodes[front].next
#             nodes[front].next = nodes[end]
#             end -= 1
#
#         nodes[len(nodes) // 2].next = None
#
#         return head
