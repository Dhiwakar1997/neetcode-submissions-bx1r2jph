class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lookup={}

        for i,val in enumerate(numbers):

            if val in lookup:
                return [lookup[val]+1,i+1]
            
            lookup[target-val]=i
        return []