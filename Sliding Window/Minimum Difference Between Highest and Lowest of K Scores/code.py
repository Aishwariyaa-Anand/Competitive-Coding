class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k==1:
            return 0
        minsc=max(nums)
        nums.sort()
        for i in range(k,len(nums)+1):
            minsc=min(minsc,nums[i-1]-nums[i-k])
        return minsc
