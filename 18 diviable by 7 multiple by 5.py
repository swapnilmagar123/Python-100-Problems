# write the python program for checking the numner which is divisiable by 7 and multiple by 5 in the range
a = int(input("Enter the number that you want to check lower"))
b = int(input("Enter the number that you want to check higher"))
for i in range(a,b):
    if (i%7==0) and (i%5==0):
        print(i)