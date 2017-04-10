#!/usr/bin/env python

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, data):
        if(self.root == None):
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        if(data < node.data):
            if(node.left != None):
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if(node.right != None):
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        if(self.root != None):
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if (data == node.data):
            return node
        elif (data < node.data and node.left != None):
            self._find(data, node.left)
        elif (data > node.data and node.right != None):
            self._find(data, node.right)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if (self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if (node != None):
            self._printTree(node.left)
            print str(node.data) + ' '
            self._printTree(node.right)


def check_binary_search_tree_(root):
    return isBinarySearchTree(root, 1, 10000)

def isBinarySearchTree(root, min, max):
    if root.data < min or root.data > max:
        return False

    check = True
    if root.left == None and root.right == None:
        check = True
    elif root.left != None:
        if root.left.data < root.data:
            isBinarySearchTree(root.left, min, max)
        else:
            check = False
    elif root.right != None:
        if root.right.data > root.data:
            isBinarySearchTree(root.right, min, max)
        else:
            check = False
    else:
        check = True
    return check

def check_binary_search_tree_(root):
    check = True
    if root.data < 0 or root.data > 10000:
        check = False
    elif (root.left is None) or (root.right is None):
        check = True
    elif root.left and root.left < root.data:
        check = True
        check_binary_search_tree_(root.left)
    elif root.right and root.right > root.data:
        check = True
        check_binary_search_tree_(root.right)
    else:
        check = False
    return check

if __name__=='__main__':
    #     3
    # 0     4
    #   2      8
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    tree.printTree()
    print (tree.find(3)).data
    print tree.find(10)
    tree.deleteTree()
    tree.printTree()

