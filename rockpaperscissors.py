player1=input("enter name of player 1")
player2=input("enter name of player 2")
n=int(input("enter the number of games to play"))


def games(n):
    num1=0
    num2=0
    for i in range(n):
        p1=input("player 1, enter rock or paper or scissor")
        p2=input("player 2, enter rock or paper or scissor")
        if((p1=="rock" and p2=="scissor") or (p1=="scissor" and p2=="paper") or (p1=="paper" and p2=="rock") ):
            print("player 1 wins")

            num1=num1+1


        elif(p1==p2):
            print("draw")
        else:
            print("player 2 wins")

            num2=num2+1


    return [num1, num2]

list=games(n)
print(list)

for i in list:

    if(list[0]>list[1]):
        print("congrats player 1 winner")
    else:
        print("congrats player 2 winner")

'''
for i in l:
    if(num1>num2):
        print("congrats player 1")
    else:
        print("congrats player 2")
'''
