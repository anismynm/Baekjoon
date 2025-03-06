## implemention of binaryTree
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def pre_order(self, n):
        if n is not None:
            print(n.item, end = '')
            if n.left:
                self.pre_order(n.left)
            if n.right:
                self.pre_order(n.right)

    def in_order(self, n):
        if n is not None:
            if n.left:
                self.in_order(n.left)
            print(n.item, end = '')
            if n.right:
                self.in_order(n.right)

    def post_order(self, n):
        if n is not None:
            if n.left:
                self.post_order(n.left)
            if n.right:
                self.post_order(n.right)
            print(n.item, end = '')
        
n = int(input())
node_arr = [Node(chr(i)) for i in range(65, 66 + n)]
tree = BinaryTree(node_arr[0])

for _ in range(n):
    item, left, right = input().rstrip().split()
    if left != '.':
        node_arr[ord(item) - 65].left = node_arr[ord(left) - 65]
    if right != '.':
        node_arr[ord(item) - 65].right = node_arr[ord(right) - 65]

tree.pre_order(node_arr[0])
print()
tree.in_order(node_arr[0])
print()
tree.post_order(node_arr[0])
print()