#  Shortest subarray with sum at least K
def shortest_subarray_bruteforce(arr, k):
    n = len(arr)
    min_len = float('inf')  # Start with a very large value
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum >= k:
                min_len = min(min_len, j - i + 1)
                break  # No need to extend, we want shortest
    return min_len if min_len != float('inf') else -1
arr = [3, 6, 7, 4, 3]
k = 12
print(shortest_subarray_bruteforce(arr, k))  # Output: 2  [6,7]
