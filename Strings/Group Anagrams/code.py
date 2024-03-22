class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            x=sorted(i)
            y="".join(x)
            if y in d:
                d[y].append(i)
            else:
                d[y]=[i]
        return d.values()
