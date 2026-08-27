class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        """
        If a linked list contains a cycle, traversing the nodes will never reach 'null'

        The slow pointer advances one step at a time, while the fast pointer moves two steps at a time.
        If a cycle exists, the fast pointer will eventually catch up with the slow pointer.

        If 'fast' reaches 'null' or 'fast.next' reaches 'null', the list has no cycle


        This is known as 'Floyd's Cycle Detection Algorithm or the Tortoise and Hare Algorithm
        """
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next

            if slow == fast:
                return True
        return False
