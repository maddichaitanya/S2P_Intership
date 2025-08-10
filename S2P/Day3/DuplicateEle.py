#Removeing duplicate ele from arr 

def sol(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[i] != arr[j]:
            i +=1
            arr[i]=arr[j]
    return i+1                         #arr[:i+1]      arr[start : end]
arr=[1,1,2,2,3,3]
print(sol(arr))












# def sol(arr):
#     if not arr:
#         return 0
    
#     i = 0
#     for j in range(1, len(arr)):
#         if arr[i] != arr[j]:
#             i += 1
#             arr[i] = arr[j]

#     return arr[:i+1]

# arr = [1, 1, 2, 2, 3, 3]
# new_arr = sol(arr)
# print("Updated array without duplicates:", new_arr)
# print("Length:", len(new_arr))

