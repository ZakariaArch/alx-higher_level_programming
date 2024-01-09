#!/usr/bin/python3
"""Module containing a Square class"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes a square

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.

        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters.

        If the size is 0, it prints an empty line.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
