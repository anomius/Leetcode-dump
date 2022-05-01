class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(a:str):
            d=[]
            for i in range(len(a)):
                d.append(a[i])                
                if a[i]=='#':
                    d.pop()
                    try:
                        d.pop()
                    except:
                        c=1
            return d
        s,t=helper(S),helper(T)
        print(s,t)
        return s==t