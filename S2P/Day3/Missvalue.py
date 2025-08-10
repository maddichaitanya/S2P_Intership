def sol(arr):
    n=arr[-1]
    sum1=(n*(n+1))//2
    sum2=0
    for i in range(len(arr)):
        sum2 +=arr[i]
    
    return sum1-sum2

arr=[1,2,3,5]
print(sol(arr))