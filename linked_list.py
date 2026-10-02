
class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        Assign the provided 'data' to an instance variable and
        initialize 'next' to None so the node has no successor yet.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        Initialize 'head' to None to represent an empty list.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        Create a new Node with 'data' and insert it at the front of the
        list. This is an O(1) operation: the new node points to the current
        head, then becomes the new head.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        (Optional) Create a new Node with 'data', traverse to the end of the
        list (O(n)) and link the last node to the new node. If the list is
        empty, the new node simply becomes the head.
        """
        new_node = Node(data)
        # Base case: empty list -> the new node is the head.
        if self.head is None:
            self.head = new_node
            return
        # Otherwise walk to the last node and link the new node after it.
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        """
        Use recursion to sum all node data in the list.

        A nested helper walks the list one node at a time:
          * Base case: the current node is None -> nothing left to add (0).
          * Recursive case: node.data + the sum of the remaining nodes.
        """
        def _sum(node):
            # Base case: reached the end of the list.
            if node is None:
                return 0
            # Recursive case: current value plus the rest of the list.
            return node.data + _sum(node.next)

        return _sum(self.head)

    def recursive_reverse(self):
        """
        Reverse the list in-place using recursion.

        A helper tracks the previous node while walking forward:
          * Base case: current is None -> 'prev' is the new head of the
            reversed list.
          * Recursive case: flip current.next to point back at 'prev', then
            recurse with current acting as the new 'prev'.
        """
        def _reverse(prev, current):
            # Base case: no more nodes to process; prev is the new head.
            if current is None:
                return prev
            # Remember the next node before overwriting the pointer.
            next_node = current.next
            # Reverse the link so current points back to the previous node.
            current.next = prev
            # Recurse, moving both pointers one step forward.
            return _reverse(current, next_node)

        self.head = _reverse(None, self.head)

    def recursive_search(self, target):
        """
        Return True if 'target' is found, otherwise False, using recursion.

        A nested helper inspects one node at a time:
          * Base case: current is None -> end reached with no match.
          * Base case: current.data == target -> found it.
          * Recursive case: keep searching the rest of the list.
        """
        def _search(node):
            # Base case: end of the list, target was not present.
            if node is None:
                return False
            # Base case: match found.
            if node.data == target:
                return True
            # Recursive case: check the remaining nodes.
            return _search(node.next)

        return _search(self.head)

    def display(self):
        """
        Print the contents of the list for debugging.

        Traverse from 'head', collect each node's data and print it in the
        format 'val -> val -> val -> None'. The formatted string is also
        returned so callers/tests can reuse it.
        """
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        values.append("None")
        formatted = " -> ".join(values)
        print(formatted)
        return formatted
