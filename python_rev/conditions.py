age=int(input("Enter your age : "))
gender=input("Enter gender : ")

if age>=18:
    print("You may drink")
    if age<=50:
        print("Wine..!")
elif gender=="Male":
    print("Tie")   
else:
    print("Heels")    
    
print("Thanks for visiting!")   