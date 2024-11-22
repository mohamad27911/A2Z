class Solution(object):
    def maxSubArray(self, nums):
        curr =0 
        m = float('inf')
        for num in nums:
            curr = curr + num
            m = max(m, curr)
            if curr <0:
                curr = 0
        return m
            
        