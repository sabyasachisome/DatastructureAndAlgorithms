"""
Merge Sort:
    
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = (l+r)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
"""
arr= [10,9,8,7,6]

def mergeSort(arr):
    if len(arr)>1:
#         print('Inside mergeSort')
        mid= len(arr)//2
#         print(mid)
        left= arr[:mid]
#         print(left)
        right= arr[mid:]
#         print(right)
        
        mergeSort(left)
#         print(left)
        mergeSort(right)
#         print(right)

        i=j=k=0
        while i< len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
#         remaining items
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1

print(arr)
mergeSort(arr)
print(arr)

"""
Quick Sort:

Like Merge Sort, QuickSort is also a divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

Always pick first element as pivot.
Always pick last element as pivot (implemented below)
Pick a random element as pivot.
Pick median as pivot.
The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.
"""			 
arr=[10,9,8,7,6]

def partition(arr, low, high):
    pivot= arr[high]
    i=low-1
    for j in range(low, high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]= arr[high], arr[i+1]
    i+=1
    return i

def quickSort(arr, low, high):
    if(low<high):
        pivot= partition(arr, low, high)
#         print(pivot)

        quickSort(arr, low, pivot-1)
#         print(arr)
        quickSort(arr,pivot+1, high)
#         print(arr)

print(arr)
quickSort(arr, 0, len(arr)-1)
print(arr)

"""
Selection Sort:

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.
"""
arr=[10,9,8,7,6]

def selectionSort(arr):
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[i]:
                min_idx= j
        arr[min_idx],arr[i]= arr[i],arr[min_idx]

print(arr)
selectionSort(arr)
print(arr)

"""
Bubble Sort:

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
"""
arr=[9,8,7,6,5]
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range((len(arr)-i-1)):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)
bubbleSort(arr)
print(arr)