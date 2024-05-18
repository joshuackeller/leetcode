from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(n1: Optional[ListNode], n2: Optional[ListNode]) -> ListNode:
            if not n1:
                return n2
            elif not n2:
                return n1
            elif n1.val < n2.val:
                parent = n1
                n1 = n1.next
            else:
                parent = n2
                n2 = n2.next

            node = parent

            while n1 and n2:
                if n1.val < n2.val:
                    node.next = n1
                    n1 = n1.next
                else:
                    node.next = n2
                    n2 = n2.next
                node = node.next

            if n1:
                node.next = n1
            else:
                node.next = n2

            return parent

        def solve(lists, s, e):
            if e - s <= 1:
                return lists[s]
            elif e - s == 2:
                return merge(lists[s], lists[s + 1])
            else:
                m = (e + s) // 2
                list1 = solve(lists, s, m)
                list2 = solve(lists, m, e)
                return merge(list1, list2)

        if len(lists) == 0:
            return
        else:
            return solve(lists, 0, len(lists))


list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))
lists = [list1, list2, list3]


s = Solution()

node = s.mergeKLists(lists)

while node:
    print(node.val)
    node = node.next
