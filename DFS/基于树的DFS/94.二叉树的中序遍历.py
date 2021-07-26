# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def func(tree, res):
            if not tree:
                return
            func(tree.left, res)
            res.append(tree.val)
            func(tree.right, res)

        res = []
        func(root, res)
        return res