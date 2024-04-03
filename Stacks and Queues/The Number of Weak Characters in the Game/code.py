class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda prop: (-prop[0],prop[1]))
        maxd=0
        res=0
        for a,d in properties:
            if d<maxd:
                res+=1
            else:
                maxd = d
        return res
