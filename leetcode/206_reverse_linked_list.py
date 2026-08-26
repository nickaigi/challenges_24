class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        """
        Time: O(n)
        Space: O(1)
        """
        prev = None  # previous
        curr = head  # current

        while curr:
            temp = curr.next  # create a temp node to hold the next node
            curr.next = prev  # reverse the pointer of current to point to prev
            prev = curr  # convert the prev to be curr
            curr = temp  # advance curr
        return prev
