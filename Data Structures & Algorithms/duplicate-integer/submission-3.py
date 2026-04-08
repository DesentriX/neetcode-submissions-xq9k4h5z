class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict = dict()
        i = 0
       
       
        while i < len(nums):
            if nums[i] not in mydict:
                mydict[nums[i]] = 1   
            else:
                mydict[nums[i]] += 1
            i+=1
        
        for value in mydict.values():
            if value > 1:
                return True
        return False
        

               

       
            
           


        