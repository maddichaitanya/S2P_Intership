def sol(arr):
    for i in range(1,len(arr)):
        arr[i] += arr[i-1]
    return arr

arr = [1, 2, 3, 4, 5]
print("Prefix Sum Array:", sol(arr))
