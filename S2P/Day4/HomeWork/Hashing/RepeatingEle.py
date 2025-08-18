def sol(arr):
    seen = {}
    for i, num in enumerate(arr):
        if num in seen:
            return num
        else:
            seen[num] = i
    return None  # If no repeating element

# Time Complexity: O(n)
# Space Complexity: O(n)
arr = [10, 5, 3, 4, 3, 5, 6]
print("First Repeating Element:", sol(arr))
