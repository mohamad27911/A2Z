class Solution(object):
    def rotate(self, nums, k):
       k = k % len(nums)
       nums[:] = nums[-k:]+nums[:-k]

Sol = Solution()
print(Sol.rotate([-1,-100,3,99],2))   