def consecutiveOnes(arr):
    count = 0 
    maxcount = 0 
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1    
        else:
            count = 0
        if count > maxcount:
            maxcount = count
    return maxcount

arr = [1, 0, 0, 1, 1, 1,1, 0]  #arr=[2,0,0,0]
print(consecutiveOnes(arr))
