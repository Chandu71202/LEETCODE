class Solution:
    def maxArea(self,height):
        if len(height) ==2:
            return min(height)
        
        start,end = 0, len(height)-1
        curr, maxi = 0, 0
        
        for _ in range(len(height)):
            curr = (end-start) * min(height[start], height[end])
            maxi = max(maxi, curr)
            if height[start]<  height[end]:
                start +=1
            else:
                end -=1
        return maxi
