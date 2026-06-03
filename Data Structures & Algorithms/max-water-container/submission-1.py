class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxi = 0

        

        for i in range(0, len(heights)):
            for j in range(i+1, len(heights)):
                distance = j - i
                if heights[i] < heights[j] or heights[i] == heights[j] :
                    curr = heights[i] * distance
                if heights[i] > heights[j]:
                    curr = heights[j] * distance
                maxi = max(maxi, curr)

        return maxi
               





      

        return maxi

        
            



        