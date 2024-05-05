r=int(input("enter row"))
c=int(input("enter col"))
m=[]
m2=[]
for i in range(r):
    temp=[]
    for j in range(c):
        a=int(input())
        temp.append(a)
    m.append(temp)
for i in range(r):
    for j in range(c):
        print(m[i][j],end="")
    print()
    
for i in range(c):
    temp=[]
    for j in range(r):
        temp.append(0)
    m2.append(temp)
    


for i in range(r):
    
    for j in range(c):
        m2[j][i]=m[i][j]
    print()
    
for i in range(c):
    for j in range(r):
        print(m2[i][j],end=" ")
    print()
    

        