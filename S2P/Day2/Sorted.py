# def solu(arr):
#     cout=0
#     for i in arr:
#         cout += 1
#     return cout

# arr=[1,2,3,4,5]
# print(solu(arr))

def solu(arr):
    issorted=True
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            issorted=False
            break
    return issorted

arr=[1,2,3,4,5]
print(solu(arr))
