'''
Balanced Binary Search Tree

Given a sorted list of numbers `a`, write a function `balanced_bst(a)` to
create a balanced binary search tree. A balanced Binary Search Tree has no more
than one level of depth difference between the right and left sides of the
tree.

Each value in the list `a` should correspond to a node value.
The return value of `balanced_bst()` will be the root note of teh balanced
tree. An empty array passed to `balanced_bst` should return None.

For example, given a list `a = [1, 2, 3, 4, 5, 6, 7, 8]`, you want to create a
balanced tree that may resemble the following:
               5
             /   \
            3     7
           / \   / \
          2   4 6   8
         /
        1
The above figure represents a balanced tree because there is at most 1 level of
difference between the depths of each side of the tree.

For this challenge you are given the class `TreeNode` with the members:
  * `value`: the node value
  * `left`: the left child node; defaults to `None`
  * `right`: The right child node; defaults to `None`
The __str__() function is also implemented in the class `TreeNode`, so at any
time you can print the root node to see a basic representation of the tree.

Original code challenge located here:
https://www.codecademy.com/code-challenges/code-challenge-balanced-binary-search-tree-python
'''


class TreeNode():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return f'{self.value}-->{self.left}\n{self.value}-->{self.right}'


def balanced_bst(a):
    if len(a) == 0:
        return None
    mid = len(a) // 2
    tree = TreeNode(a[mid])
    bottom = a[:mid]
    top = a[mid + 1:]
    if len(bottom) > 0:
        tree.left = balanced_bst(bottom)
    if len(top) > 0:
        tree.right = balanced_bst(top[0:])
    return tree


if __name__ == '__main__':

    a = [1, 2, 3, 4, 5, 6, 7, 8]
    balanced_node = balanced_bst(a)
    print(balanced_node)
