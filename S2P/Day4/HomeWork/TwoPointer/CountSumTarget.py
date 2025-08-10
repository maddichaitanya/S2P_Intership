def sol(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    count = 0
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            count += 1
            left += 1
            right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1
    return count

print(sol([1, 2, 3, 4, 3], 6))