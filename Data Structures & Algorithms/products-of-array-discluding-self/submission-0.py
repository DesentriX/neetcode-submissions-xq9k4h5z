import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        myl= []
        for i in range(len(nums)):
            res= math.prod(nums[i+1:]) * math.prod(nums[:i])
            myl.append(res)
           
        return myl


        