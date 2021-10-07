# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def BFS(currentNode):

            if not currentNode:
                return False

            left = BFS(currentNode.left)

            mid = currentNode.val == p.val or currentNode.val == q.val

            right = BFS(currentNode.right)

            if mid + left + right >= 2:
                self.ans = currentNode

            return mid or left or right

        BFS(root)

        return self.ans


