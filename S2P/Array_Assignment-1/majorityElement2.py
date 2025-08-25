'''Given an integer array nums of size n, return the which appar more than 
    n/3 times in the array. 
    The output can be returned in any order'''

def majorityElement(nums):
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] = freq[num] + 1                    #freq={1:3,2:2,3:1},freq={1:3,2:3,3:1}                 
    result = []
    for key,value in freq.items():
        if value > len(nums) // 3:
            result.append((key,value))
    return result

print(majorityElement([1, 2, 1, 1, 3, 2]))     # Output: [(1,3)]
print(majorityElement([1, 2, 1, 1, 3, 2, 2]))  # Output: [(1,3), (2,3)]
print(majorityElement([7,7,1,1,2,2]))  # Output: []              No element appears more than 2 times.n=6,6//3 =2        
