def range_sum_query(arr, queries):
    n = len(arr)
    prefix = [0] * n    #[0,0,0,0,0]
    prefix[0] = arr[0]    
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]
    results = []                 #[2, 6, 12, 20, 30]
    for L, R in queries:
        if L == 0:
            results.append(prefix[R]) 
        else:
            results.append(prefix[R] - prefix[L - 1])
    return results
arr = [2, 4, 6, 8, 10]
queries = [(1, 3), (0, 4), (2, 2)]
print(range_sum_query(arr, queries))  # Output: [18, 30, 6]
