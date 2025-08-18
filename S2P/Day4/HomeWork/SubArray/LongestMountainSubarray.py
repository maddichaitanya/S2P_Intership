def longest_mountain(arr):
    n = len(arr)
    longest = 0
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:  
            left = i
            right = i
            while left > 0 and arr[left] > arr[left - 1]:
                left -= 1
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1
            length = right - left + 1
            longest = max(longest, length)
    return longest 

arr = [2, 1, 4, 7, 3, 2]   
print(longest_mountain(arr))  # Output: 5  





""""
Move left from the peak until the numbers stop going up

Move right from the peak until the numbers stop going down

The distance between left and right gives mountain length

"""