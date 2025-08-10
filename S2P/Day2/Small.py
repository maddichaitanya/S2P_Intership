def solu(arr):
    small=arr[0]
    for i in range(1,len(arr)):
        if small > arr[i]:
            small=arr[i]
        
    return small

arr=[1,2,3,4,5]
print(solu(arr))