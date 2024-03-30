#!/usr/bin/env python3
# post - mainly translates a post-order expression into an expression tree, prints various transversals of the tree,
#        and finally prints the value of the the expression evaluated.
# 
# 1/30

import tree
from tree import Tree
from lexer import *
from stack import *

def postorder():
    get_expression()
    
    t = get_next_token()
    exprStack = Stack()
    while t:
        exprStack.push(Tree(t))
        if (t in '*/+-'):
            operator = exprStack.pop()
            operator.rightChild = exprStack.pop()
            operator.leftChild = exprStack.pop()
            exprStack.push(operator)
        t = get_next_token()
    
    exprTree = exprStack.pop()
    print("pre: " + tree.pre_order(exprTree))
    print("in: " + tree.in_order(exprTree))
    print("post: " + tree.post_order(exprTree))
    print("eval: " + str(calcPost(exprTree)))

def calcPost(exprTree):
    expr = (tree.post_order(exprTree)).split()
    exprStack = Stack()
    for i in expr:
        exprStack.push(i)
        if i == '*':
            exprStack.pop()
            exprStack.push(int(exprStack.pop()) * int(exprStack.pop()))
        elif i == '/':
            exprStack.pop()
            exprStack.push(int(exprStack.pop()) / int(exprStack.pop()))
        elif i == '+':
            exprStack.pop()
            exprStack.push(int(exprStack.pop()) + int(exprStack.pop()))
        elif i == '-':
            exprStack.pop()
            exprStack.push(int(exprStack.pop()) - int(exprStack.pop()))
    return exprStack.pop()


if __name__ == "__main__":
    postorder()