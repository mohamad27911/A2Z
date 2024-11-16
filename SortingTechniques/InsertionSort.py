class Solution:
    def insert(self, alist, index, n):
        alist.insert(index, n)
        self.insertionSort(alist, len(alist))

    def insertionSort(self, alist, n):
        for i in range(1, n):
            key = alist[i]
            j = i - 1
            while j >= 0 and alist[j] > key:
                alist[j + 1] = alist[j]
                j -= 1
            alist[j + 1] = key