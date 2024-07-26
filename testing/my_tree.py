# my_tree.py
from treelib import Node, Tree

# Documentation: https://readthedocs.org/projects/treelib/downloads/pdf/stable/

# IMPORTANT NOTE: The way the count variable is designed to store information is that each node can get incremented when a new node is found
# THIS DOES NOT CHANGE THE LEAF NODES!!!
# So when you want to get the count through the leaf nodes it will be different

# Extend the Node class to include a 'count' attribute, this is used for feature counting
class MyNode(Node):
    def __init__(self, tag=None, identifier=None, expanded=True, data=None, count=1):
        super(MyNode, self).__init__(tag=tag, identifier=identifier, expanded=expanded, data=data)
        self.count = count

    def change_count(self, amount):
        self.count+=amount

    def set_count(self, amount):
        self.count = amount

# Override the Tree class to use MyNode
class MyTree(Tree):
    def __init__(self, tree=None, deep=False, node_class=MyNode, identifier=None):
        super(MyTree, self).__init__(tree=tree, deep=deep, node_class=node_class, identifier=identifier)

    # Override the create_node function to allow 'count' as a parameter
    def create_node(self, tag=None, identifier=None, parent=None, data=None, count=1):
        node = super().create_node(tag=tag, identifier=identifier, parent=parent, data=data)
        node.set_count(count)
        return node


