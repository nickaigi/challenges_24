"""
21. Merge two sorted lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Explanation of the Optimized Solution:
Time Complexity: O(n+m), where n and m are the lengths of the two lists. This is because we traverse each list once.
Space Complexity: O(1), as we are only using a constant amount of extra space (the dummy node and current pointer).
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify the merging process
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append the remaining nodes from list1 or list2
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        # The merged list starts at dummy.next
        return dummy.next
