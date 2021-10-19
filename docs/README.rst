README
======

Installation
------------

To use sl29.structures.binarytree, first install it using pip:

.. code-block:: console

   (.venv) $ pip install sl29.structures.binarytree


Usage
-----

Let's start with a manually created tree:

.. code-block:: python

    >>> from sl29.structures import Node, BinaryTree
    >>> n1 = Node('A')
    >>> n2 = Node('B')
    >>> n3 = Node('C')
    >>> n1.set_left(n2)
    >>> n1.set_right(n3)
    >>> t = BinaryTree(n1)
    >>> n1.is_leaf()
    False
    >>> n2.is_leaf()
    True
    >>> t.size()
    3
    >>> t.display()
    A
    ├──B
    └──C


And now let's build our binarytree from a python list:

.. code-block:: python

    >>> l = ["A", ["B"], ["C", [], ["D"]]]
    >>> t = BinaryTree()
    >>> t.import_tree(l)
    >>> t.display()
    A
    ├──B
    └──C
        └──
        └──D

