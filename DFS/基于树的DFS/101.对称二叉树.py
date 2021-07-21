# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def func(left, right):
            if left and not right:
                return False
            elif not left and right:
                return False
            elif not left and not right:
                return True
            else:
                return left.val == right.val and func(left.left, right.right) and func(left.right, right.left)

        if not root:
            return True
        return func(root.left, root.right)