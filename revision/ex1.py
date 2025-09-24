# for i in range(0,10,2):  # (start,end,step)
#     print(i)  # op:- 0,2,4,6,8



#List 
mylist = list()
mylist.append("hello")
mylist.append("nanu")
mylist.append("venu")
print(mylist)

mylist.pop()
mylist.pop()
print(mylist)
mylist.remove("hello")
print(mylist)

# ep1
mylist1=["hello","venu","chiku","sonu","monu"]  
mylist1.insert(2,"kana")
mylist1.remove("venu")
print(mylist1)

# ep2
mylist2=["idli","dosa","Filter coffee","pizza","Biryani"]
print(mylist2)
mylist2.insert(2,"pasta")
print(mylist2)
mylist2.remove("Filter coffee")
print(mylist2)

# count() method
l1=[1,2,1,2,1,2,1,1,1]
occ=l1.count(1)
print(occ)



# List :- is a collection of object(different data Type), which is ordered and changeable. Allows duplicate members.
# Tuple :- is a collection which is ordered and unchangeable. Allows duplicate members.
# Set :- is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary :- is a collection which is ordered** and changeable. No duplicate members.
# *Set items are unchangeable, but you can remove and/or add items whenever you like.