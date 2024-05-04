r=int(input("enter row"))
c=int(input("enter col"))
m=[]
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
top=0
bottom=r-1
left=0
right=c-1
while(top<=bottom and left<=right):
    for i in range(left,right+1):
        print(m[top][i],end="")
    top+=1
    for i in range(top,bottom+1):
        print(m[i][right],end="")
    right-=1
    if(top<=bottom):
        for i in range(right,left-1,-1):
            print(m[bottom][i],end="")
        bottom-=1
    if(left<=right):
        for i in range(bottom,top-1,-1):
            print(m[i][left],end="")
        left+=1
            
    
    

