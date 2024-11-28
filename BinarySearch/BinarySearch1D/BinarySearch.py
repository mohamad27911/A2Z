class Solution(object):
        def search(self,arr, x):
            low = 0
            high = len(arr) - 1
            while high >= low:
        
                mid = (high + low) // 2
        
                if arr[mid] == x:
                    return mid
        
                elif arr[mid] > x:
                    high = mid - 1
        
                else:
                    low= mid + 1

            else:
                return -1