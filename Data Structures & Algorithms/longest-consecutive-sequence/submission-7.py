class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0


        nums.sort()
        seen = set()
        current = 1
        longest  = 1

        for i in range(1, len(nums)):
            if nums[i] in seen:
                continue
            if nums[i] - nums[i-1] == 1:
                current += 1
            else:
                current = 1
            seen.add(nums[i])


            longest = max(longest, current)

        return longest



        

        






       

            

    

        
            


       

        


        


       
        


        