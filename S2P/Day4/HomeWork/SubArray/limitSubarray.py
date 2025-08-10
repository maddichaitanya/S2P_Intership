# Longest Contiguous Subarray With Absolute Diff Bounded by a Limit 
#https://www.naukri.com/code360/problems/longest-contiguous-subarray-with-absolute-diff-bounded-by-a-limit_977250

def longest_subarray(arr, limit):
    n = len(arr)
    max_len = 0
    for i in range(n):  # starting index i
        for j in range(i, n):  # ending index of ith first++ value 
            sub = arr[i:j+1]  # current subarray
            max_val = max(sub)
            min_val = min(sub)
            
            if max_val - min_val <= limit:
                max_len = max(max_len, j - i + 1)
    
    return max_len

arr = [8, 2, 4, 7]
limit = 4
print(longest_subarray(arr, limit))  # Output: 2 
