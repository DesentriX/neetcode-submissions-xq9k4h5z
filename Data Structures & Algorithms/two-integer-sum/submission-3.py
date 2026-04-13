class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsv2 = sorted(nums)
        i = 0
        j = i + 1

        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
        
        
            

        
        