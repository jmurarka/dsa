# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        from collections import deque

        if root is None:
            return 0

        q = deque([root])
        depth = 0

        while q:
            levelSize = len(q)

            for i in range(levelSize):
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            depth += 1

        return depth