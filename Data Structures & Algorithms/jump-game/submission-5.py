class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True
        
    
        n = len(nums)-1
        target = n
        space = 0

        for i in range(target - 1, -1, -1):
            if nums[i] + i >= target :
                target = i
                space = 0
           
            if target == 0:
                return True
            
        return False
            




       
            

        