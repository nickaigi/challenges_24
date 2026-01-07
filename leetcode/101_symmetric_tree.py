from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(
            node_one: Optional[TreeNode], node_two: Optional[TreeNode]
        ) -> bool:  # node_one: left, node_two: right
            if not node_one and not node_two:  # both nodes are None
                return True

            if not node_one or not node_two:  # one of the nodes is None
                return False

            if node_one.val != node_two.val:
                return False

            return is_mirror(node_one.left, node_two.right) and is_mirror(
                node_one.right, node_two.left
            )

        return is_mirror(root, root)
