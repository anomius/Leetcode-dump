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
        print(k)
        l=k.copy()
        k.sort()
        print(k)
        dic=[l[i]-k[i] for i in range(len(k))]
        print(dic)
        global count
        count=0
        def helper2(root):
            if root:
                global count
                helper2(root.left)
                root.val-=dic[count] 
                print(root.val)
                count+=1
                helper2(root.right)
        helper2(root)
        