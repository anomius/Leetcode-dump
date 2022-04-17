# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        k=[]
        def helper(root):
            if root:
                helper(root.left)
                k.append(root.val) 
                helper(root.right)
        helper(root)
        l=k.copy()
        k.sort()
        dic=[l[i]-k[i] for i in range(len(k))]
       
        global count
        count=0
        def helper2(root):
            if root:
                global count
                helper2(root.left)
                root.val-=dic[count] 
                
                count+=1
                helper2(root.right)
        helper2(root)
        