a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if( a>b and a>c):
    print("largest",a)
elif(b>c):
    print("largest",b)
else:
    print("largest",c)