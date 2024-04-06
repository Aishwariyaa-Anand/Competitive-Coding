class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k=len(p)
        r=[i for i in p]
        r.sort()
        res=[]
        for i in range(k,len(s)+1):
            x=list(s[i-k:i])
            x.sort()
            if x==r:
                res.append(i-k)
        return res
