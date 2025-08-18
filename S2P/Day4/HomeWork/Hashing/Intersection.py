def sol(union_result):
    for i in range(len(union_result)):
        for j in range(i+1, len(union_result)):
            if union_result[i] > union_result[j]:
                union_result[i], union_result[j] = union_result[j], union_result[i]
    return union_result    

arr1=[1,2,3,4,5]
arr2=[6,7,4,5,3]
result= arr1 and arr2
print("Union",sol(result) )

