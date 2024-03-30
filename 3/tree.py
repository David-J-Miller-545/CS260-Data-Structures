#!/usr/bin/env python3
# tree - the tree class is structure for a recursive binary tree
# 
# 1/30

class Tree:
    def __init__(self, data, leftChild = None, rightChild = None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild
    
    def __str__( self ):
        return str( self.data )


def post_order(tree):
    if (tree.leftChild == None and tree.rightChild == None):
        return str(tree)
    else:
        return post_order(tree.leftChild) + ' ' + post_order(tree.rightChild) + ' ' + str(tree)

def pre_order(tree):
    if (tree.leftChild == None and tree.rightChild == None):
        return str(tree)
    else:
        return str(tree) + ' ' + pre_order(tree.leftChild) + ' ' + pre_order(tree.rightChild)

def in_order(tree):
    if (tree.leftChild == None and tree.rightChild == None):
        return str(tree)
    else:
        return  in_order(tree.leftChild) + ' ' + str(tree) + ' ' + in_order(tree.rightChild)

if __name__ == "__main__":
    A = Tree('*', Tree('-', Tree('5'), Tree('12')), Tree('3'))
    print("post: " + post_order(A))
    print("pre: " + pre_order(A))
    print("in: " + in_order(A))