from typing import Optional

"""

    #Reverse Linked List - 206

    1. Save cur.next in temp.
    2. Point cur.next to prev (reverse the link).
    3. Move prev forward to cur.
    4. Move cur forward to temp.

    Time complexity: O(n)
    Space complexity: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev


def createLinkedList(nums):
    dummy = ListNode()
    cur = dummy

    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next

    return dummy.next


def printLinkedList(head):
    values = []

    while head:
        values.append(str(head.val))
        head = head.next

    return " -> ".join(values)


# test cases
solution = Solution()

head1 = createLinkedList([1, 2, 3, 4, 5])
print(printLinkedList(solution.reverseList(head1)))
# 5 -> 4 -> 3 -> 2 -> 1

head2 = createLinkedList([1, 2])
print(printLinkedList(solution.reverseList(head2)))
# 2 -> 1

head3 = createLinkedList([])
print(printLinkedList(solution.reverseList(head3)))
# ""

head4 = createLinkedList([7])
print(printLinkedList(solution.reverseList(head4)))
# 7
