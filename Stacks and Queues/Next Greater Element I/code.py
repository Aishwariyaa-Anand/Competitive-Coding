class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums1:
            if i in nums2:
                ind = nums2.index(i)
                x = -1
                while ind < len(nums2):
                    if nums2[ind] > i:
                        x = nums2[ind]
                        break
                    ind+=1
            res.append(x)
        return res
