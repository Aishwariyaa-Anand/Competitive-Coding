class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []
        for i in operations:
            if i == '+':
                rec.append(rec[-1]+rec[-2])
            elif i == 'C':
                rec.pop()
            elif i == 'D':
                rec.append(2*rec[-1])
            else:
                rec.append(int(i))
        return sum(rec)
