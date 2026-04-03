class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup={}

        for i,v in enumerate(nums):
            if v in lookup:
                return [lookup[v],i]
            lookup[target-v]=i