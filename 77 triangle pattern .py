# write the python program for printing the triangle
a = int(input("Enter the number herer"))
for i in range(0, a):
    for j in range(0 ,a-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()