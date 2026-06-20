from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Binary Tree Inorder Traversal - #94

        Visit left subtree, then current node, then right subtree.
        This gives nodes in sorted order for a binary search tree.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        nums = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)

        dfs(root)
        return nums


# test cases
solution = Solution()
root1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(solution.inorderTraversal(root1))  # [1, 3, 2]

root2 = TreeNode(1, TreeNode(2), TreeNode(3))
print(solution.inorderTraversal(root2))  # [2, 1, 3]

print(solution.inorderTraversal(None))  # []
