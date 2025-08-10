def sol(arr, target):
    left = 0
    right = len(arr) - 1 
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return arr[left], arr[right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return None


arr=[1,2,3,2,1]
print(sol(arr,2))