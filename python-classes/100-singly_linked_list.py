#!/usr/bin/python3
"""Defines a Node and SinglyLinkedList classes.
"""


class Node:
    """
    A Node represents ONE item in the linked list.

    Each node stores:
    1. data       -> the value inside the node
    2. next_node  -> reference to the next node

    Example:

        node1 -> node2 -> node3 -> None
    """

    def __init__(self, data, next_node=None):
        """
        Create a new node.

        Args:
            data (int): value stored in the node
            next_node (Node): next node in the list
        """

        # Use setters for validation
        self.data = data
        self.next_node = next_node

    # ---------------- DATA PROPERTY ---------------- #

    @property
    def data(self):
        """
        Getter for node data.

        Returns:
            int: value stored in the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for node data.

        Makes sure data is an integer.
        """

        if type(value) is not int:
            raise TypeError("data must be an integer")

        self.__data = value

    # ---------------- NEXT NODE PROPERTY ---------------- #

    @property
    def next_node(self):
        """
        Getter for next_node.

        Returns:
            Node: next node in the list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for next_node.

        next_node must be:
        - another Node object
        OR
        - None
        """

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


# =========================================================


class SinglyLinkedList:
    """
    Creates and manages a singly linked list.

    The list keeps track of:
        __head -> first node in the list

    Example:

        head
         ↓
        [2] -> [5] -> [10] -> None
    """

    def __init__(self):
        """
        Create an empty linked list.

        __head is None because list starts empty.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new node in sorted order.

        Example:

            Current list:
            1 -> 3 -> 7

            Insert 5:

            Result:
            1 -> 3 -> 5 -> 7
        """

        # Create new node
        new_node = Node(value)

        # CASE 1:
        # List is empty
        # OR
        # New value should become first element
        if self.__head is None or value < self.__head.data:

            # New node points to current head
            new_node.next_node = self.__head

            # Head becomes new node
            self.__head = new_node

            return

        # Start from first node
        current = self.__head

        # Move through the list until:
        # - next node is None
        # OR
        # - next node value is bigger than new value
        while current.next_node is not None and \
                current.next_node.data < value:

            current = current.next_node

        # Insert node in correct position

        # New node points to next node
        new_node.next_node = current.next_node

        # Current node points to new node
        current.next_node = new_node

    def __str__(self):
        """
        Return the linked list as a string.

        Each node value appears on a new line.
        """

        values = []

        # Start from head
        current = self.__head

        # Traverse the linked list
        while current is not None:

            # Add current node data to list
            values.append(str(current.data))

            # Move to next node
            current = current.next_node

        # Join all values with newline
        return "\n".join(values)
