#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Code très inspiré par l'excellent cours
# https://notebooks.lecluse.fr/python/nsi/terminale/arbres%20binaires/algorithmique/poo/tp/2020/08/16/nsi_t_algo_arbres.html
from io import StringIO
from graphviz import Digraph
from random import randint

class Node:
    """
    a node of a the :class:`sl29.structures.BinaryTree`
    """

    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    def value(self):
        """
        :return: The value of the :class:`sl29.structures.Node`, the type of the value can be anything.
        :rtype: any
        """
        return self._value
    
    def left(self):
        """
        Return the left child of the node or None.
        
        :return: an instance of a node :class:`sl29.structures.Node` or None
        :rtype: :class:`sl29.structures.Node` or None
        """
        return self._left
    
    def set_left(self, node):
        """
        Set the left node.
        
        :param node: an instance of a :class:`sl29.structures.Node`
        :return: None
        """
        self._left = node
        
    def right(self):
        """
        Return the right child of the node or None.
        :return: an instance of a node :class:`sl29.structures.Node` or None
        :rtype: :class:`sl29.structures.Node` or None
        """
        return self._right
    
    def set_right(self, node):
        """
        Set the right node.
        
        :param node: an instance of a :class:`sl29.structures.Node`
        :return: None
        """
        self._right = node
        
    def is_leaf(self):
        """
        :return: True if the node is a leaf, False otherwise.
        :rtype: Boolean
        """
        return self.left() == None and self.right() == None

    def __repr__(self):
        """
        Return the representation of a node
        """
        return str(self.value())
    

class BinaryTree:
    """
    This class represents a :class:`sl29.structures.BinaryTree`.
    """

    def __init__(self, node = None):
        self._root = node

    def root(self):
        """
        Return the root node of the binary tree.
        :return: an instance of a node :class:`sl29.structures.Node` or None
        :rtype: :class:`sl29.structures.Node` or None
        """
        return self._root

    def import_tree(self, table):
        """
        Import a binary tree from a table
        
        >>> t = BinaryTree()
        >>> l = ["A", ["B"], ["C", [], ["D"]]]    
        >>> t.import_tree(l)
        :param table: an instance of a :class:`list`
        :return: None
        """

        def import_table(a_table):
            if a_table == []:
                return None
            if len(a_table) == 1:
                return Node(a_table[0])

            node = Node(a_table[0])
            node.set_left(import_table(a_table[1]))
            if len(a_table) > 2:  # the right tree can be omitted
                node.set_right(import_table(a_table[2]))
            return node

        my_node = import_table(table)
        self._root = my_node

    def show(self):
        """
        Return a graphviz.Digraph instance of the tree.
        """

        def representation(dot, noeud, aretes):
            # Ajoute la représentation du noeud à la représentation dot de l'arbre
            if noeud is not None:
                dot.node(str(id(noeud)), str(noeud.value()))
                # Appel récursif de la fonction representation
                if noeud.left() is not None:
                    representation(dot, noeud.left(), aretes)
                    aretes.append((str(id(noeud)), str(id(noeud.left()))))
                if noeud.right() is not None:
                    representation(dot, noeud.right(), aretes)
                    aretes.append((str(id(noeud)), str(id(noeud.right()))))

        dot = Digraph(comment="Arbre binaire", format='svg')
        aretes = []
        representation(dot, self.root(), aretes)
        dot.edges(aretes)
        dot.view()

    def display(self):
        """
        Print the tree
        >>> t = BinaryTree()
        >>> l = ["A", ["B"], ["C", [], ["D"]]]    
        >>> t.import_tree(l)
        >>> t.display()
        A
        ├──B
        └──C
           └──
           └──D
        """
        def r_print_tree(node, out, prefix=''):
            if node is not None:
                out.write(f"{node.value()}\n")
                if node.left() is not None:
                    if node.right():
                        out.write(prefix + '├──')
                        prefix += '|  '
                    else:
                        out.write(prefix + '└──')
                    r_print_tree(node.left(), out, prefix)
                else:
                    if node.right() is not None:
                        out.write(prefix + '└──\n')
                        prefix += '|  '
                if node.right() is not None:
                    prefix= prefix[0:-3]
                    out.write(prefix + '└──')
                    prefix += '   '
                    r_print_tree(node.right(), out, prefix)

        out = StringIO()
        r_print_tree(self.root(), out)
        print(out.getvalue())
        out.close()

    def size(self):
        """
        Return the size of the tree : the number of nodes in the tree
        
          - 0 for a empty tree
          - 1 for a tree with one node
        >>> t = BinaryTree()
        >>> l = ["A", ["B"], ["C", [], ["D"]]] 
        >>> t.import_tree(l)
        >>> t.size()
        4
        :return: an instance :class:`int`
        :rtype: :class:`int`
        """
        def _size(root):
            if root is None:
                return 0
            else:
                return 1 + _size(root.left()) + _size(root.right())

        return _size(self.root())

    def height(self):
        """
        Return the height of the tree
          
          - -1 for a empty tree
          - 0 for a tree with one Node
        :return: an instance :class:`int`
        :rtype: :class:`int`
        """
        def _height(root):
            if root is None:
                return 0
            else:
                return max(_height(root.left()), _height(root.right())) + 1

        return _height(self.root()) - 1

    def preorder(self):
        """
        Return the preoder values of the binarytree in a list
        :return: an instance :class:`list`
        :rtype: :class:`list`
        """
        def _preorder(node):
            if not node:
                return []
            return [node.value()] + _preorder(node.left()) + _preorder(node.right())
        return _preorder(self.root())

    def postorder(self):
        """
        Return the prostorder values of the binarytree in a list
        :return: an instance :class:`list`
        :rtype: :class:`list`
        """
        def _postorder(node):
            if not node:
                return []
            return _postorder(node.left()) + _postorder(node.right()) + [node.value()]
        return _postorder(self.root())

    def inorder(self):
        """
        Return the inorder values of the binarytree in a list
        :return: an instance :class:`list`
        :rtype: :class:`list`
        """
        def _inorder(node):
            if not node:
                return []
            return _inorder(node.left()) + [node.value()] + _inorder(node.right())
        return _inorder(self.root())




class BinarySearchTree(BinaryTree):
    """A Binary Search Tree"""

    def __init__(self, node = None):
        super().__init__(node = node)
        
    def add(self, value):
        """
        Add a value in the BST.
        
        :param value: the value to add.
        :return: an instance of :class:`sl29.structures.BinarySearchTree`
        :rtype: :class:`sl29.structures.BinarySearchTree`
        """
        def _add(node, value):
            if node is None:
                node = Node(value)
            if value < node.value():
                node.set_left(_add(node.left(), value))
            elif value > node.value():
                node.set_right(_add(node.right(), value))
            return node
        
        self._root = _add(self.root(), value)
        return self
        
    def search(self, value):
        """
        Search for a value in the BST.

        :param value: the value to search for.

        :return: an instance of :class:`sl29.structures.Node` or None if not found.
        :rtype: :class:`sl29.structures.Node` or None
        """
        def _search(node, value):
            if node != None:
                if value == node.value():
                    return node
                elif value < node.value():
                    return _search(node.left(), value)
                else:
                    return _search(node.right(), value)
        return _search(self.root(), value)
