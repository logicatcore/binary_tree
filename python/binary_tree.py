from typing import TypeVar, Generic

Node = TypeVar('Node')

class Node(Generic[Node]):

    def __init__(self, v: float, l: Node = None, r: Node = None) -> None:
        """
        Initialises a node with a value and assigns it left and/or right childs

        :param v: Value of the Node in the tree
        :param l: left child node if present
        :param r: right child node if present
        """
        self.value = v
        self._left = l
        self._right = r

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, l):
        if hasattr(l, 'value') or l is None:
            self._left = l
        else:
            raise TypeError('Left child accepts only a "Node" type object')

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, r):
        if hasattr(r, 'value') or r is None:
            self._right = r
        else:
            raise TypeError('Right child accepts only a "Node" type object')

    def __repr__(self):
        """
        Prints the node value and it's childs values in ASCII style

        ##a##
        #/ \#
        b###c

        :return: ASCII representation of the node and it's childs
        """
        if self.left and self.right:
            return f'  {self.value}  \n' \
                   f' / \\ \n' \
                   f'{self.left.value}   {self.right.value}'
        elif self.right is None and self.left is not None:
            return f'  {self.value}  \n' \
                   f' /   \n' \
                   f'{self.left.value}    '
        else:
            return f'  {self.value}  '

class BT:

    def __init__(self, norl) -> None:
        """
        The init initialiser accepts either a single root node or a list to create a binary tree from the list
        :param norl: An object of type Node or type python list
        """
        if isinstance(norl, Node):
            self.root = norl
        elif isinstance(norl, list):
            def recur(i):
                if 2*i+2 < len(norl):
                    return Node(norl[i], recur(2*i+1), recur(2*i+2))
                elif 2*i+1 < len(norl):
                    return Node(norl[i], recur(2*i+1))
                else:
                    return Node(norl[i])
            self.root = recur(0)