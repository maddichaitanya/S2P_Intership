def union(nums1, nums2):
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
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
        else:
            if not result or result[-1] != nums2[j]:
                result.append(nums2[j])
            j += 1
    while i < len(nums1):
        if not result or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1
    while j < len(nums2):
        if not result or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1

    return result

print(union([1, 2, 2, 3, 5], [1, 2, 7]))        # Output: [1, 2, 3, 5, 7]

print(union([1, 2, 2, 3, 3], [2, 3, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
