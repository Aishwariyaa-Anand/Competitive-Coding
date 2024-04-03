class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a,b = [],[]
        for i in range(len(s)):
            a.append(s.index(s[i]))
            b.append(t.index(t[i]))
        if a==b:
            return True
        else:
            return False
