"""
        *
       ***
      *****
     *******
    *********
   ***********
  *************
 ***************
*****************
        *
"""
import sys

def tree(height: int) -> None:
    length = (height * 2) - 1
    stars = 1
    for _ in range(1, height + 1):
        print(('*' * stars).center(length))
        stars += 2
    print('*'.center(length))


if __name__ == '__main__':
    height: int = 10
    if len(sys.argv) > 1:
        height = int(sys.argv[1])
    tree(height)
