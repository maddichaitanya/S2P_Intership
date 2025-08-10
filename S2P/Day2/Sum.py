def solution(arr):
    sum=arr[0]
    for i in range(1,len(arr)): 
        sum += arr[i] 
    return sum

arr=[1,2,3,4,5]
print(solution(arr))