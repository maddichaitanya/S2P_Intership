'''Given an integer array nums of size n, return the majority ele of array 
    
    The majority ele of an ele that appears more than n/2 times in the array. 
    The array is guaranted to have a majority ele'''


def majorityElement(nums):
    freq = {}
    for num in nums:
        if num not in freq:  
            freq[num] = 1
        else:
            freq[num] = freq[num] + 1           #num=9 freq = {7:5,0:2,1:1,2:1}  num=6 feq={1:4,2:2}
    for key,value in freq.items():             #items = iterate both key & value
        if value > len(nums) // 2:
            return key,value


print(majorityElement([7, 0, 0, 1, 7, 7, 2, 7, 7]))  # Output: (7,5)
print(majorityElement([1, 1, 1, 2, 1, 2]))           # Output: (1,4) 
# print(majorityElement([1,1,2,3,4,5,5]))
# print(majorityElement([1,1,5,5]))


'''Here n/2 = 2, but both elements appear exactly 2 times, not greater.
So again → no majority element exists → function returns None.'''