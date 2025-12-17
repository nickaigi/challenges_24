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


def heapsort(arr):
    """
    Heap Sort
    Time: O(n log n), Space: O(n)
    NOTE: O(1) Space is possible via swapping, but this is complex
    """
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn

    return new_list


if __name__ == "__main__":
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
    min_element = heapq.heappop(data)  # -7

    # Heap Push Pop: Time O(log n)
    heapq.heappushpop(data, 99)

    # Peak at Min: Time O(1)
    # Just get the heap[0]
    print(data[0])

    # Max Heap
    data_max = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
    n = len(data_max)
    for i in range(n):
        data_max[i] = -data_max[i]  # Multiply everything with -1

    heapq.heapify(data_max)  # [-12, -9, -10, -8, -2, -5, -1, -3, 0, 4]
    largest = -heapq.heappop(data_max)  # 12

    heapq.heappush(data_max, -7)  # insert 7 into max heap

    # Building a heap from scratch - Time: O(n long n)
    # Slower than heapq.heapify() which takes Time: O(n)
    c = [-5, 4, 2, 1, 7, 0, 3]
    heap_example = []
    for x in c:
        heapq.heappush(heap_example, x)
        print(heap_example, len(heap_example))

    # Putting tuples of items on the heap
    # We shall use a frequency counter example
    D = [5, 4, 3, 5, 4, 3, 5, 5, 4]
    from collections import Counter

    counter = Counter(D)  # Counter({5: 4, 4: 3, 3: 2})

    heap = []  # heap to store our frequency counter

    # we could add the items to a heap
    for k, v in counter.items():
        heapq.heappush(heap, (v, k))

    print(heap)  # [(2, 3), (4, 5), (3, 4)]  Smallest freq shows up ontop
