import heapq

"""
A heap is a tree-based data structure that satisfies the heap property.
    - max heap: for any given node C, if P is the parent node of C, then the 
      key( the value) of P is greater than or equal to the key of C.
    - min heap: the key of P is less than or equal to the key of C.
    - The node at the "top" of the heap is called the root node

The heap is an efficient implementation of a ADT called a "Priority Queue"

Heaps are usually implemented with an array as follows:
    - each element in the array represents a node of the heap
    - the parent/child relationship is defined implicitly by the elements' indices in the array.

In the array, the first index contains the root element. The next two indices contain the root's children.

    Given a node at index i, the children are at indices: 2i + 1 and 2i + 2


In python, all heaps are min heaps.

- heappop(heap) : pops the value and heapify's the heap
- heappush(heap) : pushes a value into the heap and heapify's the heap
"""


if __name__ == '__main__':
    # Build Min Heap (heapify)
    # Time: O(n), Space: O(1)

    data = [10, 20, 43, 1, 2, 65, 17, 2, 3, 1]
    heapq.heapify(data)
    print(data)  # [1, 1, 17, 2, 2, 65, 43, 10, 3, 20]
    # the lowest value item (highest priority)

    # Heap Push (Insert element)
    # Time: O(log n) time taken to re-order the tree
    heapq.heappush(data, -7)  # [-7, 1, 17, 2, 1, 65, 43, 10, 3, 20, 2]

    # Heap Pop(Extract min)
    # Time: O(log n)
