from __future__ import annotations
from abc import ABC, abstractclassmethod
from typing import List

class Component(ABC):
    """
    Common operations for leaf classes and composite class
    """

    @property
    def parent(self):
        return self.parent

    @parent.setter
    def parent(self, parent: Component)
        """
        Optionally, the base Component can declare an interface for setting and
        accessing a parent of the component in a tree structure. It can also
        provide some default implementation for these methods.
        """
