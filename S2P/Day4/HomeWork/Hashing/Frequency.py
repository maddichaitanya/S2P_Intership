def sol(arr):
    freq = {}   # dictionary to store element:count
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

# Example
arr = [1, 2, 2, 3, 1, 4]
print("Frequencies:", sol(arr))
