def bubblesort(num):
    for i in range(len(num)-1,0,-1):  #  pass=4  {4,3,2,1} 
        for j in range(i):  
            if num[j]>num[j+1]:  
                num[j],num[j+1]=num[j+1],num[j]
    return num
num=[10,9,6,4,5]
print(bubblesort(num))


#  Pass      Result            
#   1     [9, 6, 4, 5, 10] 
#   2     [6, 4, 5, 9, 10] 
#   3     [4, 5, 6, 9, 10] 
#   4     [4, 5, 6, 9, 10] 


            
