#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
"""
                  50
                 /  \
                /    \
               /      \
              /        \
             /          \
            /            \
           /              \
          10               70
         /  \             /  \
        /    \           /    \
       4     15         60    80
            / \         / \
           /   \       /   \
          12   17     55    65

import pdb;pdb.set_trace()
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def bst_find(root:Node, val:int)->Node:
    if not root:return None
    curr = root
    while curr:
        if curr.val == val:
            return curr
        elif curr.val > val:
            curr = curr.left
        else:
            curr = curr.right
    return curr


 
def menu(root):
    menu_str="""~~ Menu ~~
    1. Disp
    2. Max
    3. Min
    4. Successor"""
    ch = 1
    while ch != 0:
        print(menu_str)
        #ch = int(input("enter choice:"))
        print("Enter choice:", end="")
        sys.stdout.flush()
        res = sys.stdin.readline()
        #import pdb;pdb.set_trace()
        ch = int(res.strip())

        if ch == 1:
            disp_lvl(root)
        elif ch == 2:
            x = int(input("enter root node val of subtree:"))
            subtree = bst_find(root, x)
            if not subtree: subtree = root
            y = bst_max(subtree)
            if y:print(f"max({x})={y.val}")
            else: print("node with val {x.val} doesnt exist")
        elif ch == 3:
            x = int(input("enter root node val of subtree:"))
            subtree = bst_find(root, x)
            if not subtree: subtree = root
            y = bst_min(subtree)
            if y:print(f"min({x})={y.val}")
            else: print("node with val {x.val} doesnt exist")
        elif ch == 4:
            val = int(input("enter val of node whose successor is needed:"))
            p = bst_find(root, val)
            if not p:
                print("({val}) does not exist in tree")
            else:
                #y = successor(root, p) # bad
                #y = succ(root, p) # good recursive
                y = inorderSuccessor(root, p)
                if y: print(f"successor({val})={y.val}")
                else: print(f"successor({val})=None")
# https://stackoverflow.com/questions/45127902/why-isnt-this-ascii-art-printing-on-multiple-lines-despite-being-a-multiline-st
bst=r'''
                  50
                 /  \
                /    \
               /      \
              /        \
             /          \
            /            \
           /              \
          10               70
         /  \             /  \
        /    \           /    \
       4     15         60    80
            / \         / \
           /   \       /   \
          12   17     55    65
'''
# inorder succesor: LNR
# max of rt subtree else min rt ancestor
# succ(17):50 X
"""
case1: When the node has a right child: ret min(node.right)
case2: When the node doesn't have a right child:
case3:
"""
# https://leetcode.com/problems/inorder-successor-in-bst/discuss/72723/Python-Short-Recursive-solution-4-lines
# iterative
def succ(root:Node, p:Node)->Node:
    if not root: return None
    print(f"root:{root.val} p:{p.val}")
    #import pdb;pdb.set_trace()
    if root.val > p.val:
        print("find <")
        res = succ(root.left, p)
        if res:
            return res
        else:# returns nearest largest ancestor
            print(f"returning root:{root.val}")
            return root
    else:
        print("find >")
        res =  succ(root.right, p)
        print(f"returning rtroot:{root.val}")
        return res

# recursive
def inorderSuccessor(root, p):
    successor = None
    while root:
        if p.val < root.val:
            successor = root
            root = root.left
        else:
            root = root.right
    return successor

# get max of of given subtree, which is right-most elm
def bst_max(x)->Node:
    while x and x.right: x = x.right
    return x

# get min of of given subtree, which is left-most elm
def bst_min(x)->Node:
    while x and x.left: x = x.left
    return x

def insert(root, val)->Node:
    prev, curr = None, root
    if not curr:
        curr = Node(val)
        return curr
    while curr:
        if curr.val < val:
            prev = curr
            curr = curr.right
        elif curr.val > val:
            prev = curr
            curr = curr.left
    # insert new node
    curr = Node(val)
    if curr.val < prev.val:
        prev.left = curr
    else:# curr.val > prev.val
        prev.right = curr
    return root
   return root

def disp_lvl(root):
    if not root:
        return
    q = [root]
    while q:
        cnt = len(q)
        while cnt:
            node = q.pop(0)
            if node.left:q.append(node.left)
            if node.right:q.append(node.right)
            if node:
                print(f"{node.val:>2}", end=",")
            else:
                print(f"-", end=",")

            cnt -= 1
        print("")

def inorder(root):#LNR
    if not root:return
    inorder(root.left)
    print(f"{root.val}", end=",")
    inorder(root.right)

#main
n = Node(50)
n = insert(n, 10)
n = insert(n, 70)
n = insert(n, 15)
n = insert(n, 17)
n = insert(n, 12)
n = insert(n, 60)
n = insert(n, 55)
n = insert(n, 65)
n = insert(n, 80)
n = insert(n, 4)
disp_lvl(n)
print("inorder:", end="")
inorder(n)
print(bst)
menu(n)

