def solu(arr):
    largest=arr[0]
    for i in range(len(arr)):
        if largest < arr[i]:
            largest=arr[i]
    return largest

arr=[1,2,3,4,5,100]
print(solu(arr))
