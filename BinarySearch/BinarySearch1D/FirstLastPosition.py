class Solution(object):
    def searchRange(self, nums, target):
        def find_left(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        def find_right(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        left = find_left(nums, target)
        right = find_right(nums, target)

        if left <= right and left < len(nums) and nums[left] == target:
            return [left, right]
        return [-1, -1]
