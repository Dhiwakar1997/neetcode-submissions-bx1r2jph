class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[-1] or len(nums)==1:
            return nums[0]

        i=-1
        while nums[i-1]<nums[i]:
            i-=1
        return nums[i]