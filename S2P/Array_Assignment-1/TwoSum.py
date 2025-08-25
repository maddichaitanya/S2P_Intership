def twoSumAll(nums, target):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                result.append([i, j])   # save the pair
    return result 
print(twoSumAll([1, 6, 2, 10, 1], 7))  
print(twoSumAll([1, 3, 5, -7, 6, -3], 0)) 
