class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        for i in s:
            if i=='#' and len(stack1)!=0:
                stack1.pop(-1)
            elif i=='#':
                continue
            else:
                stack1.append(i)
        for i in t:
            if i=='#' and len(stack2)!=0:
                stack2.pop(-1)
            elif i=='#':
                continue
            else:
                stack2.append(i)
        print(stack1,stack2)
        if len(stack1)==len(stack2):
            for i in range(len(stack1)):
                if stack1[i]!=stack2[i]:
                    return False
        else:
            return False
        return True
        
        