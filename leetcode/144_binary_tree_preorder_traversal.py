class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorder_traversal_recursive(self, root: TreeNode | None) -> list[int]:
        res = []

        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return res

    def preorder_traversal_iterative(self, root: TreeNode | None) -> list[int]:
        """
        Time: O(n)
        Space: O(height)   height of the tree
        """
        res = []
        stack = []
        curr = root
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return res
