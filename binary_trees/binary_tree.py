# Binary Tree
from typing import Optional, Self
from collections import deque


class TreeNode:
    def __init__(self, val: int, left: Optional[Self]=None, right: Optional[Self]=None) -> None:
        self.val = val
        self.right = left
        self.left = right

    def __str__(self) -> str:
        return str(self.val)


def pre_order(node: Optional[TreeNode]):
    """
    Recursive Pre-Order Traversal (DFS) Time: O(n), Space: O(n)
    """
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)


def in_order(node: Optional[TreeNode]):
    """
    Recursive In-Order Traversal (DFS) Time: O(n), Space: O(n)
    """
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)


def post_order(node: Optional[TreeNode]):
    """
    Recursive Post-Order Traversal (DFS) Time: O(n), Space: O(n)
    """
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node)


def pre_order_iterative(node: TreeNode):
    stk = [node]

    while stk:
        node = stk.pop()
        if node.right: stk.append(node.right)
        print(node)
        if node.left: stk.append(node.left)


def level_order(node: Optional[TreeNode]):
    """
    Level Order Traversal (BFS) Time: O(n), Space: O(n)
    """
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node and node.left:
            q.append(node.left)
        if node and node.right:
            q.append(node.right)


def search(node: Optional[TreeNode], target: int) -> bool:
    if not node:
        return False
    if node.val == target:
        return True
    return search(node.left, target) or search(node.right, target)


if __name__ == '__main__':
    # create the following Tree
    #         1
    #    2        3
    # 4    5   10

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(10)

    a.left = b
    a.right = c

    b.left = d
    b.right = e

    c.left = f

    print(a)
    print('\n================== Pre-Order ==================')
    pre_order(a)
    print('\n================== In-Order ===================')
    in_order(a)
    print('\n================== Post-Order =================')
    post_order(a)
    print('\n================== Pre-Order Iterative =========')
    pre_order_iterative(a)
    print('\n================== Level Order =================')
    level_order(a)
    print('\n================== Search for 10 in the tree using DFS ============')
    print(f"search(node, 10) => {search(a, 10)}")
