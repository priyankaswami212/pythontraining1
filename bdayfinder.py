
def bday(n):

    if n=="Girija":
        print(n, "birthday is", dict["Girija"])
    if n=="Swami":
        print(n, "birthday is", dict["Swami"])
    if n=="Priyanka":
        print(n, "birthday is", dict["Priyanka"])
dict={"Girija":"11/12/1969","Priyanka":"02/12/1999","Swami":"13/10/1956"}
print("Welcome to the birthday dictionary. We know the birthdays of:")
print("Girija")
print("Priyanka")
print("Swami")
n=input( "Who's birthday do you want to look up?")
print(n)
bday(n)
