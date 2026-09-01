class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]


        currsum = 0
        maxi = nums[0]

        for elm in nums:
            if currsum < 0:
                currsum = 0
            currsum += elm
            maxi = max(maxi, currsum)


        return maxi



       






        
        