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
        self.left = l
        self.right = r

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

        ##a##    ##a##    ##a##
        #/ \# or #/    or
        b###c    b

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
        self.root = norl
        self.depth = self.__depth__(self.root)
        self.nodes, self.leafs = self.__countnl__(self.root, self.depth)

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, norl):
        if isinstance(norl, Node):
            self._root = norl
        elif isinstance(norl, list):
            def recur(i):
                if 2*i+2 < len(norl):
                    return Node(norl[i], recur(2*i+1), recur(2*i+2))
                elif 2*i+1 < len(norl):
                    return Node(norl[i], recur(2*i+1))
                else:
                    return Node(norl[i])
            self._root = recur(0)

    @staticmethod
    def __depth__(root):
        """
        Calculates the maximum depth/height of the tree
        :param root: root node of the tree
        :return: maximum depth/height of the tree
        """
        def recur(n):
            if n.left is None:
                return 1
            if n.right is None:
                return 1
            return max(1 + recur(n.left), 1 + recur(n.right))

        return max(1 + recur(root.left), 1 + recur(root.right)) - 1

    @staticmethod
    def __countnl__(root, depth):
        """
        Counts the number of nodes and leafs in the tree
        :param root: root node of the tree
        :return: count of nodes and count of leafs
        """
        elements = [root]
        n,l = 0, 0
        while depth > 0:
            for e in elements:
                if e.left or e.right:
                    n += 1
                else:
                    l += 1
            elements = [e.left for e in elements if e.left is not None] + [e.right for e in elements if e.right is not None]
            depth -= 1
        # the elements in last level are indefinitely leafs, so no checking needed
        l += len(elements)
        return n, l

    def graphviz(self):
        try:
            import graphviz as G

            dot = G.Digraph(comment='Binary Tree',
                            graph_attr={'nodesep': '0.04', 'ranksep': '0.05', 'bgcolor': 'white', 'splines': 'line',
                                        'rankdir': 'TB', 'fontname': 'Hilda 10', 'color':'transparent'},
                            node_attr={'fixedsize': 'true', 'shape': 'circle', 'penwidth': '1', 'width': '0.4',
                                       'height': '0.4', 'fontcolor':'black'},
                            edge_attr={'color': 'black', 'arrowsize': '.4'})
            mapping = []
            depth = self.depth
            while depth >= 0:
                with dot.subgraph(name='cluster_' + str(depth)) as c:
                    #c.attr(color='transparent', rankdir='LR')
                    if depth == self.depth:
                        c.node(str(depth) + str(0), str(self.root.value))

                        if self.root.left and self.root.right:
                            mapping += [{str(depth)+str(0): [self.root.left, self.root.right]}]
                        elif self.root.right is None:
                            mapping += [{str(depth)+str(0): [self.root.left]}]
                        elif self.root.right is None:
                            mapping += [{str(depth)+str(0): [self.root.right]}]
                    else:
                        tmp = []
                        i = 0
                        # list of dicts
                        for subtree in mapping:
                            # dict with list as value
                            for key, value in subtree.items():
                                # value list contains the childs of a node, here key
                                for e in reversed(value):
                                    c.node(str(depth)+str(i), str(e.value))
                                    dot.edge(key, str(depth)+str(i))

                                    if e.left or e.right:
                                        if e.left and e.right:
                                            tmp += [{str(depth)+str(i): [e.left, e.right]}]
                                        elif e.right is None:
                                            tmp += [{str(depth) + str(i): [e.left]}]
                                        elif e.left is None:
                                            tmp += [{str(depth) + str(i): [e.right]}]
                                    i += 1
                        mapping = tmp
                depth -= 1
            return dot
        except ImportError as e:
            print('ModuleNotFoundError: "graphviz" package not available')