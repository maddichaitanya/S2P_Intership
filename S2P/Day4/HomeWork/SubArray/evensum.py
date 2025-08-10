#Given an array ARR of integers, return the length of the longest subarray whose sum is even. If there is no such subarray, return 0.

def longest_even_sum_subarray(arr):
    n = len(arr)
    max_len = 0
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            if total % 2 == 0:  # even sum
                max_len = max(max_len, j - i + 1)
    
    return max_len

# Example 1
arr = [1, 2, 3, 4]
print(longest_even_sum_subarray(arr))  # Output: 4

# Example 2
arr = [1, 3, 5]
print(longest_even_sum_subarray(arr))  # Output: 0
