from __future__ import annotations
from abc import ABC, abstractmethod
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

    """
    In some cases, it would be beneficial to define the child-management
    operations right in the base Component class. This way, you won't need to
    expose any concrete component classes to the client code, even during the
    object tree assembly. The downside is that these methods will be empty for
    the leaf-level components.
    """

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def is_composite(self):
        """
        You can provide a method that lets the client code figure out whether a
        component can bear children.
        """

        return False

    @abstractclassmethod
    def operation(self):
        """
        The base Component may implement some default behavior or leave it to
        concrete classes (by declaring the method containing the behavior as
        "abstract").
        """
        pass


    class Leaf(Component):
        """
        The Leaf class represents the end objects of a composition. A leaf can't
        have any children.

        Usually, it's the Leaf objects that do the actual work, whereas Composite
        objects only delegate to their sub-components.
        """
        def operation(self):
            return "Leaf"



    class Composite(Component):
        """
        The Composite class represents the complex components that may have
        children. Usually, the Composite objects delegate the actual work to their
        children and then "sum-up" the result.
        """
        def __init__(self):
            self._children = []

        def add(self, component):
            self._children.append(component)
            component.parent = self

        def remove(self, component: Component) -> None:
            self._children.remove(component)
            component.parent = None

        def is_composite(self) -> bool:
            return True

        def operation(self):
            """
            The Composite executes its primary logic in a particular way. It
            traverses recursively through all its children, collecting and summing
            their results. Since the composite's children pass these calls to their
            children and so forth, the whole object tree is traversed as a result.
            """
            results = []
            for child in self._children:
                results.append(child.operation())
            return f"Branch({'+'.join(results)}"

def client_code(component):
    print(f"RESULT: {component.operation()}", end="")

def client_code2(component1, component2):
    if component1.is_composite():
        component1.add(component2)
    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":
    # This way the client code can support the simple leaf components...
    simple = Leaf()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as the complex composites.
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)
