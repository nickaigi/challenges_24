class Node:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    """
    A singly-linked list implementation.
    """
    def __init__(self):
        self.head = None

    def __repr__(self) -> str:
        """
        Returns a string representation of the entire list
        for easier debugging and visualization.
        """
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.data))
            curr = curr.next
        return " -> ".join(values)

    def get(self, index: int) -> int:
        """
        Retrieve the data of the node at a given index (0-based).
        Raises IndexError if the index is out of range.
        """
        count = 0
        curr = self.head
        while curr and count != index:
            curr = curr.next
            count += 1
        if curr is None:
            raise IndexError("Index out of range.")
        return curr.data

    def insertHead(self, val: int) -> None:
        """
        Insert a new node containing 'val' at the head of the list.
        """
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head

    def insertTail(self, val: int) -> None:
        """
        Insert a new node containing 'val' at the tail of the list.
        """
        new_tail = Node(val)
        if not self.head:
            # If the list is empty, new node becomes the head.
            self.head = new_tail
            return

        curr = self.head
        # Traverse to the last node.
        while curr.next:
            curr = curr.next
        curr.next = new_tail

    def remove(self, index: int) -> bool:
        """
        Remove the node at the given index (0-based).
        Returns True if removal succeeded; False if index is invalid.
        """
        if self.head is None:
            return False  # List is empty

        # Special case: removing the head
        if index == 0:
            self.head = self.head.next
            return True

        count = 0
        curr = self.head
        prev = None

        # Traverse until you reach the node to remove
        while curr and count != index:
            prev = curr
            curr = curr.next
            count += 1

        if curr is None:
            # Index out of range
            return False

        # Bypass the node to remove it
        prev.next = curr.next
        return True

    def getValues(self) -> list:
        """
        Return a list of all node data in the linked list.
        """
        values = []
        curr = self.head
        while curr:
            values.append(curr.data)
            curr = curr.next
        return values


if __name__ == "__main__":
    # Example usage:
    linked_list = LinkedList()

    # Insert at head
    linked_list.insertHead(10)
    linked_list.insertHead(20)
    linked_list.insertHead(30)
    print("After insertHead calls:", linked_list)  # 30 -> 20 -> 10

    # Insert at tail
    linked_list.insertTail(40)
    linked_list.insertTail(50)
    print("After insertTail calls:", linked_list)  # 30 -> 20 -> 10 -> 40 -> 50

    # Remove at index 2
    linked_list.remove(2)
    print("After remove(2):", linked_list)  # 30 -> 20 -> 40 -> 50

    # Get values
    print("getValues():", linked_list.getValues())  # [30, 20, 40, 50]

    # Access node at index 1
    print("get(1):", linked_list.get(1))  # 20
