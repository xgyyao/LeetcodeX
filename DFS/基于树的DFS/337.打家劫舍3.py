# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def func(tree):
            if not tree:
                return 0, 0
            left = func(tree.left)
            right = func(tree.right)
            v1 = tree.val + left[1] + right[1]
            v2 = max(left) + max(right)
            return v1, v2
        return max(func(root))