from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_digits(self, node: Optional[ListNode]) -> list[int]:
        res: list[int] = []
        while node:
            res.append(node.val)
            node = node.next

        res.reverse()
        return res

    def build_number(self, num_list: list[int]) -> int:
        num = 0
        return num

    def create_res(self, digits: list[int]) -> ListNode:
        head = ListNode()
        return head

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        d1 = self.get_digits(l1)
        print("d1 =", d1)
        d2 = self.get_digits(l2)
        print("d2 =", d2)


if __name__ == "__main__":
    n1 = ListNode(val=2)
    n2 = ListNode(val=4)
    n3 = ListNode(val=3)
    n1.next = n2
    n2.next = n3

    m1 = ListNode(val=5)
    m2 = ListNode(val=6)
    m3 = ListNode(val=4)
    m1.next = m2
    m2.next = m3

    sol = Solution()
    sol.addTwoNumbers(n1, m1)
