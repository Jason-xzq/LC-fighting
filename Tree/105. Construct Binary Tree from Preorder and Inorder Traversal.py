# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dict = {}
        index = 0
        for i in inorder:
            dict[i] = index
            index += 1

        def helper(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            if inorder_left > inorder_right:
                return None

            preorder_root = preorder_left
            inorder_root = dict[preorder[preorder_root]]

            root = TreeNode(preorder[preorder_root])
            size_left_subtree = inorder_root - inorder_left
            root.left = helper(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            root.right = helper(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)

            return root

        n = len(preorder)
        return helper(0, n - 1, 0, n - 1)