class Solution:
    def bubbleSort(self,arr):
        for i in range(1,len(arr)):
            self.helper(arr,i,0)
        
        
    def helper(self,arr,i,j):
        if j == len(arr):
            return
        else:
            if(arr[j]>arr[i]):
                arr[i],arr[j]=arr[j],arr[i]
            self.helper(arr,i,j+1)
            

        