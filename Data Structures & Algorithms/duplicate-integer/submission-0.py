class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        sNum = set(nums)
        
        return len(sNum)!=len(nums)