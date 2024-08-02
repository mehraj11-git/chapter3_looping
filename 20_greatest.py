n= int(input("enter a number"))
n1=int(input("enter a second number"))
n2=int(input("enter a third number"))
import random
yoyo=random.randint(1,100)
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(f"greatest{n,n1,n2},{yoyo}")       
