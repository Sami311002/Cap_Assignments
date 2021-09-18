choice = 0
print("1. Add")
print("2. Subtract:")
choice = int(input("Enter choice:"))
Number1 = int(input("Enter number1:"))
Number2 = int(input("Enter number2:"))             
if (choice == 1):
    result = Number1+Number2
    print("The result after adding =", result)
elif (choice == 2):
    result = Number1-Number2
    print("The result after subtracting =", result)
else :
    print("Wrong choice entered")
   
