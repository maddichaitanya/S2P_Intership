def sol(arr, k):
    res = 1
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sum = 1
            for l in range(i,j+1):
                sum *= arr[l]
            if sum == k:
                subarrlen = j - i + 1
                res = max(res, subarrlen)
    return res
arr = [-5, 8, -14, 2, 4, 12]
k = -40
print(sol(arr, k))   #[-5*8]
