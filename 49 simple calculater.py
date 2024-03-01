# write the python program simple calcular;
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
print(" for addtion press 1\n for subtraction press 2 \n for multiplication press 3\n for division press 4 \n")
choice=int(input("Enter the number from 1 to 4 : "))
if (choice==1):
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif (choice==3):
    print(num1*num2)
elif(choice==4):
    print(num1/num2)
else:
    print("invalid")