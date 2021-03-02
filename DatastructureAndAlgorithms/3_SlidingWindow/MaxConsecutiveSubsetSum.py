import random

# brute force way: O(n^2)
def MaxConsecutiveSubsetSumBruteForce(max_sum, arr, subset_len):
    arr_len = len(arr)
    for i in range(arr_len - subset_len + 1):
        subset_sum = 0
        # print(arr[i])
        for j in range(subset_len):
            # print(arr[i],arr[i+j])
            subset_sum += arr[i + j]
            # print(loopSum)
        max_sum = max(max_sum, subset_sum)
        # print(max_sum)
    return max_sum


# optimised: sliding window method: O(n)
def MaxConsecutiveSubsetSumSlidingWindow(arr, subset_len):
    if len(arr) < subset_len:
        return -1
    else:
        subset_sum = sum([arr[i] for i in range(subset_len)])
        max_sum = subset_sum
        for i in range(len(arr) - subset_len):
            subset_sum = subset_sum - arr[i] + arr[i + subset_len]
            max_sum = max(max_sum, subset_sum)
            # print(subset_sum)
        return max_sum


arr = [1, 2, 3, 4, 5, 6]
arr1 = [80, -50, 90, 100]
subset_len = 2
max_sum = random.randint(-100000, -1000)
print(MaxConsecutiveSubsetSumBruteForce(max_sum, arr1, subset_len))
