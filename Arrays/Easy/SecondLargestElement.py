class Solution:
    def getSecondLargest(self, arr):
        max = arr[0]
        secMax=-1
        for el in arr[1:]:
            if(max < el):
                secMax = max 
                max = el
            if(el>secMax and not (max == el)):
                secMax = el
        return secMax