class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        
        total = nums[0]
        running_sum = [nums[0]]
        start = 0
        curr = 0

        while curr < len(nums):
            current_slice_sum = sum(nums[start:curr+1])
            if current_slice_sum < nums[curr]:
                start = curr
                current_slice_sum = nums[curr]
            
            running_sum.append(current_slice_sum)
            curr += 1
        
        return max(running_sum)