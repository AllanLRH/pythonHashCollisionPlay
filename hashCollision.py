#!/usr/bin/env python
# -*- coding: utf8 -*-


class MyObject():
    """Object with __eq__ and __hash__ methods."""

    def __init__(self, id_int):
        super(MyObject, self).__init__()
        self.id_int = id_int

    def __eq__(self, other):
        return self.id_int == other.id_int

    def __hash__(self):
        """Return 0 for even numbers and 1 for uneven numbers.
        It's thus easy to create a hash collision."""
        return self.id_int % 2

    def __repr__(self):
        return str(self.id_int)


a = MyObject(1)
b = MyObject(2)
c = MyObject(3)

# Test the __eq__ method
assert not a == b
assert not a == c
assert not b == c

# Test the __hash__ method
assert not hash(b) == hash(c)
assert hash(a) == hash(c)

my_set = set()
my_set.add(a)
my_set.add(b)
my_set.add(c)

print(my_set)  # prints: {2, 1, 3}

