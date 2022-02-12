class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        l=list(re.sub(r'\s|[0-9]+', '', licensePlate).lower())
        #print(l)
        words=sorted(words, key=len)
        for i in words:
            i_l=list(i)
            #print(i_l)
            for k in l:
                flag=1
                if k in i_l:
                    i_l.remove(k)
                else:
                    flag=0
                    break
            if flag==1:
                return i
            
            
        