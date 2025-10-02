import sys
sys.setrecursionlimit(1000000)

class Node:
    def __init__(self, key):
        self.key = key
        self.left_node = None
        self.right_node = None

class Tree:
    def __init__(self):
        self.root = None

    def rootNone(self):
        if self.root is None:
            return True
        return False

    def insert(self, key : int):
        if self.rootNone():
            self.root = Node(key)
            return

        cur_node = self.root
        pre_node = None
        while cur_node is not None:
            pre_node = cur_node
            if key < cur_node.key:
                cur_node = cur_node.left_node
            else:
                cur_node = cur_node.right_node
        if key < pre_node.key:
            pre_node.left_node = Node(key)
        else:
            pre_node.right_node = Node(key)
    
    def postOrder(self, node = None):
        if node is None:
            node = self.root
        if node.left_node is not None:
            self.postOrder(node.left_node)
        if node.right_node is not None:
            self.postOrder(node.right_node)
        print(node.key)

tree = Tree()
while True:
    try:
        tree.insert(int(input()))
    except:
        break

if not tree.rootNone():
    tree.postOrder()