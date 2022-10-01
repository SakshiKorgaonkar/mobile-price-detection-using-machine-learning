#2 player game asks for name choices no of matches to be played & provide individual mattch & whole series result in the end.

player1=input("Enter name of the first player : ")
y=int(input("How many matches do you want to play ? "))
player2=input("Enter name of the second player : ")
b=int(input("How many matches do you want to play ? "))

points1=0
points2=0

print("Let's get started!!!")

for i in range(y):
    z=input("stone,paper,scissor - ")
    c=input("stone,paper,scissor - ")
    if ((z=="stone" and c=="scissor") or (z=="scissor" and c=="paper") or (z=="paper" and c=="stone")) :
        print(player1 , "won!!")
        points1+=1
    elif ((z=="stone" and c=="stone") or (z=="scissor" and c=="scissor") or (z=="paper" and c=="paper")) :
        print("Try again :(")
        points1+=0 
    elif ((z=="scissor" and c=="stone") or (z=="paper" and c=="scissor") or (z=="stone" and c=="paper")) :
        print(player2 , "won!!")
        points2+=1
    else:
        print("Invalid input.")
        points2+=0
        points1+=0

if(points1>points2):
    print("The winner is - " , player1 , "Points scored - ", points1)
elif(points2>points1): 
    print("The winner is - " , player2 , "Points scored - ", points2) 
elif(points2==points1):
    print("The match was a tie.")


