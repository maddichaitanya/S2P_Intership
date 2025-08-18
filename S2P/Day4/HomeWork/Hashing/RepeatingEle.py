# def sol(arr):
#     seen = {}
#     for i, num in enumerate(arr):
#         if num in seen:
#             return num
#         else:
#             seen[num] = i
#     return None  # If no repeating element

# # Time Complexity: O(n)
# # Space Complexity: O(n)
# arr = [10, 5, 3, 4, 3, 5, 6]
# print("First Repeating Element:", sol(arr))


def sol(arr):
    seen = set()   # to store visited elements
    for num in arr:
        if num in seen:   # if already seen, it's repeating
            return num
        seen.add(num)     # otherwise add to set
    return None   # if no repeating element

arr = [10, 5, 3, 4, 3, 5, 6]
print("First Repeating:", sol(arr))
