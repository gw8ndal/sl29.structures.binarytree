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
        self.assertEqual(s, expected, f"La taille de l'arbre vide devrait être {expected} mais elle vaut {s}.")

    def test_size2(self):
        # test avec un arbre qui ne contient qu'un seul noeud
        n = Node('N1')
        a = BinaryTree(n)
        s = a.size()
        expected = 1
        self.assertEqual(s, expected, f"La taille de l'arbre devrait être {expected} mais elle vaut {s}.")

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
        self.assertEqual(s, expected, f"La taille de l'arbre devrait être {expected} mais elle vaut {s}.")

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
        self.assertEqual(s, expected, f"La taille de l'arbre devrait être {expected} mais elle vaut {s}.")

    def test_size5(self):
        # test avec l'arbre importé
        tree = tree1
        a = BinaryTree()
        a.import_tree(tree)
        s = a.size()
        expected = 8
        self.assertEqual(s, expected, f"La taille de l'arbre devrait être {expected} mais elle vaut {s}.")

    def test_size6(self):
        # test avec l'arbre importé
        tree = tree2
        a = BinaryTree()
        a.import_tree(tree)
        s = a.size()
        expected = 11
        self.assertEqual(s, expected, f"La taille de l'arbre devrait être {expected} mais elle vaut {s}.")
        
    def test_height1(self):
        a = BinaryTree()
        h = a.height()
        expected = -1
        self.assertEqual(h, expected, f"La hauteur de l'arbre devrait être {expected} mais elle vaut {h}.")

    def test_height2(self):
        n = Node('N1')
        a = BinaryTree(n)
        h = a.height()
        expected = 0
        self.assertEqual(h, expected, f"La hauteur de l'arbre devrait être {expected} mais elle vaut {h}.")

    def test_height3(self):
        n, k = Node('N1'), Node('K1')
        
        n.set_left(k)
        a = BinaryTree(n)
        h = a.height()
        expected = 1
        self.assertEqual(h, expected, f"La hauteur de l'arbre devrait être {expected} mais elle vaut {h}.")
        
    def test_height4(self):
        n, k, v, d = Node('N1'), Node('K1'), Node('V1'), Node('D1')
        
        n.set_left(k)
        n.set_right(d)
        k.set_left(v)
        a = BinaryTree(n)
        h = a.height()
        expected = 2
        self.assertEqual(h, expected, f"La hauteur de l'arbre devrait être {expected} mais elle vaut {h}.")
        
    def test_prefix1(self):
        a = BinaryTree()
        p = a.preorder()
        expected = []
        self.assertEqual(p, expected, f"Le parcours préfixe de l'arbre devrait être {expected} mais elle vaut {p}.")
        
    def test_prefix2(self):
        n = Node("1")
        a = BinaryTree(n)
        p = a.preorder()
        expected = ["1"]
        self.assertEqual(p, expected, f"Le parcours préfixe de l'arbre devrait être {expected} mais elle vaut {p}.")

    def test_prefix3(self):
        n, k = Node("1"), Node("2")
        n.set_left(k)
        a = BinaryTree(n)
        p = a.preorder()
        expected = ["1", "2"]
        self.assertEqual(p, expected, f"Le parcours préfixe de l'arbre devrait être {expected} mais elle vaut {p}.")

    def test_prefix4(self):
        n, k, v, d = Node("1"), Node("2"), Node("3"), Node("4")
        n.set_left(k)
        n.set_right(d)
        k.set_left(v)
        a = BinaryTree(n)
        h = a.preorder()
        expected = ["1","2","3","4"]
        self.assertEqual(h, expected, f"La hauteur de l'arbre devrait être {expected} mais elle vaut {h}.")

    def test_suffix1(self):
        a = BinaryTree()
        p = a.postorder()
        expected = []
        self.assertEqual(p, expected, f"Le parcours préfixe de l'arbre devrait être {expected} mais elle vaut {p}.")
        
    def test_suffix2(self):
        n = Node("1")
        a = BinaryTree(n)
        p = a.postorder()
        expected = ["1"]
        self.assertEqual(p, expected, f"Le parcours préfixe de l'arbre devrait être {expected} mais elle vaut {p}.")

    def test_suffix3(self):
        n, k = Node("1"), Node("2")
        n.set_left(k)
        a = BinaryTree(n)
        p = a.postorder()
        expected = ["2","1"]
        self.assertEqual(p, expected, f"Le parcours préfixe de l'arbre devrait être {expected} mais elle vaut {p}.")

    def test_suffix4(self):
        n, k, v, d = Node("1"), Node("2"), Node("3"), Node("4")
        n.set_left(k)
        n.set_right(d)
        k.set_left(v)
        a = BinaryTree(n)
        h = a.postorder()
        expected = ["3","2","4","1"]
        self.assertEqual(h, expected, f"La hauteur de l'arbre devrait être {expected} mais elle vaut {h}.")

if __name__ == '__main__':
    unittest.main()        
