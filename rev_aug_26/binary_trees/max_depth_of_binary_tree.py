from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth_dfs(self, root: TreeNode | None) -> int:
        """
        if the current node is null, return 0
        - recursively compute the maximum depth of the left subtree
        - recursively compute the maximum depth of the right subtree
        - return 1 + max(left_depth, right_depth)
        """
        if not root:
            return 0
        left_depth = self.max_depth_dfs(root.left)
        right_depth = self.max_depth_dfs(root.right)

        return 1 + max(left_depth, right_depth)

    def max_depth(self, root: TreeNode | None) -> int:
        """
        Breadth-First Search
        """
        if not root:
            return 0
        height = 0
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            height += 1
        return height
