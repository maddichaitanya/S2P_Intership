def String(s):
    for i in range(len(s)):
        for j in range(i,len(s)):
            for k in range(i,j):
                print(s[k],end=" ")
            print()

s=['a','b','c','d','e']
String(s)
