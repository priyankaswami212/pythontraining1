name=input("enter name")
age=int(input("enter age"))

def year100(age):

    age=100-age
    year=2021+age
    return year

print(year100(age),"In this age you'll turn 100")