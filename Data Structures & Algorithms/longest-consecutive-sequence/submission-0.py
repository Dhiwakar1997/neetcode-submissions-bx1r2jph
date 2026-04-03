class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        maxLen=0
        for num in nums:
            curLen=1
            if num-1 in numSet:        
                tmp=num
                while tmp in numSet:
                    curLen+=1
                    tmp+=1
            maxLen=max(maxLen,curLen)
        return maxLen