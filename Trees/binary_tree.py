"""

binary_tree.py
This program is for creating of binary search tree and implementation of its basic and auxiliary operations
Basic Operations:
1) Insert an element into a tree
2) Searching for an element
3) Deletion of an element
4) Find Maximum element in the tree
5) Find Minimum element in the tree
6) Level ordered printing of tree
7) Depth First Inordered printing of tree
8) Check if tree is Binary Search Tree or not
9) Find Successor of an element in binary search tree

@author Rahul Kr Sinha
@version 2017-05-01
"""


class BstNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return self.data

    def __repr__(self):
        return self.data


def insert(root, data):
    if not root:
        root = BstNode(data)
    elif data <= root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


def search(root, data):
    if not root:
        return "Not Found : " + str(data)
    elif root.data == data:
        return "Found : " + str(data)
    elif data <= root.data:
        return search(root.left, data)
    else:
        return search(root.right, data)


def maximum(root):
    if not root:
        return None
    elif root.right is None:
        return root.data
    elif root.right is not None:
        return maximum(root.right)


def minimum(root):
    if not root:
        return None
    elif root.left is None:
        return root.data
    elif root.left is not None:
        return minimum(root.left)


def dept_first_print(root):
    """
    Recursive function to print tree in in-ordered format
    :param root: root BstNode of the tree
    :return:
    """
    if root.left:
        dept_first_print(root.left)

    if root:
        print(root.data, end=" ")

    if root.right:
        dept_first_print(root.right)


def level_order_print(root):
    """
    Function to print tree in level ordered format
    :param root: root BstNode of the tree
    :return:
    """
    if root:
        que = [root]
        while que:
            node = que.pop(0)
            print(node.data, end=" ")
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)


def height(root):
    """
    Function to find height of the tree
    :param root: root BstNode of the tree
    :return: height as integer and -1 for empty tree and 0 for single node tree
    """
    if root:
        return max(height(root.left), height(root.right)) + 1
    else:
        return -1


def sub_tree_smaller(root, data):
    """
        This is a sub function used in check_for_bst for finding that every node in the root tree is smaller than data
        :param root: root BstNode of the tree
        :param data: root's tree parent data value, for which root is left sub tree
        :return: Boolean True/False
        """
    if not root:
        return True
    if root.data <= data and sub_tree_smaller(root.left, data) and sub_tree_smaller(root.right, data):
        return True
    else:
        return False


def sub_tree_greater(root, data):
    """
    This is a sub function used in check_for_bst for finding that every node in the root tree is greater than data
    :param root: root BstNode of the tree
    :param data: root's tree parent data value, for which root is right sub tree
    :return: Boolean True/False
    """
    if not root:
        return True
    if root.data > data and sub_tree_greater(root.left, data) and sub_tree_greater(root.right, data):
        return True
    else:
        return False


def check_for_bst(root):
    """
    This function check if the given tree is BST or not,
    Its an expensive function because every node is checked multiple times.
    Another method is traversal of tree Inordered and see if elements are in ascending order, because in binary tree
    elements are in ascending ordered and it will cost O(n) time.
    :param root: root BstNode of the tree
    :return: boolean True or False
    """
    if not root:
        return True
    if sub_tree_smaller(root.left, root.data) and \
            sub_tree_greater(root.right, root.data) and \
            check_for_bst(root.left) and check_for_bst(root.right):
        return True
    else:
        return False


def delete(root, data):
    if not root:
        return root
    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    if root.data == data:
        # case 1 : data is a leaf node
        if root.left is None and root.right is None:
            root = None
        # case 2 : data has single node
        elif root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        # case 3: data has both the nodes
        else:
            min_data = minimum(root.right)
            root.data = min_data
            delete(root.right, min_data)
        return root


def find(root, data):
    if root is None:
        return root
    if data < root.data:
        return find(root.left, data)
    elif data > root.data:
        return find(root.right, data)
    elif data == root.data:
        return root


def find_successor(root, data):
    current = find(root, data)
    if current is None:
        return current
    if current.right is not None:
        return minimum(current.right)
    else:
        successor = None
        ancestor = root
        while ancestor != current:
            if current.data < ancestor.data:
                successor = ancestor
                ancestor = ancestor.left
            elif current.data > ancestor.data:
                ancestor = ancestor.right
        return successor


def main():
    root = None

    insertion_list = ["F", "D", "J", "B", "E", "G", "K", "A", "C", "I", "H"]
    for i in insertion_list:
        root = insert(root, i)

    print(search(root, "A"))
    print(search(root, "Z"))

    print("Maximum is : " + str(maximum(root)))
    print("Minimum is : " + str(minimum(root)))

    print("Depth first")
    dept_first_print(root)

    print("\nLevel ordered tree")
    level_order_print(root)

    print("\nHeight of tree is : " + str(height(root)))
    print("Is Tree a Binary Search Tree : ", check_for_bst(root))

    root = delete(root, "F")

    print("Level ordered tree after deletion")
    level_order_print(root)
    print("\nDepth first tree after deletion")
    dept_first_print(root)
    print("\nsuccessor of G is ", find_successor(root, "G"))


if __name__ == "__main__":
    main()