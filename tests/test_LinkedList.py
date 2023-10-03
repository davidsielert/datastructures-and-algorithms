import unittest
from datastructures.LinkedList import LinkedList
from tests.helpers import ListTest


class LinkedListTestCase(ListTest):

    def test_linkedlist(self):
        list = LinkedList()
        self.list_tester(list)
        self.assertEqual(True,True)



if __name__ == '__main__':
    unittest.main()
