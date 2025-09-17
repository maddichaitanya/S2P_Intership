def largest_odd(s):
    n = len(s)
    start = 0
    while start < n and s[start] == '0': 
        start += 1
    end = -1
    for i in range(n-1,start-1, -1):
        d = ord(s[i]) - ord('0')        # 50-48                             
        if d % 2 == 1:   # odd check
            end = i
            break
    if end == -1 or start > end:
        return "-1"
    return s[start:end+1]
 
print(largest_odd("42"))     
print(largest_odd("023")) 
print(largest_odd("00214632"))      