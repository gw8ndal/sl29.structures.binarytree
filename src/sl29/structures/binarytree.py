#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Code très inspiré par l'excellent cours
# https://notebooks.lecluse.fr/python/nsi/terminale/arbres%20binaires/algorithmique/poo/tp/2020/08/16/nsi_t_algo_arbres.html
from io import StringIO
from graphviz import Digraph

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
        if self.left() == None and self.right() == None:
            return True
        else:
            return False

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
                dot.node(str(id(noeud)), str(noeud.value))
                # Appel récursif de la fonction representation
                if noeud.left() is not None:
                    representation(dot, noeud.left(), aretes)
                    aretes.append((str(id(noeud)), str(id(noeud.left()))))
                if noeud.right() is not None:
                    representation(dot, noeud.right(), aretes)
                    aretes.append((str(id(noeud)), str(id(noeud.right()))))

        dot = Digraph(comment="Arbre binaire", format='svg')
        aretes = []
        representation(dot, self._root, aretes)
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
            out.write(node.value()+'\n')
            if node.left() is not None:
                out.write(prefix + '├──')
                prefix += '|  '
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
        def _size(node):
            if node == None:
                return 0
            else:
                return 1 + _size(node.left()) + _size(node.right())
        
        return _size(self.root())

    def height(self):
        """
        Return the height of the tree
          
          - -1 for a empty tree
          - 0 for a tree with one Node

        :return: an instance :class:`int`
        :rtype: :class:`int`
        """
        
        
        
        def _height(node):
            if node == None:
                return -1
            else:
                return 1 + max(_height(node.left()), _height(node.right()))
        
        return _height(self.root())

    def preorder(self):
        """
        Returns the path of the tree
        empty list for an empty tree
        """
        def _preorder(node, result=None):
            if result == None:
                result = []
            print(result)
            if node != None:
                result.append(node.value())
                if node.left():
                    _preorder(node.left(), result)
                if node.right():
                    _preorder(node.right(), result)
            return result
               
        return _preorder(self.root())

    def postorder(self):
        """
        Returns the path of the tree
        empty list for an empty tree
        """
        def _postorder(node, result=None):
            if result == None:
                result = []
            print(result)
            if node != None:
                if node.left():
                    _postorder(node.left(), result)
                if node.right():
                    _postorder(node.right(), result)
                result.append(node.value())
            return result
               
        return _postorder(self.root())

    def inorder(self):
        """
        Returns the path of the tree
        empty list for an empty tree
        """
        def _inorder(node, result=None):
            if result == None:
                result = []
            print(result)
            if node != None:
                if node.left():
                    _inorder(node.left(), result)
                result.append(node.value())
                if node.right():
                    _inorder(node.right(), result)
                
            return result
               
        return _inrder(self.root())




class BinarySearchTree(BinaryTree):
    """A Binary Search Tree"""

    def __init__(self, node = None):
        super().__init__(node = node)

    def add(self, value):
        """
        Add a value in the BST

        :param value: the value to add.

        :return: an instance of :class:`sl29.structures.BinarySearchTree`
        :rtype: :class:`sl29.structures.BinarySearchTree`
        """
        def _add(root, value):
            if root == None:
                _add(self.root, value)
            if value < root.value():
                if not root.left():
                    root.set_left(value)
                else:
                    _add(root.left(), value)
            if value > root.value():
                if not root.right():
                    root.set_right(value)
                else:
                    _add(root.right(), value)
            return root

        self._root = _add(self.root(), value)
        return self









































