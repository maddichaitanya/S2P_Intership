# def subarray(arr):
#     for i in range(len(arr)):
#         for j in range(0,i+1):
#             print(arr[j],end=' ')
#         print()

# arr=[10,20,30,40,50]
# print(subarray(arr))





def print_subarrays(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            print(arr[i:j+1])  


arr = [1, 2, 3]
print_subarrays(arr)