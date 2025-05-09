# Binary Search Tree (BSTs)
from typing import Optional, Self

class TreeNode:
    def __init__(self, val: int, left: Optional[Self]=None, right: Optional[Self]=None) -> None:
        self.val = val
        self.right = left
        self.left = right

    def __str__(self) -> str:
        return str(self.val)

def in_order(node: Optional[TreeNode]) -> None:
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)



if __name__ == '__main__':
    # create the following Tree
    #            5
    #        1               8
    #  -1        3      7          9
    a = TreeNode(5)
    b = TreeNode(1)
    c = TreeNode(8)
    d = TreeNode(-1)
    e = TreeNode(3)
    f = TreeNode(7)
    g = TreeNode(9)

    a.left, a.right = b, c
    b.left, b.right = d, e
    c.left, c.right = f, g
    print('\n================== In-Order BST ===================')
    in_order(a)

