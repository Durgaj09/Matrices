r=int(input())
c=int(input())
m1=[]
for i in range(r):
    t=[]
    for j in range(c):
        a=int(input())
        t.append(a)
    m1.append(t)
    
a=[]
for i in range(r):
    
    sum=0
    for j in range(c):
        sum+=m1[i][j]
    a.append(sum)
a=max(a)

b=[]
for i in range(c):
    
    sum=0
    for j in range(r):
        sum+=m1[j][i]
    b.append(sum)
b=max(b)

print(a+b)
    




        