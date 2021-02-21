class Solution:
    def binary_search(self, arr, low, high, target):
        if high>=low:
            mid= (low+high)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                return self.binary_search(arr, low, mid-1, target)
            elif arr[mid]<target:
                return self.binary_search(arr, mid+1, high, target)
        else:
            return -1

    def binary_search_iter(self, arr, low, high, target):
        while(low<=high):
            mid= (low+high)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                low= mid+1
            elif arr[mid]>target:
                high= mid-1
        return -1

arr=[1,2,3,4,5]

s= Solution()

print(s.binary_search(arr, 0, len(arr)-1,4))

print(s.binary_search_iter(arr, 0, len(arr)-1,4))