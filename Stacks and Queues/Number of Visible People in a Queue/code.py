class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res=[1]*len(heights)
        st=[]
        i=len(heights)-1
        while i>=0:
            c=0
            while st and heights[st[-1]]<heights[i]:
                st.pop()
                c+=1
            if st:
                res[i] += c
            else:
                res[i] = c
            st.append(i)
            i-=1
        return res
