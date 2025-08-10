def sol(arr):
    maxproduct=1    
    for i in range(len(arr)):
        pord=1
        for j in range(i,len(arr)):
            pord =pord*arr[j]
            if maxproduct < pord:
                maxproduct =pord
    return maxproduct 
arr=[-1,-3,1,7,-1]
print(sol(arr))