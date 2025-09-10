def sum(arr):
    for i in range(1,len(arr)):
        arr[i] +=arr[i-1] 
    return arr

arr=[2,3,4,5,6]
print(sum(arr))  

