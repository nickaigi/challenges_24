"""

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""
from typing import List, Optional

class ListNode:
    """
    Definition of a singly-linked list
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        values_one = self.walk(l1)
        values_two = self.walk(l2)
        sum_ = self.str_rep(values_one) + self.str_rep(values_two)
        sum_str = str(sum_)
        for val in sum_str:
            head = self.insert_head(int(val), head)
        return head
    
    def insert_head(self, val: int, head: ListNode) -> ListNode:
        node = ListNode(val)
        node.next = head
        head = node
        return head
    
    def str_rep(self, val: List[int]) -> int:
        res = ''.join([str(i) for i in val])
        return int(res)

    def walk(self, l: ListNode) -> List[int]:
        current = l
        values = []
        while current:
            values.append(current.val)
            current = current.next
        values.reverse()
        return values
