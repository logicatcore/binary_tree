#pragma once

#include "node.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>

template<typename T>
class BinaryTree {
    private:
        Node<T> *_root;

        Node<T>* spawnTree(int idx) {
            if(2 * idx + 2 < _values.size()) {
                return new Node<T>(_values[idx], BinaryTree<T>::spawnTree(2 * idx + 1), BinaryTree<T>::spawnTree(2 * idx + 2));
            }
            else if(2 * idx + 1 < _values.size()) {
                return new Node<T>(_values[idx], BinaryTree<T>::spawnTree(2 * idx + 1));
            }
            else {
                return new Node<T>(_values[idx]);
            }
        }
        
    public:
        unsigned int _nodesCount{0}, _leafsCount{0}, _depth{0};
        std::vector<T> _values;

        BinaryTree(T value): _root(new Node<T>(value)) {}
        BinaryTree(Node<T> *root): _root(root) {}
        BinaryTree(Node<T> &root): _root(&root) {}

        BinaryTree(std::vector<T> values) {
            _values = values;
            _root = spawnTree(0);
        }

        ~BinaryTree(){
            delete _root;
        }

        Node<T>* getRoot(){
            return _root;
        }

        std::vector<T> toVector(){
            if (_values.empty()) {
                std::vector<Node<T>*> nodes{_root};
                std::vector<T> values{_root->_value};
                int n = 0, l = 0;
                while(nodes.size() > 0) {
                    std::vector<Node<T>*> tmp;
                    for(Node<T> *&n: nodes) {
                        if(n->_left && n->_right) {
                            tmp.push_back(n->_left);
                            tmp.push_back(n->_right);
                        }
                        else if(n->_left == nullptr && n->_right) {
                            tmp.push_back(n->_right);
                        }
                        else if(n->_right == nullptr && n->_left) {
                            tmp.push_back(n->_left);
                        }
                    }
                    nodes = tmp;
                    for(Node<T> *&n: nodes) {
                        values.push_back(n->_value);
                    }
                }
                return values;
            }
            else {
               return _values; 
            }
        }

        static unsigned int depthRecurssion(Node<T>* n){
            if (n == nullptr){
                return 1;
            }
            return std::max(1 + depthRecurssion(n->_left), 1 + depthRecurssion(n->_right));
        }

        unsigned int findMaxDepth(){
            if (_depth == 0) {
                _depth = std::max(1 + depthRecurssion(_root->_left), 1 + depthRecurssion(_root->_right)) - 2;
                return _depth;
            }
            else {
                return _depth;
            }
        }

        std::tuple<unsigned int, unsigned int> getNodesLeafsCount() {
            std::vector<Node<T>*> nodes{_root};
            unsigned int N = 0, L = 0;

            if (_depth == 0){
                findMaxDepth();
            }
            
            if (_nodesCount == 0 && _leafsCount == 0 ) {
                int depth = _depth;
                while(depth > 0) {
                    for(Node<T> *&n: nodes) {
                        if(n->_left != nullptr | n->_right != nullptr) {
                            N += 1;
                        }
                        else {
                            L += 1;
                        }
                    }
                    std::vector<Node<T>*> tmp;
                    for (Node<T> *&n: nodes) {
                        if (n->_left != nullptr) {
                            tmp.push_back(n->_left);
                        }
                    }
                    for (Node<T> *&n: nodes) {
                        if (n->_right != nullptr) {
                            tmp.push_back(n->_right);
                        }
                    }
                    nodes = tmp;
                    depth -= 1;
                }
                L += nodes.size();
                _nodesCount = N;
                _leafsCount = L;
                return std::tuple<unsigned int, unsigned int>(N, L);
            }
            else {
                return std::tuple<unsigned int, unsigned int>(_nodesCount, _leafsCount);
            }
        }
};