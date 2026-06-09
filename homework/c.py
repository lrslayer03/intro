n=int(input("number of terms :  ")) 
x,y=0,1
print(x)
print(y)
for i in range(3, n+1):
    z=x+y
    print(z)
    x=y
    y=x

