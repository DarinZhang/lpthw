# -*- coding: utf-8 -*-
# 树排序算法

# Refer to this project
# https://github.com/TheAlgorithms/Python/blob/master/sorts/tree_sort.py

# Tree_sort algorithm
# Build a BST and in order traverse.

# 定义类node
class node():
    # BST data structure
	# 定义类中的函数__init__，参数为self, val
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 
    
	# 定义类中的函数insert，参数为self, val
    def insert(self,val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

# 定义函数inorder,参数为root, res
def inorder(root, res):
    # Recursive travesal 
    if root:
        inorder(root.left,res)
        res.append(root.val)
        inorder(root.right,res)

# 定义函数treesort, 参数为arr
def treesort(arr):
    # Build BST
    if len(arr) == 0:
        return arr
    root = node(arr[0])
    for i in range(1,len(arr)):
        root.insert(arr[i])
    # Traverse BST in order. 
    res = []
    inorder(root,res)
    return res

print(treesort([10,1,3,2,9,14,13]))