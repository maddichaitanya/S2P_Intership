#List  
mylist = list() 
mylist.append("hello") 
mylist.append("nanu")
mylist.append("venu")
print(mylist)
print(len(mylist)) 

list1=[1,2,"HEllo",True,10.2] 
for i in list1:
    print(i)


list2=["idli","dosa","Filter coffee","pizza","Biryani"]
print(list2)
print(list2[2])  

#append()
list2.append("Tea")
print(list2)

#pop()
list2.pop()
print(list2)

#insert()
list2.insert(2,"pasta")
print(list2)

#remove()
list2.remove("Filter coffee")
print(list2)


