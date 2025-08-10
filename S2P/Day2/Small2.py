def solu(arr):
    small=arr[0]
    small2=float("-inf") # lowest ele in arry 
    for i in range(1,len(arr)):
        if small>arr[i] :
            small2=small
            small=arr[i]
        elif small2 > arr[i] and small != small2:
            small2=arr[i]
    return small2

arr=[10,1,2,5]
print(solu(arr))
        