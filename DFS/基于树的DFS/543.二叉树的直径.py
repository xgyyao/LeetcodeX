# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(root):
            if not root:
                return 0, 0
            ldiameter, ldepth = traverse(root.left)
            rdiameter, rdepth = traverse(root.right)
            return max(ldiameter, rdiameter, ldepth+rdepth), max(ldepth, rdepth)+1
        return traverse(root)[0]