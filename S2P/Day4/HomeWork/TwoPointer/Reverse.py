def sol(arr):
    left, right = 0, len(arr) - 1 
    for _ in range(len(arr) // 2): # 2 
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr=[1,2,3,4,5]
print(sol(arr))