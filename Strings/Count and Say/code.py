class Solution:
    def countAndSay(self, n: int) -> str:
        j=1
        s="1"
        while(j<n):
            c=1
            st=s
            s=""
            for i in range(1,len(st)):
                if st[i]==st[i-1]:
                    c+=1
                else:
                    s=s+str(c)+st[i-1]
                    c=1
            s=s+str(c)+st[-1]
            j+=1
        return s
