#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from sl29.structures import Node

class NodeTests(unittest.TestCase):
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

    def test_is_leaf1(self):
        # test d'un noeud unique
        a = Node('A')
        self.assertTrue(a.is_leaf(), f"Le noeud {a.value()} devrait être une feuille.")
        
    def test_is_leaf2(self):
        # test avec un noeud ayant un noeud à gauche
        a = Node('A')
        b = Node ('B')
        a.set_left(b)
        self.assertFalse(a.is_leaf(), f"Le noeud {a.value()} ne devrait pas être une feuille, car il possède le noeud {a.left().value()} à gauche.")
        
    def test_is_leaf3(self):
        # test avec un noeud ayant un noeud à droite
        a = Node('A')
        b = Node ('B')
        a.set_right(b)
        self.assertFalse(a.is_leaf(), f"Le noeud {a.value()} ne devrait pas être une feuille, car il possède le noeud {a.right().value()} à gauche.")

    def test_is_leaf4(self):
        # test avec un noeud ayant un noeud à droite
        a = Node('A')
        b = Node ('B')
        c = Node ('C')
        a.set_left(b)
        a.set_right(c)
        self.assertFalse(a.is_leaf(), f"Le noeud {a.value()} ne devrait pas être une feuille, car il possède le noeud {a.left().value()} à gauche et le noeud {a.right().value()} à droite.")

        
if __name__ == '__main__':
    unittest.main()        
