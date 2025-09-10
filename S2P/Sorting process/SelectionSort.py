'''Works by selecting the smallest element and putting it at the beginning.

Find minimum from unsorted part.

Swap with the first unsorted element.'''

def Selection(num):
    for i in range(0,len(num)-1):
        min=i 
        for j in range(i+1,len(num)):
             if num[j]<num[min]:
                min=j
        num[i],num[min]=num[min],num[i]
    return num 
num=[14,4,5,3,8,10]
print(Selection(num))   