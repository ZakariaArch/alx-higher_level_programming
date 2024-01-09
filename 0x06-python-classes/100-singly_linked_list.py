#!/usr/bin/python3

"""It defines classes for a singly linked listi."""


class Node:
    """Represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a node with given data and next_node.

        Args:
            data (int): The data for the node.
            next_node (Node, optional): The next node in the linked list.
                                        Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not
                       a Node object.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node.

        Returns:
            int: The data of the node.

        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node.

        Args:
            value (int): The new data for the node.

        Raises:
            TypeError: If value is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node in the linked list.

        Returns:
            Node: The next node in the linked list.

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node in the linked list.

        Args:
            value (Node): The new next node in the linked list.

        Raises:
            TypeError: If value is not a Node object.

        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new node into the correct
           sorted position in the list (increasing order).

        Args:
            value (int): The value for the new node.

        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and \
                value >= current.next_node.data:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list."""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip("\n")
