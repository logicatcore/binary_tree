#include "include/node.h"
#include "include/binary_tree.h"
#include <iostream>
#include <vector>

int main() {
    Node<int> n1(10342);
    std::cout << n1;

    Node<int> n2(10342);
    Node<int> left(22);
    n2.setLeftNode(&left);
    std::cout << n2;

    Node<int> n3(10342);
    Node<int> right(324);
    n3.setRightNode(&right);
    std::cout << n3;

    Node<int> n4(10342, 22, 323);
    std::cout << n4;

    std::vector<int> values{1,2,3};
    BinaryTree<int> tree1(values);

    {   
        auto values = tree1.toVector();
        for(auto &v: values) {
            std::cout << v << " ";
        }
        std::cout << std::endl;
    }

    BinaryTree<int> tree2(1);

    (tree2.getRoot())->setLeftNode(2);
    (tree2.getRoot())->setRightNode(3);

    (tree2.getRoot())->getLeftNode()->setLeftNode(4);
    (tree2.getRoot())->getLeftNode()->setRightNode(5);

    (tree2.getRoot())->getRightNode()->setLeftNode(6);
    (tree2.getRoot())->getRightNode()->setRightNode(7);

    {   
        auto values = tree2.toVector();
        for(auto &v: values) {
            std::cout << v << " ";
        }
        std::cout << std::endl;
    }
    
    std::cout << tree2.findMaxDepth() << std::endl;
    auto nl = tree2.getNodesLeafsCount();
    std::cout << std::get<0>(nl) << " " << std::get<1>(nl) << std::endl;

}