class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def pos(nums,target):
            l,h=0,len(nums)-1
            while l<=h:
                mid=(l+h)//2
                if nums[mid]<target:
                    l=mid+1
                else:
                    h=mid-1
            return l
        if target in nums:
            lpos=pos(nums,target)
            rpos=pos(nums,target+1)-1
            return [lpos,rpos]
        return [-1,-1]
