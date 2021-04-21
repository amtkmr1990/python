from node import Node
from binarytree import BinaryTree

tree = BinaryTree(Node(9))
tree.add(Node(5))
tree.add(Node(13))
tree.add(Node(11))
tree.add(Node(6))
tree.add(Node(3))
tree.add(Node(15))

print(tree.find(2))
tree.inorder()