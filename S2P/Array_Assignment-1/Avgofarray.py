def Avg(arr):
    sum=arr[0]
    for i in range(1,len(arr)):
        sum +=arr[i]
    
    return sum //len(arr)

print(Avg([1, 2, 3, 4, 5]))
print(Avg([5, 8, 11]))
