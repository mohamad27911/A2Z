class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m =0
        current=0
        for i in range(len(nums)):
            if nums[i]==0:
                m = max(m,current)
                current=0
            else:
                current=current+1
        m = max(m, current)
        return m