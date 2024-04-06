class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c=0
        for i in range(3,len(s)+1):
            substr=s[i-3:i]
            if len(set(substr))==3:
                c+=1
        return c
