"""
This module contains a basic accumulator class.
Its purpose is to show how to use the pytest framework
"""

# -----------------------------
# Class: Accumulator
# -----------------------------

class Accumulator:

    # _count private for prefix '_'
    def __init__(self):
        self._count = 0

    # in Python properties control how callers can get and set values
    @property
    def count(self):
        return self._count

    def add(self, more=1):
        self._count += more