class Node:
    """The class represents a single node in a binary tree"""

    def __init__(self, value, left_child: "Node" = None, right_child: "Node" = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def greatest_node(root):
    if root is None:
        return None  # Return None for an empty tree

    max_value = root.value  # Assume the root value is the maximum initially

    left_max = greatest_node(root.left_child)
    right_max = greatest_node(root.right_child)

    if left_max is not None:
        max_value = max(max_value, left_max)
    if right_max is not None:
        max_value = max(max_value, right_max)

    return max_value


if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))
