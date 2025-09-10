def sol(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            for k in range(i,j+1):
                print(arr[k],end=' ')
            print()
        print()       

arr=[10,20,30,40]
sol(arr)

