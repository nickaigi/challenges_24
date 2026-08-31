class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        """
        Given the root of a binary tree, check whether it is a mirror of itself
        i.e symmetric around its center
        """

        def sym(r1: TreeNode | None, r2: TreeNode | None):
            if not r1 and not r2:
                return True

            if not r1 or not r2:
                return False

            if r1.val != r2.val:
                return False

            return sym(r1.left, r2.right) and sym(r1.right, r2.left)

        return sym(root, root)
