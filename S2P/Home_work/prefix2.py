
def sum(arr):
    prefixsum=[0]*len(arr)  #[2,0,0,0,0]
    prefixsum[0]=arr[0]      
    for i in range(1,len(arr)):
        for j in range(0,i+1):  
            prefixsum[i]=prefixsum[i]+arr[j] 
    return prefixsum
arr=[2,3,4,5,6]
print(sum(arr))




# def prefix_sum(arr):
#     prefixsum = [0] * len(arr)
#     prefixsum[0]=arr[0]
#     for i in range(1,len(arr)):              
#         total = 0
#         for j in range(0,i+1):       
#             total += arr[j]
#         prefixsum[i] = total        
#     return prefixsum
# arr = [2, 3, 4, 5, 6]
# print(prefix_sum(arr))



