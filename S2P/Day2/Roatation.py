#Left Rotation 

def solu(arr):
    temp=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[-1]=temp
    return arr
arr=[1,2,3,4,5]
print(solu(arr))


#Rigth Rotation 

def solu(arr):
    temp = arr[-1]
    for i in range(len(arr)-2, -1, -1):  
        arr[i+1] = arr[i]
    arr[0] = temp
    return arr

arr=[1,2,3,4,5]
print(solu(arr))

#left 
def left_rotate(arr, k):
    n = len(arr)
    k = k % n   # to handle if k > n
    return arr[k:] + arr[:k]
arr = [1, 2, 3, 4, 5]
print("Left Rotate by 2:", left_rotate(arr, 2))

def right_rotate(arr, k):
    n = len(arr)
    k = k % n   # to handle if k > n
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5]
print("Left Rotate by 2:", right_rotate(arr, 2))

