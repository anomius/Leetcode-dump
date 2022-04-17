# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        k=[]
        def helper1(root):
            if root:
                helper1(root.left)
                k.append(root.val)
                helper1(root.right)
        helper1(root)
        global gg
        gg=sum(k)
        
        def helper2(root):
            if root:
            
                helper2(root.left)
                global gg 
                temp=root.val
                root.val = gg
                gg = gg-temp
                print(root.val)
                helper2(root.right)
        
        helper2(root)
        return root