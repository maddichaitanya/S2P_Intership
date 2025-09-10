def twoSumAll(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append((i, j))  
    return result 
print(twoSumAll([1, 6, 2, 10, 1], 7))           # output  : [(0, 1), (1, 4)]
print(twoSumAll([1, 3, 5, -7, 6, -3], 0))       # output  : [(1,5)]