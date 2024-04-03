class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        st=[len(temperatures)-1]
        i=len(temperatures)-2
        while i>=0:
            while st and temperatures[i]>=temperatures[st[-1]]:
                st.pop()
            if len(st)==0:
                res[i]=0
            else:
                res[i]=st[-1]-i
            st.append(i)
            i-=1
        return res
