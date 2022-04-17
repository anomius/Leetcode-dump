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
        stack=[]
        prev=None
        nxt=None
        first=None
        middle=None
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            tmp=stack.pop()
            if prev!=None and prev.val>tmp.val:
                if first==None:
                    first=prev
                    middle=tmp
                else:
                    nxt=tmp
            prev=tmp
            root=tmp.right
        if first and nxt:
            first.val,nxt.val=nxt.val,first.val
        elif first and middle:
            first.val,middle.val=middle.val,first.val
        