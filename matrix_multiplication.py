row1=int(input())
col1=int(input())
row2=int(input())
col2=int(input())
m1=[]
m2=[]
r=[]
if(col1==row2):
    for i in range(row1):
        t=[]
        for j in range(col1):
            a=int(input())
            t.append(a)
        m1.append(t)
    for i in range(row1):
        for j in range(col1):
            print(m1[i][j],end=" ")
        print()
        
    for i in range(row2):
        t=[]
        for j in range(col2):
            a=int(input())
            t.append(a)
        m2.append(t)
    for i in range(row2):
        for j in range(col2):
            print(m2[i][j],end=" ")
        print()
        
    for i in range(len(m1)):
        t=[]
        for j in range(len(m2[0])):
            a=0
            for k in range(len(m2)):
                a+=m1[i][k]*m2[k][j]
            t.append(a)
        r.append(t)
          
        
        
    for i in range(row1):
        for j in range(col2):
            print(r[i][j],end=" ")
        print()
            
    


