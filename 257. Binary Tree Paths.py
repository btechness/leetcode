# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.
# Example 1:
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# Example 2:
# Input: root = [1]
# Output: ["1"]

# Constraints:
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def _dfs(self, root: TreeNode, cur, res) -> None:
        
        # Base Case
        if not root:
            return
        
        # Append node to path
        cur.append(str(root.val))
        
        # If root is a leaf, append path to result
        if not root.left and not root.right:
            res.append('->'.join(cur))
            
        # Recursive Step
        self._dfs(root.left, cur, res)
        self._dfs(root.right, cur, res)
        
        # Backtracking / Post-processing / pop node from path
        cur.pop()
        
        
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        res = []
        self._dfs(root, [], res)
        return res
        