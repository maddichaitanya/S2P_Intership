def sol(arr):
    pos=[]
    neg=[]
    for i in range(1,len(arr)):
        if arr[i]>=0 :
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    for i in range(len(arr)//2):
        arr[2*i]=pos[i]
        arr[2*i+1]=neg[i]
    return arr

arr=[1,-2,3,-4,5]
print(sol(arr))