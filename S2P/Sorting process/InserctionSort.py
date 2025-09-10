def insertion(num):
    for i in range(0,len(num)-1):
        j=i+1
        while num[j-1]>num[j] and j>0:
            num[j-1],num[j]=num[j],num[j-1]  
            j-=1
    return num

num =[4,3,2,5,6,9]
print(insertion(num))

'''Works like how we arrange playing cards in our hand.

Start from the 2nd element.

Compare it with the left side and insert it in the correct position.

Repeat until the array is sorted.'''
