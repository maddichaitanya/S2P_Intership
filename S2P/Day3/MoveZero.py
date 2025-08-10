# move ele to right 
def sol(arr):
    j= -1
    for i in range(len(arr)):  # checking any Zero ele present or not 
        if arr[i]==0:
            j=i           # arr = [1,2,34,5,6,9] 
            break 
    if j == -1:
        return arr
    for i in range(j+1, len(arr)):
        if arr[i] != 0:
            arr[i],arr[j]=arr[j],arr[i]   
            j+=1  
    
    return arr


arr=[1,2,0,1,4,0,5,2]
print(sol(arr))




# def moveZeros(n, arr):
#     j = -1
#     # Step 1: Find the index of the first 0
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             j = i
#             break

#     # If no zero found, array is already good
#     if j == -1:
#         return arr

#     # Step 2: Swap non-zero elements ahead of j
#     for i in range(j + 1, len(arr)):
#         if arr[i] != 0:
#             arr[i], arr[j] = arr[j], arr[i]
#             j += 1

#     return arr
