def sol(arr, target):
    seen = set()   # store elements while checking
    for num in arr:
        needed = target - num   # what number we need  
        if needed in seen:      # check if it already exists
            return True
        seen.add(num)           # else add current number
    return False
arr = [8, 4, 1, 6]
target = 12
print("Pair exists:", sol(arr, target))
