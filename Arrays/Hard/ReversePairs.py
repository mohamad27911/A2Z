class Solution(object):
    def reversePairs(self, nums):
        ans = 0
        for i in range(len(nums)):
            ans += self.binary_search(nums, i + 1, len(nums) - 1, nums[i])
        return ans

    def binary_search(self, arr, low, high, x):
        count = 0
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] * 2 < x: 
                count = mid - low + 1
                low = mid + 1  
            else:
                high = mid - 1  
        return count
