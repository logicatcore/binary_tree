import pytest
from lib.binary_tree import BT, Node

class TestBinaryTreeAttributes:

    def test_depth(self):
        """
        For a 10 elemets tree the tree would be as follows
                       1
                      / \
                     2   3
                    /\   /\
                   4  5 6  7
                  /\  |
                 8 9  10
        which has maximum depth/height of 3 for elements 8,9, and 10
        :return: None
        """
        import math
        bt = BT([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        assert math.floor(math.log2(10)) == bt.depth, "The calculated depth differs from the theoretical depth"

    def test_nodes_and_leafs_count(self):
        """
        For a 10 elemets tree the tree would be as follows
                       1
                      / \
                     2   3
                    /\   /\
                   4  5 6  7
                  /\  |
                 8 9  10
        which has 5 nodes and 5 leafs exactly
        :return: None
        """
        bt = BT([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        assert 5 == bt.nodes, "Number of nodes differs from the expected value"
        assert 5 == bt.leafs, "Number of leafs differs from the expected value"