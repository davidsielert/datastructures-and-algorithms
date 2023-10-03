import unittest

from datastructures.DoubleLinkedList import DoubleLinkedList
from tests.helpers import ListTest


class LinkedListTestCase(ListTest):

    def test_doublelinkedlist(self):
        list = DoubleLinkedList()
        self.list_tester(list)
        self.assertEqual(True,True)



if __name__ == '__main__':
    unittest.main()
