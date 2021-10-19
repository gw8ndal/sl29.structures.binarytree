#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from sl29.structures import BinaryTree, Node
from sl29.structures.samples import tree1, tree2

class BinaryTreeTests(unittest.TestCase):
    """
    A class to test the Node class
    """
    def setUp(self):
        """
        This is called before each test
        """
        pass
    
    def tearDown(self):
        """
        call this at the end of each tests, wheter the test fail or not
        """
        pass

    def test_size1(self):
        # test avec un arbre vide
        a = BinaryTree()
        s = a.size()
        expected = 0
        self.assertEqual(s, expected, "La taille de l'arbre vide devrait être {expected} mais elle vaut {s}.")

    def test_size2(self):
        # test avec un arbre qui ne contient qu'un seul noeud
        n = Node('N1')
        a = BinaryTree(n)
        s = a.size()
        expected = 1
        self.assertEqual(s, expected, "La taille de l'arbre devrait être {expected} mais elle vaut {s}.")

    def test_size3(self):
        # test avec l'arbre : racine -> fils droit + gauche
        n1 = Node('Root')
        n2 = Node('Left')
        n3 = Node('Right')
        n1.set_left(n2)
        n1.set_right(n3)
        a = BinaryTree(n1)
        s = a.size()
        expected = 3
        self.assertEqual(s, expected, "La taille de l'arbre devrait être {expected} mais elle vaut {s}.")

    def test_size4(self):
        # test avec l'arbre : racine -> fils gauche -> fils droit 
        n1 = Node('Root')
        n2 = Node('Left')
        n3 = Node('Right')
        n1.set_left(n2)
        n2.set_right(n3)
        a = BinaryTree(n1)
        s = a.size()
        expected = 3
        self.assertEqual(s, expected, "La taille de l'arbre devrait être {expected} mais elle vaut {s}.")

    def test_size5(self):
        # test avec l'arbre importé
        tree = tree1
        a = BinaryTree()
        a.import_tree(tree)
        s = a.size()
        expected = 8
        self.assertEqual(s, expected, "La taille de l'arbre devrait être {expected} mais elle vaut {s}.")

    def test_size6(self):
        # test avec l'arbre importé
        tree = tree2
        a = BinaryTree()
        a.import_tree(tree)
        s = a.size()
        expected = 11
        self.assertEqual(s, expected, "La taille de l'arbre devrait être {expected} mais elle vaut {s}.")

        
if __name__ == '__main__':
    unittest.main()        
