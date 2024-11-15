def selectionSort(arr):
    for i in range(len(arr)):
        min = select(arr,i)
        arr[i],arr[min] = arr[min],arr[i]
        
def select(arr,n):
    min = n
    for i in range(n+1, len(arr)):
        if(arr[min]>arr[i]):
            min = i
    return min

#Test selection
array = [64, 25, 12, 22, 11]
for a in array:
    print(a, end=" ")
selectionSort(array)
print("\n")
for a in array:
    print(a, end=" ")
