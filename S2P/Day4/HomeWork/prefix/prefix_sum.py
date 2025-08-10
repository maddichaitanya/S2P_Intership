def sol(arr):
    prefix = []
    total = 0
    for num in arr:
        total += num
        prefix.append(total)
    return prefix

arr = [1, 2, 3, 4, 5]
print("Prefix Sum Array:", sol(arr))
