# Binary Tree
from typing import Optional, Self


class TreeNode:
    def __init__(self, val: int, left: Optional[Self]=None, right: Optional[Self]=None) -> None:
        self.val = val
        self.right = left
        self.left = right

    def __str__(self) -> str:
        return str(self.val)


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
