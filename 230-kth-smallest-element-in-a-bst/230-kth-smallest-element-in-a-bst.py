# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        li=[]
        def helper(root):
            if root:
                helper(root.left)
                if len(li)!=k:
                    li.append(root.val)
                else:
                    return
                helper(root.right)
        helper(root)
        return li[-1]
        
            