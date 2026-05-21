class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        if len(nums) == 0:
            return 0

        new = sorted(nums)
        seen = set()


        current = 1
        longest = 1

       


        for i in range(1, len(new)):

            
            if new[i] in seen:
                continue
            if new[i] - new[i-1] == 1:
                seen.add(new[i])
                current += 1
            else:
                current = 1
                continue

            longest = max(current, longest)

        return longest






       

            

    

        
            


       

        


        


       
        


        