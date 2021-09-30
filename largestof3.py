a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))

def lar3(a,b,c):

    if( a>b and a>c):
        print("largest",a)
        return a
    elif(b>c):
        print("largest",b)
        return b
    else:
        print("largest",c)
        return c

largest=lar3(a,b,c)
print(largest)