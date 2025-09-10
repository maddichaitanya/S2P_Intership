def intersection(nums1, nums2):  
    result = [] 
    nums1.sort()
    nums2.sort()
    i = j = 0
    while i < len(nums1) and j < len(nums2):  
        if nums1[i] == nums2[j]:
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1 
    return result
print(intersection([1, 2, 2, 3, 5], [1, 2, 7]))        # Output: [1, 2]
print(intersection([1, 2, 2, 3, 3], [2, 3, 3, 4, 5]))  # Output: [2, 3]
