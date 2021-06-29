#pragma once

#include <iostream>
#include <string>
#include <algorithm>

template<typename T>
class BinaryTree;

template<typename T>
class Node {
    private:
        T _value;
        Node *_left;
        Node *_right;
        friend BinaryTree<T>;

    public:
        Node(T value, int left_value, int right_value): 
            _value(value), _left(new Node(left_value)), _right(new Node(right_value)) {}
        
        Node(T value, Node &left, Node &right): 
            _value(value), _left(&left), _right(&right) {}

        Node(T value, Node *left = nullptr, Node *right = nullptr): 
            _value(value), _left(left), _right(right) {}
        
        void setValue(T value){
            _value = value;
        }

        T getValue(T value){
            return _value;
        }

        void setLeftNode(Node<T> *left){
            _left = left;
        }

        void setLeftNode(T value){
            if (_left != nullptr)
                _left->_value = value;
            else
                _left = new Node<T>(value);
        }

        void setRightNode(Node<T> *right){
            _right = right;
        }

        void setRightNode(T value){
            if (_right != nullptr)
                _right->_value = value;
            else
                _right = new Node<T>(value);
        }

        Node* getRightNode(){
            return _right;
        }

        Node* getLeftNode(){
            return _left;
        }

        friend std::ostream& operator<<(std::ostream& stream, Node<T> &node) {
            int c = std::to_string(node._value).length();

            stream << std::string(c, ' ') << node._value << std::string(c, ' ') << "\n";
            stream << std::string(std::max((int)(1.5*c)-1, c), ' ') << "/\\  \n";

            if (node._left != nullptr && node._right != nullptr) {
                int l = std::to_string(node._left->_value).length();
                stream << std::string((int)(1.5*c)-l-1, ' ') << node._left->_value << "  " << node._right->_value << std::endl;
            }
            else if (node._left == nullptr && node._right != nullptr) {
                stream << std::string((int)(1.5*c)-2, ' ') << "-  " << node._right->_value << std::endl;
            }
            else if (node._left != nullptr && node._right == nullptr) {
                int l = std::to_string(node._left->_value).length();
                stream << std::string(std::max((int)(1.5*c)-l-1, 0), ' ') << node._left->_value << "  -" << std::endl;
            }
            else {
                stream << std::string((int)(1.5*c)-2, ' ') << "-  -" << std::endl;
            }
            return stream;
        }
};
