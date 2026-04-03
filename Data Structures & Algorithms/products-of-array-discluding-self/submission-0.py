import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prod = np.array([1]*n)
        np_nums=np.array(nums)
        result = []

        for i in range(n):
            temp = np_nums[i]
            np_nums[i]=1
            result.append(np.prod(np_nums))
            np_nums[i]=temp
        return result


