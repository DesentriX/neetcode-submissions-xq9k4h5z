class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        
       
        
        for i in range(len(nums)):
            j = i +1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0  and k != i and i!=j and j!=k:
                    out.append([nums[i], nums[j], nums[k]])

                if nums[j] + nums[k] < target:
                    j +=1
                else:
                    k -=1

        unique = list({tuple(x) for x in out})
        unique = [list(x) for x in unique]

        return unique
                
                



   










        
        