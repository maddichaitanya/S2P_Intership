# def sol(arr):
#     max_sum = 0
#     left, right = 0, len(arr) - 1
#     for _ in range(len(arr) // 2):
#         total = arr[left] + arr[right]
#         max_sum = max(max_sum, total)
#         left += 1
#         right -= 1
#     return max_sum
# print(sol([1, 2, 3, 4])) 

def sol(arr):
    max_sum = 0
    left, right = 0, len(arr)-1
    for i in range(left,right):
        total=0 
        total = arr[i]+arr[i+1]
        max_sum = max(max_sum, total)
    return max_sum
print(sol([1, 2, 3, 4,5]))
