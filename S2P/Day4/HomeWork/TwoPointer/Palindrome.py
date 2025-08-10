def is_palindrome(arr):
    left, right = 0, len(arr) - 1
    for _ in range(len(arr) // 2):
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome([1, 2, 3, 2, 1]))