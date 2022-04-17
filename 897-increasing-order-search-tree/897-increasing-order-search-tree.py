# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        global temp
        temp=TreeNode()
        head=temp
        def helper(root):
            if root:
                helper(root.left)
                global temp
                temp.right=TreeNode(root.val)
                print(root.val)
                temp=temp.right
                helper(root.right)
        helper(root)
        return head.right
            