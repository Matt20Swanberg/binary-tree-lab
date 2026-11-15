"""
Binary Trees - Depth and Ancestors Lab

This module implements two binary tree algorithms:

1. Maximum Depth of a Binary Tree
   - Calculates the longest path from the root to a leaf node
   - Uses recursion to determine the depth of each subtree

2. Lowest Common Ancestor of a Binary Search Tree
   - Finds the lowest shared ancestor of two nodes
   - Uses BST properties to navigate left or right recursively
"""

from typing import Optional

class TreeNode:
    """
    Represents a single node in a binary tree

    Attributes:
        val (int): The value stored in the node
        left (Optional[TreeNode]): Reference to the left child
        right (Optional[TreeNode]): Reference to the right child
    """

    def __init__(self, val: int):
        """Initialize a node with a value and no children"""
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


def max_depth(root: Optional[TreeNode]) -> int:
    """
    Calculate the maximum depth of a binary tree

    The maximum depth is the number of nodes along the longest
    path from the root node to the farthest leaf node

    Args:
        root (Optional[TreeNode]): Root node of the binary tree

    Returns:
        int: Maximum depth of the tree, or 0 if the tree is empty

    Time Complexity:
        O(n) - Each node is visited once

    Space Complexity:
        O(h) - Recursive call stack depends on tree height
        O(n) in the worst case for a skewed tree
    """

    # Base case: An empty tree has a depth of 0
    if root is None:
        return 0

    # Recursively calculate the depth of the left subtree
    left_depth = max_depth(root.left)

    # Recursively calculate the depth of the right subtree
    right_depth = max_depth(root.right)

    # Return the greater subtree depth plus the current node
    return max(left_depth, right_depth) + 1


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find the lowest common ancestor of two nodes in a BST.

    The lowest common ancestor is the deepest node that is
    an ancestor of both target nodes. A node can also be
    considered an ancestor of itself.

    This implementation assumes both target nodes exist
    in the BST and that node values are unique.

    Args:
        root (TreeNode): Current root of the BST or subtree
        p (TreeNode): First target node
        q (TreeNode): Second target node

    Returns:
        TreeNode: The lowest common ancestor of p and q

    Time Complexity:
        O(h) - Traverses one path through the BST
        O(log n) for a balanced BST
        O(n) in the worst case for a skewed BST

    Space Complexity:
        O(h) - Recursive call stack depends on tree height
    """

    # Both target values are smaller than the current node
    # Search the left subtree for their common ancestor
    if root.val > p.val and root.val > q.val:
        return lowest_common_ancestor(root.left, p, q)

    # Both target values are greater than the current node
    # Search the right subtree for their common ancestor
    elif root.val < p.val and root.val < q.val:
        return lowest_common_ancestor(root.right, p, q)

    # The targets split across subtrees, or the current
    # node matches one of the targets
    # Therefore, the current node is their lowest common ancestor
    return root

