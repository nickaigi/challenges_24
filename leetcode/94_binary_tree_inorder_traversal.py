class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traversal_recursive(self, root: TreeNode | None) -> list[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        res = []

        def inorder(root: TreeNode | None):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res

    def inorder_traversal_iterative(self, root: TreeNode | None) -> list[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        res = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res
