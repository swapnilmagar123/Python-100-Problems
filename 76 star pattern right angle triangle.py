# write the python program for printing the star pattern in the right angle triangle
a = int(input("Enter the number here"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
