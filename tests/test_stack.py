"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Stack, Node

s1 = Stack()
s1.push('data')
s1.push('data1')


class TestStack(unittest.TestCase):
    def test_push(self):
        self.assertEqual(s1.top.data, 'data1')
        self.assertEqual(s1.top.next_node.data, 'data')



