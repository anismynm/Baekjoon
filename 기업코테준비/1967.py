import sys
input = sys.stdin.readline

class Node:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None
        self.left_cost = 0
        self.right_cost = 0

class Tree:
    def __init__(self, root):
        self.node = Node(root)
    
    def insert(self, num, cost):
        temp = Node(num)
        while node:
            

    def find(self):
        result = 0
        if node.left:
            result += node.left_cost + node.left.find()
        if node.right:
            result += node.right_cost + node.right.find()
        return result


n = int(input())
tree = Tree(1)
for _ in range(n - 1):
    parent, child, cost = map(int, input().split())
    tree.insert