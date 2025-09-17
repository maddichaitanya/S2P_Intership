def sol(s):
    h =[0] * 26 
    for c in s:
        h[ord(c)-97] += 1   # h[i] => h[0]= 2 ,h[1]= 2,h[2]= 1, h[3]= 0 , h[4]=0 , h[5]=0 ...........,h[25]=0
    for i in range(len(h)):  #
        if h[i] > 1:
            print(chr(i+97))
print("Duplicates without frequency value : ")

sol("aabbcdee")
print()
print("Duplicates with frequency value : ")
def sol(s):
    h =[0] * 26 
    for c in s:
        h[ord(c)-97] += 1
    for i in range(len(h)):
        if h[i] > 0:
            print(chr(i+97), ":", h[i]) 

sol("aabbc")
