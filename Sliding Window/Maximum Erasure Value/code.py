class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        j=1
        maxsc=0
        l=[nums[0]]
        while j<len(nums):
            if nums[j] not in l:
                l.append(nums[j])
            else:
                maxsc=max(sum(l),maxsc)
                x=l.index(nums[j])
                l=l[x+1:]
                l.append(nums[j])
            j+=1
        maxsc=max(sum(l),maxsc)
        return maxsc
