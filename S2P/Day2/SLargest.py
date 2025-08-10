def solu(arr):
    largest=arr[0]
    lag2=float('-inf')

    for i in range(1,len(arr)):
        if largest < arr[i]:
            lag2=largest
            largest=arr[i]
        elif lag2 < arr[i]:
            lag2=arr[i]
    return lag2

arr=[1,2,3,4,5]
print(solu(arr))
            