def sol(arr):
    maxsum=0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum=0 
            for k in range(i,j+1):
                sum =sum+arr[k]
                if maxsum < sum:
                    maxsum =sum
    return maxsum 
arr=[-1,-3,1,7,-1]
print(sol(arr)) 


















# def sol(arr):
#     maxproduct=1
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             sum=1
#             for k in range(i,j+1):
#                 sum =sum*arr[k]
#                 if maxproduct < sum:
#                     maxproduct =sum
#     return maxproduct 
# arr=[-1,-3,1,7,-1]
# print(sol(arr))