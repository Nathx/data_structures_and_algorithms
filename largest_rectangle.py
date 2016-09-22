# https://www.hackerrank.com/challenges/largest-rectangle

# There are  buildings in a certain two-dimensional landscape. Each building has a height given by . If you join  adjacent buildings, they will form a solid rectangle of area .
#
# Given  buildings, find the greatest such solid area formed by consecutive buildings.
#
# Input Format
# The first line contains , the number of buildings altogether.
# The second line contains  space-separated integers, each representing the height of a building.
#
# Constraints
#
#
# Output Format
# One integer representing the maximum area of rectangle formed.
#
# Sample Input
#
# 5
# 1 2 3 4 5

# Sample Output
#
# 9


class Node(object):
    def __init__(self, value, idx):
        self.value = value
        self.idx = idx
        self.left = None
        self.right = None


class MST(object):
    """
    Minimum Search Tree
    For node with idx i:
    * Left child is the minimum value left of i
    * Right child is the minimum value right of i
    """
    def __init__(self, root):
        self.root = root
        self.size = 0

    def insert(self, n, idx):
        if not self.root:
            self.root = Node(n, idx)
        else:
            self._insert(n, idx, self.root)
        self.size += 1

    def _insert(self, n, idx, node):
        if idx < node.idx:
            if not node.left:
                node.left = Node(n, idx)
            else:
                self._insert(n, idx, node.left)
        if idx > node.idx:
            if not node.right:
                node.right = Node(n, idx)
            else:
                self._insert(n, idx, node.right)



def create_tree(arr):
    """Sort (value, index) tuples, then insert in tree."""
    sorted_arr = [(val, i) for i, val in enumerate(arr)]
    sorted_arr.sort()
    tree = MST()
    for val, i in sorted_arr:
        tree.insert(val, i)
    return tree


def area_traversal(tree):
    """Traverse tree and update max. area."""
    start, end = 0, tree.size
    result = 0
    stack = []
    stack.append((tree.root, start, end))
    while stack:
        node, start, end = stack.pop()
        if node.value*(end - start) > result:
            result = node.value*(end - start)
        if node.left:
            stack.append((node.left, start, node.idx))
        if node.right:
            stack.append((node.right, node.idx, end))
    return result

def find_largest_rectangle(arr):
    tree = create_tree(arr)
    return area_traversal(tree)



if __name__ == '__main__':
    n = int(raw_input())
    landscape = map(int, raw_input().split())
    print largest_rectangle(landscape)
