class Solution(object):
    def searchInsert(self, nums, target):
        l,r=0,len(nums)-1
        ans = 0
        found = False
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                found = True
                ans = mid 
                break
            elif nums[mid] > target:
                ans = mid -1
                r = mid -1
            else:
                l = mid + 1
        return ans
