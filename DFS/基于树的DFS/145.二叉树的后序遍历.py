# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def func(tree, res):
            if not tree:
                return
            func(tree.left, res)
            func(tree.right, res)
            res.append(tree.val)
        res = []
        func(root, res)
        return res