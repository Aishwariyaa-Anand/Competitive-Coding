class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res=[]
        for op in tokens:
            if op=='+':
                a,b=res.pop(),res.pop()
                res.append(b+a)
            elif op=='-':
                a,b=res.pop(),res.pop()
                res.append(b-a)
            elif op=='*':
                a,b=res.pop(),res.pop()
                res.append(b*a)
            elif op=='/':
                a,b=res.pop(),res.pop()
                res.append(int(b/a))
            else:
                res.append(int(op))
        return res.pop()
