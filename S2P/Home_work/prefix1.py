def sum(arr):
    prefix=[0]*len(arr)
    prefix[0]=arr[0]
    for i in range(1,len(arr)):
        prefix[i] =prefix[i-1]+arr[i]
    return prefix

arr=[2,3,4,5,6]
print(sum(arr))


#tc=o(n)
#s =O(n)